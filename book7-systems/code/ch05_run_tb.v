// ch05_run_tb.v -- one generic testbench for all three cores.
//   -DSC    ch05 single-cycle core      -DPIPE  ch06 naive pipeline
//   (neither) ch07 forwarding/stall/flush pipeline
// Plusargs: +hex=prog.hex  +halt=<byte address of `halt: j halt`>
//           +cyc=<cycles to run>  +nret=<which retire pulse to time>
// Prints one metrics line, then every nonzero register and data word in
// the same format as ch05_golden.py, so the two outputs can be diffed.
`timescale 1ns/1ps
module run_tb;
  reg clk = 0, rst = 1;
  wire [31:0] pc, da, dw; wire dwe, ret, st;
  reg [31:0] imem [0:63];
  reg [31:0] dmem [0:255];
  wire [31:0] insn = imem[pc[7:2]];
  wire [31:0] drd  = dmem[da[9:2]];
`ifdef SC
  rv32i_sc_top dut(.clk(clk), .rst(rst), .insn(insn), .dmem_rdata(drd),
    .pc(pc), .dmem_addr(da), .dmem_wdata(dw), .dmem_we(dwe),
    .retired(ret));
  assign st = 1'b0;
  localparam NAME = "single-cycle";
`elsif PIPE
  rv32i_pipe_top dut(.clk(clk), .rst(rst), .insn_f(insn),
    .dmem_rdata(drd), .pc_f(pc), .dmem_addr(da), .dmem_wdata(dw),
    .dmem_we(dwe), .retired(ret));
  assign st = 1'b0;
  localparam NAME = "naive-pipe";
`else
  rv32i_fwd_top dut(.clk(clk), .rst(rst), .insn_f(insn),
    .dmem_rdata(drd), .pc_f(pc), .dmem_addr(da), .dmem_wdata(dw),
    .dmem_we(dwe), .retired(ret), .stalled(st));
  localparam NAME = "fwd-pipe";
`endif
  always #5 clk = ~clk;
  always @(posedge clk) if (dwe) dmem[da[9:2]] <= dw;

  reg [1023:0] hexfile;
  integer halt, ncyc, nret, i;
  integer cyc, F, stalls, taken, retires, lastret;
  reg seen; reg doTrace;
  initial begin
    if (!$value$plusargs("hex=%s", hexfile))  hexfile = "ch05_prog.hex";
    if (!$value$plusargs("halt=%d", halt))    halt = 48;
    if (!$value$plusargs("cyc=%d", ncyc))     ncyc = 300;
    if (!$value$plusargs("nret=%d", nret))    nret = 0;
    for (i = 0; i < 256; i = i + 1) dmem[i] = 0;
    $readmemh(hexfile, imem);
    cyc = 0; F = -1; stalls = 0; taken = 0; retires = 0; lastret = -1;
    seen = 0; doTrace = $test$plusargs("trace");
    #12 rst = 0;
    while (cyc < ncyc) begin
      @(posedge clk);
      if (!seen && pc == halt) begin F = cyc; seen = 1; end
      if (st) stalls = stalls + 1;
`ifdef SC
      if (doTrace && !seen)
        $display("T %2d pc=%h insn=%h imm=%h alu=%h next=%h", cyc, pc,
                 insn, dut.imm, dut.alu_y, dut.pc_next);
`endif
`ifdef SC
`elsif PIPE
`else
      if (dut.brtake) taken = taken + 1;
`endif
`ifdef SC
      if (ret) begin
`else
      // count only real register writes: the nops that fill the pipe
      // after reset also assert `retired` but write x0
      if (ret && dut.wbwa != 5'd0) begin
`endif
        retires = retires + 1;
        if (retires == nret) lastret = cyc + 1;
      end
      cyc = cyc + 1;
    end
    $display("CORE=%0s F=%0d stalls=%0d taken=%0d lastret=%0d",
             NAME, F, stalls, taken, lastret);
    for (i = 1; i < 32; i = i + 1)
      if (dut.rf.x[i] !== 32'd0) $display("x%0d=%08x", i, dut.rf.x[i]);
    for (i = 0; i < 16; i = i + 1)
      if (dmem[i] !== 32'd0) $display("m%0d=%08x", i, dmem[i]);
    $finish;
  end
endmodule
