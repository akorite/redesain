// The datapath run BY HAND: this bench plays the control unit the
// ch16 FSM will become, driving one 11-bit control word per step and
// checking registers, flags, OUT and the PC as the program executes.
// Program (ch15_program.hex):
//   0: LDI A,5      2: MOV r1   3: LDI A,3   5: MOV r2
//   6: ADD r1       7: SUB r1   8: OUT       9: HALT
`timescale 1ns/1ps
module datapath_tb;
  localparam OP_ADD=3'b000, OP_SUB=3'b001;
  localparam WB_ALU=2'b00, WB_IMM=2'b01, WB_PA=2'b10;
  localparam PC_NEXT=2'b00, PC_SKIP=2'b01, PC_HOLD=2'b11;

  reg clk = 0, rst = 1;
  reg [2:0] alu_op = 0;
  reg [1:0] wb_sel = 0, pc_mode = 0;
  reg dst_sel = 0, we = 0, flags_we = 0, out_we = 0;
  wire [3:0] pc;
  wire [7:0] instr, imm, a, rb, out;
  wire z, n, c, v;
  integer errors = 0;

  datapath u(.i_clk(clk), .i_rst(rst),
    .i_alu_op(alu_op), .i_wb_sel(wb_sel), .i_dst_sel(dst_sel),
    .i_we(we), .i_flags_we(flags_we), .i_out_we(out_we),
    .i_pc_mode(pc_mode),
    .o_pc(pc), .o_instr(instr), .o_imm(imm), .o_a(a), .o_rb(rb),
    .o_out(out), .o_z(z), .o_n(n), .o_c(c), .o_v(v));

  always #5 clk = ~clk;

  task check(input [191:0] what, input [7:0] got, input [7:0] exp);
    if (got !== exp) begin
      errors = errors + 1;
      $display("FAIL %0s: got=%h exp=%h", what, got, exp);
    end
  endtask

  task step(input [2:0] op, input [1:0] wb, input dst, input [1:0] pcm);
    begin
      @(negedge clk);
      alu_op = op; wb_sel = wb; dst_sel = dst; pc_mode = pcm;
      we = 1; flags_we = 0; out_we = 0;
      @(posedge clk); #1;
      we = 0;
      $display("t=%0t pc=%d instr=%h -> a=%h rb=%h flags z%b n%b c%b v%b",
               $time, pc, instr, a, rb, z, n, c, v);
    end
  endtask

  initial begin
    $dumpfile("ch15_datapath.vcd");
    $dumpvars(0, datapath_tb);
    // reset
    @(negedge clk); rst = 1;
    @(posedge clk); #1;
    rst = 0;
    check("pc after reset", {4'd0, pc}, 8'd0);
    check("fetch rom[0]=LDI", instr, 8'h10);
    check("imm byte rom[1]",  imm,   8'h05);

    // step 1: LDI A,5  (write imm byte -> r0, pc+2)
    step(OP_ADD, WB_IMM, 1'b0, PC_SKIP);
    check("A=5", a, 8'h05); check("pc=2", {4'd0,pc}, 8'd2);

    // step 2: MOV r1 (portA -> r[1], pc+1)
    step(OP_ADD, WB_PA, 1'b1, PC_NEXT);
    // r1 isn't directly visible; prove it via the next ADD

    // step 3: LDI A,3  (pc=3 instr 10 imm 03)
    check("fetch rom[3]", instr, 8'h10);
    step(OP_ADD, WB_IMM, 1'b0, PC_SKIP);
    check("A=3", a, 8'h03); check("pc=5", {4'd0,pc}, 8'd5);

    // step 4: MOV r2 (portA -> r[2], pc+1)
    step(OP_ADD, WB_PA, 1'b1, PC_NEXT);
    check("pc=6", {4'd0,pc}, 8'd6); check("fetch rom[6]=ADD r1", instr, 8'h31);

    // step 5: ADD r1 -> A = 3 + 5 = 8, flags captured
    @(negedge clk);
    alu_op=OP_ADD; wb_sel=WB_ALU; dst_sel=0; pc_mode=PC_NEXT;
    we=1; flags_we=1; out_we=0;
    @(posedge clk); #1; we=0; flags_we=0;
    $display("t=%0t ADD: a=%h z%b n%b c%b v%b", $time, a, z, n, c, v);
    check("A=8", a, 8'h08);
    check("flags ZN CV", {4'b0, z, n, c, v}, 8'b0000_0000);
    check("pc=7", {4'd0,pc}, 8'd7);

    // step 6: SUB r1 -> A = 8 - 5 = 3 (C=1 means no borrow)
    @(negedge clk);
    alu_op=OP_SUB; wb_sel=WB_ALU; dst_sel=0; pc_mode=PC_NEXT;
    we=1; flags_we=1;
    @(posedge clk); #1; we=0; flags_we=0;
    check("A=3", a, 8'h03);
    check("C=1 no borrow", {7'b0, c}, 8'b1);
    check("V=0", {7'b0, v}, 8'b0);
    check("pc=8", {4'd0,pc}, 8'd8); check("fetch rom[8]=OUT", instr, 8'h80);

    // step 7: OUT (out_we captures A)
    @(negedge clk);
    out_we=1; pc_mode=PC_NEXT;
    @(posedge clk); #1; out_we=0;
    check("OUT=3", out, 8'h03);
    check("pc=9", {4'd0,pc}, 8'd9); check("fetch rom[9]=HALT", instr, 8'h90);

    // step 8: HALT freezes the PC
    @(negedge clk);
    pc_mode=PC_HOLD;
    @(posedge clk); #1;
    check("pc held at 9", {4'd0,pc}, 8'd9);
    @(posedge clk); #1;
    check("pc still 9", {4'd0,pc}, 8'd9);

    if (errors == 0)
      $display("PASS: datapath executed 8 control-word steps clean");
    $finish;
  end
endmodule
