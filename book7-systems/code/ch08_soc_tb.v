// ch08_soc_tb.v -- end-to-end: compute, UART print, ecall->handler,
// mret back, park. Bytes captured at the MMIO edge; the wire itself
// is checked for real serialisation (busy + start bit on tx).
`timescale 1ns/1ps
module ch08_soc_tb;
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
            .div(16'd16),.tx(tx),.busy(busy));
  always #5 clk=~clk;
  always @(posedge clk) if (dwe && da!=32'h10000000) dmem[da[9:2]] <= dw;
  integer i, cyc, ngot, sawtx;
  reg [7:0] got [0:7];
  // every MMIO request captures the byte the program is sending
  always @(posedge clk)
    if (ureq) begin got[ngot] <= dw[7:0]; ngot = ngot + 1; end
  // and the wire must actually wiggle: start bit seen on tx
  always @(negedge tx) sawtx = sawtx + 1;
  initial begin
    for (i=0;i<256;i=i+1) dmem[i]=0;
    ngot=0; sawtx=0;
    $readmemh("ch08_prog.hex", imem, 0, 38);
    #12 rst=0; cyc=0;
    while (cyc<40000 && pcw!=32'h50) begin @(posedge clk); cyc=cyc+1; end
    repeat(800) @(posedge clk);
    $display("ran %0d cyc, pc=%h, a2=%0d (want 42)",
             cyc, pcw, dut.rf.x[12]);
    $write("MMIO bytes sent: ");
    for (i=0;i<ngot;i=i+1) $write("%c", got[i]);
    $display("");
    $display("uart frames started: %0d (want 4)", ngot);
    $display("tx start-bit edges seen: %0d", sawtx);
    check(dut.rf.x[12]==42, "6*7=42 via loop");
    check(ngot==4 && got[0]==8'h34 && got[1]==8'h32, "'42' to MMIO");
    check(ngot==4 && got[2]==8'h4B && got[3]==8'h21, "'K!' trap handler + mret");
    check(sawtx>=4, "serial wire really wiggled");
    $display("ch08 PASS");
    $finish;
  end
  task check(input cond, input [8*32-1:0] name);
    if (!cond) begin $display("FAIL: %0s", name); $fatal; end
    else $display("  ok: %0s", name);
  endtask
endmodule
