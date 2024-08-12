module sample_module(
  input wire clk,
  input wire reset,
  input wire [7:0] data_in,
  output reg [7:0] data_out
);

  // Internal signals
  reg [7:0] temp_reg;
  wire valid;

  // Parameter declaration
  parameter WIDTH = 8;

  // Combinational logic
  always @(*) begin
      if (data_in > 8'h80)
          temp_reg = data_in;
      else
          temp_reg = 8'h00;
  end

  // Sequential logic
  always @(posedge clk or posedge reset) begin
      if (reset)
          data_out <= 8'h00;
      else
          data_out <= temp_reg;
  end

  // Simple task
  task example_task;
      input [7:0] value;
      begin
          $display("Value: %h", value);
      end
  endtask

  // Simple function
  function [7:0] example_function;
      input [7:0] a, b;
      begin
          example_function = a + b;
      end
  endfunction

  // Initial block for simulation
  initial begin
      $monitor("Data out: %h", data_out);
  end

endmodule
