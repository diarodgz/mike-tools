import re

def clean_data_line(line):
    
    line = line.replace('"', '').strip()

    # Step 0: Get rid of extra quotation mark and space
    line = re.sub(r'(\d+) = (\d+) 1 0(\d+\.\d+) (\d+\.\d+) 2048 (\d+\.\d+) (\d+\.\d+) (\d+\.\d+)', r'\1 = \2 1 0 \3 \4 2048 \5 \6 \7', line)

    # Step 1: Insert a missing space between numbers that need it (between floats and integers)
    line = re.sub(r'(\d+) = (\d+) 1 0(\d+\.\d+) (\d+\.\d+) 2048 (\d+\.\d+) (\d+\.\d+) (\d+\.\d+)', r'\1 = \2 1 0 \3 \4 2048 \5 \6 \7', line)  # handles cases like "4961.45766212217310.050..."

    # Step 2: Ensure a space between the '2048' and any other connected number
    line = re.sub(r'(\d+) = (\d+) 1 0 (\d+\.\d+) (\d+\.\d+)2048 (\d+\.\d+) (\d+\.\d+) (\d+\.\d+)', r'\1 = \2 1 0 \3 \4 2048 \5 \6 \7', line)  # Fix missing space after 2048

    # Separate the (\d+\.\d+)(\d+\.\d+)
    line = re.sub(r'(\d+) = (\d+) 1 0 (\d+\.\d+)(\d+\.\d+) 2048 (\d+\.\d+) (\d+\.\d+) (\d+\.\d+)', r'\1 = \2 1 0 \3 \4 2048 \5 \6 \7', line)

    # Separate =(\d+)
    line = re.sub(r'(\d+) =(\d+) 1 0 (\d+\.\d+) (\d+\.\d+) 2048 (\d+\.\d+) (\d+\.\d+) (\d+\.\d+)', r'\1 = \2 1 0 \3 \4 2048 \5 \6 \7', line)
 
    # Separate (\d+)1
    line = re.sub(r'(\d+) = (\d+)1 0 (\d+\.\d+) (\d+\.\d+) 2048 (\d+\.\d+) (\d+\.\d+) (\d+\.\d+)', r'\1 = \2 1 0 \3 \4 2048 \5 \6 \7', line)

    # Separate (\d+)=
    line = re.sub(r'(\d+)= (\d+) 1 0 (\d+\.\d+) (\d+\.\d+) 2048 (\d+\.\d+) (\d+\.\d+) (\d+\.\d+)', r'\1 = \2 1 0 \3 \4 2048 \5 \6 \7', line)

    # Step 3: Ensure the structure matches the expected pattern
    pattern = re.compile(r'(\d+) = (\d+) 1 0 (\d+\.\d+) (\d+\.\d+) 2048 (\d+\.\d+) (\d+\.\d+) (\d+\.\d+)')
    match = pattern.match(line)
    
    if match:
        return match.group(0)  # Return the cleaned line
    else:
        #print(f"Line couldn't be cleaned properly: {line}")
        return line