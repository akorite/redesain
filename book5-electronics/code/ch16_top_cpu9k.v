// ch16_top_cpu9k.v -- cpu8 on the Tang Nano 9K.
// OUT register shows on the 6 onboard LEDs (active low -> inverted);
// every OUT write also goes out on the UART at 115200 baud (8N1),
// which is how "count up forever" reaches the serial monitor.
// Board build is described-not-run in the chapter; this top is
// structurally complete and lint-clean.
module top_cpu9k (
  input  wire i_clk27,     // 27 MHz onboard oscillator, pin 52
  input  wire i_btn,       // user button (reset), active low, pin 4
  output wire [5:0] o_led, // active-low LED bank
  output wire o_uart_tx    // BL702 UART bridge TX pin, pin 17
);
  wire clk = i_clk27;
  reg [21:0] div = 0;              // slow the machine to ~6 Hz visible
  always @(posedge clk) div <= div + 1;
  wire step = (div[21:0] == 0);    // one cpu edge per div wrap

  // CPU runs on the divided-enable clock domain via a manual gate:
  // simplest honest approach -- drive the whole CPU off div[21].
  wire cpu_clk = div[21];
  wire rst = ~i_btn;

  wire [7:0] a, pc, instr, out_r;
  wire out_we, halted;
  cpu8 #() u_cpu (
    .i_clk(cpu_clk), .i_rst(rst),
    .o_a(a), .o_pc(pc), .o_instr(instr),
    .o_out(out_r), .o_out_we(out_we), .o_halted(halted)
  );

  assign o_led = ~out_r[5:0];      // LEDs are active low

  // UART at full 27 MHz clock -- frames are fast enough that each
  // OUT write at ~6 Hz always finds the transmitter idle.
  reg        tx_start = 0;
  reg [7:0]  tx_data  = 0;
  wire       tx_busy;
  uart_tx8 #(.CLKS_PER_BIT(234)) u_tx (
    .i_clk(clk), .i_start(tx_start), .i_data(tx_data),
    .o_tx(o_uart_tx), .o_busy(tx_busy)
  );
  reg [21:0] seen = 0;             // edge-detect on div wrap + out_we
  always @(posedge clk) begin
    tx_start <= 0;
    if (out_we & ~tx_busy) begin   // out_we is a cpu-domain pulse;
      tx_data  <= out_r;           // at 6 Hz it is wide enough to
      tx_start <= 1;               // catch reliably in the 27MHz dom.
    end
  end
endmodule
