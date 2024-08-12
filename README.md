# Verilog to SystemVerilog Conversion Tool

## Project Overview

The Verilog to SystemVerilog Conversion Tool is designed to automatically convert Verilog code into SystemVerilog code. SystemVerilog extends Verilog with additional features and improvements, making this tool essential for upgrading legacy Verilog codebases to SystemVerilog. This tool simplifies the conversion process and ensures that the code adheres to SystemVerilog standards.

## Features

- **Syntax Conversion**: Converts Verilog constructs to their SystemVerilog equivalents.
- **Parameter and Localparam Handling**: Updates `parameter` declarations to `localparam`.
- **Always Blocks**: Converts `always @(*)` to `always_comb` and `always @(posedge clk or posedge reset)` to `always_ff @(posedge clk or posedge reset)`.
- **Task and Function Enhancement**: Updates tasks and functions to conform to SystemVerilog syntax.
- **Initial Blocks**: Converts initial blocks to SystemVerilog format.
- **Comments and Documentation**: Preserves and adds comments to ensure code clarity.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Verilog-to-SystemVerilog-Converter.git

2. **Navigate to the Project Directory:**:
   ```bash
   cd Verilog-to-SystemVerilog-Converter

3.** Install Dependencies**:
- **This project requires Python 3.x. Ensure you have Python installed.
- **No additional dependencies are required beyond Python's standard library.

## Usage

1. **Prepare Your Verilog File**:
- **Place the Verilog file you want to convert in the project directory.
- **Run the Conversion Script:

2.**Use the Python script to convert the Verilog file to SystemVerilog**:
```bash
   python verilog_to_systemverilog.py <verilog_file_path>
```
3. **Check the Output**:
- **The converted SystemVerilog file will be saved in the same directory with the .sv extension.

