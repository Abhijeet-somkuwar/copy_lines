import sys

def copy_lines_from_log(input_file, output_file, start_line, end_line):
    try:
        # Open the input log file
        with open(input_file, 'r') as infile:
            with open(output_file, 'w') as outfile:
                # Iterate through the log file line by line
                for current_line_number, line in enumerate(infile, start=1):
                    # Write to output file only if the line is within the specified range
                    if start_line <= current_line_number <= end_line:
                        outfile.write(line)
                    elif current_line_number > end_line:
                        # Stop processing once we've reached beyond the end line
                        break

        print(f"Lines {start_line} to {end_line} have been copied to {output_file}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script_name.py <input_file> <output_file> <start_line> <end_line>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    start_line = int(sys.argv[3])
    end_line = int(sys.argv[4])
    
    # Ensure valid line numbers
    if start_line <= 0 or end_line < start_line:
        print("Error: Invalid line number range.")
        sys.exit(1)
    
    copy_lines_from_log(input_file, output_file, start_line, end_line)
