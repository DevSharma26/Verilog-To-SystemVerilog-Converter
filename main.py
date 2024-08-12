import re
import os

class VerilogToSystemVerilogConverter:
    def __init__(self, verilog_code):
        self.verilog_code = verilog_code
        self.systemverilog_code = ""

    def convert(self):
        # Replace 'reg' with 'logic'
        self.systemverilog_code = re.sub(r'\breg\b', 'logic', self.verilog_code)

        # Replace 'always @(*)' with 'always_comb'
        self.systemverilog_code = re.sub(r'always @\(\*\)', 'always_comb', self.systemverilog_code)

        # Replace 'always @(posedge clk or posedge reset)' with 'always_ff @(posedge clk or posedge reset)'
        self.systemverilog_code = re.sub(r'always @\(posedge (\w+) or posedge (\w+)\)',
                                         r'always_ff @(\1 or \2)', self.systemverilog_code)

        # Replace 'always @(posedge clk)' with 'always_ff @(posedge clk)'
        self.systemverilog_code = re.sub(r'always @\(posedge (\w+)\)',
                                         r'always_ff @(\1)', self.systemverilog_code)

        # Replace 'always @(negedge clk)' with 'always_ff @(negedge clk)'
        self.systemverilog_code = re.sub(r'always @\(negedge (\w+)\)',
                                         r'always_ff @(\1)', self.systemverilog_code)

        # Replace 'integer' with 'int'
        self.systemverilog_code = re.sub(r'\binteger\b', 'int', self.systemverilog_code)

        # Compact parameter declaration using 'localparam'
        self.systemverilog_code = re.sub(r'parameter\s+(\w+)\s*=\s*(\d+);',
                                         r'localparam \1 = \2;', self.systemverilog_code)

        # For loop integer declaration
        self.systemverilog_code = re.sub(r'for\s*\((\w+)\s*=\s*(\d+);',
                                         r'for (int \1 = \2;', self.systemverilog_code)

        # Generate block logic
        self.systemverilog_code = re.sub(r'(generate\s*)(.*)(endgenerate)',
                                         r'\1logic \2;\3', self.systemverilog_code, flags=re.DOTALL)

        # Initial block enhancement
        self.systemverilog_code = re.sub(r'\binitial\b', 'initial begin', self.systemverilog_code)

        # Skip conversion for continuous assignments
        def logic_conversion(match):
            if "assign" in match.group(0):
                return match.group(0)
            return re.sub(r'\bwire\b', 'logic', match.group(0))

        self.systemverilog_code = re.sub(r'\bwire\b.*?;', logic_conversion, self.systemverilog_code, flags=re.DOTALL)

        # Task and function enhancements
        self.systemverilog_code = re.sub(r'\btask\b', 'task void', self.systemverilog_code)
        self.systemverilog_code = re.sub(r'\bfunction\s+(\w+)\b', r'function logic \1', self.systemverilog_code)

        # Replace '==' with '===' for bitwise comparison
        self.systemverilog_code = re.sub(r'==', '===', self.systemverilog_code)

        # Named blocks for begin-end
        self.systemverilog_code = re.sub(r'\bbegin\b', 'begin : block_name', self.systemverilog_code)
        self.systemverilog_code = re.sub(r'\bend\b', 'end : block_name', self.systemverilog_code)

        # Removing deprecated keywords
        self.systemverilog_code = re.sub(r'\btri\b', '', self.systemverilog_code)
        self.systemverilog_code = re.sub(r'\btriand\b', '', self.systemverilog_code)

        return self.systemverilog_code

def convert_file(verilog_file_path):
    # Read the Verilog file
    with open(verilog_file_path, 'r') as file:
        verilog_code = file.read()

    # Create an instance of the converter and convert the code
    converter = VerilogToSystemVerilogConverter(verilog_code)
    systemverilog_code = converter.convert()

    # Determine the output file path
    base_name = os.path.splitext(verilog_file_path)[0]
    systemverilog_file_path = f"{base_name}.sv"

    # Save the SystemVerilog code to a new file
    with open(systemverilog_file_path, 'w') as file:
        file.write(systemverilog_code)

    print(f"Conversion complete! SystemVerilog file saved as: {systemverilog_file_path}")

# Example usage:
verilog_file_path = "sample_verilog_code.v"  # Replace with your Verilog file path
convert_file(verilog_file_path)
