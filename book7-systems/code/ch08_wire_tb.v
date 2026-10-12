// ch08_wire_tb.v -- decode the program's output FROM THE tx WIRE ONLY,
// the way a real terminal at the other end would: find the falling
// edge of a start bit, wait 1.5 bit times, sample 8 data bits LSB
// first, check the stop bit. Also timestamps the trap in clock cycles.
`timescale 1ns/1ps
module ch08_wire_tb;
  localparam DIV = 16;                 // clocks per bit (same as ch08_soc_tb)
  reg clk=0, rst=1;
  wire [31:0] pcw, da, dw; wire dwe, ureq, ret;
  reg [31:0] imem [0:127];
  reg [31:0] dmem [0:255];
  wire [31:0] insn = imem[pcw[8:2]];
  wire [31:0] drd  = dmem[da[9:2]];
  rv32i_soc_top dut(.clk(clk),.rst(rst),.insn_f(insn),
    .dmem_rdata(drd),.pc_f(pcw),.dmem_addr(da),.dmem_wdata(dw),
    .dmem_we(dwe),.uart_req(ureq),.retired(ret));
  wire tx, busy;
  uart_tx u(.clk(clk),.rst(rst),.valid(ureq),.data(dw[7:0]),
            .div(DIV[15:0]),.tx(tx),.busy(busy));
  always #5 clk=~clk;
  always @(posedge clk) if (dwe && da!=32'h10000000) dmem[da[9:2]] <= dw;

  integer cyc = 0;
  always @(posedge clk) if (!rst) cyc <= cyc + 1;

  // ---- trap timestamps. The loop's bne also fetches 0x44 on the wrong
  // path every iteration, so "ecall happened" means the ecall is in EX. ----
  integer c_ecall=-1, c_vec=-1, c_mret=-1, c_back=-1;
  always @(posedge clk) if (!rst) begin
    if (dut.idex_ecall && c_ecall<0) c_ecall <= cyc;
    if (c_ecall>=0 && pcw==32'h80 && c_vec<0) c_vec <= cyc;
    if (dut.idex_mret && c_mret<0) c_mret <= cyc;
    if (c_mret>=0 && pcw==32'h48 && c_back<0) c_back <= cyc;
  end

  // ---- wire decoder: knows nothing about the CPU ----
  integer nfall=0, nframes=0, k, bad=0;
  reg [7:0] byte_r; reg [7:0] dec [0:15]; integer start_cyc [0:15];
  reg prev = 1;
  always @(posedge clk) begin prev <= tx; if (prev && !tx) nfall <= nfall + 1; end
  initial begin
    wait (rst==0);
    forever begin
      @(negedge tx);                          // start bit begins
      start_cyc[nframes] = cyc;
      repeat (DIV + DIV/2) @(posedge clk);    // 1.5 bit times: middle of d0
      for (k=0;k<8;k=k+1) begin
        byte_r[k] = tx;                       // LSB first
        repeat (DIV) @(posedge clk);
      end
      if (tx !== 1'b1) bad = bad + 1;         // stop bit must be high
      dec[nframes] = byte_r; nframes = nframes + 1;
    end
  end

  integer i;
  reg [8*80-1:0] hexname;
  initial begin
    if (!$value$plusargs("hex=%s", hexname)) hexname = "ch08_prog.hex";
    for (i=0;i<256;i=i+1) dmem[i]=0;
    $readmemh(hexname, imem, 0, 38);
    #12 rst=0;
    repeat (1400) @(posedge clk);
    $write("decoded from tx wire: ");
    for (i=0;i<nframes;i=i+1) $write("%c", dec[i]);
    $display("");
    $display("frames=%0d  bad stop bits=%0d  falling edges on tx=%0d",
             nframes, bad, nfall);
    for (i=0;i<nframes;i=i+1)
      $display("  frame %0d: byte 0x%h  start-bit cycle %0d", i, dec[i], start_cyc[i]);
    $display("ecall in EX at cycle %0d; fetch pc becomes 0x80 at cycle %0d (%0d cycles later)",
             c_ecall, c_vec, c_vec - c_ecall);
    $display("mret in EX at cycle %0d; fetch pc is back at 0x48 at cycle %0d (%0d cycles later)",
             c_mret, c_back, c_back - c_mret);
    if (nframes==4 && dec[0]==8'h34 && dec[1]==8'h32 && dec[2]==8'h4B &&
        dec[3]==8'h21 && bad==0 && nfall==13)
      $display("ch08 WIRE PASS");
    else $display("ch08 WIRE FAIL");
    $finish;
  end
endmodule
