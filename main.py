import sys
from pathlib import Path

from compress import compress

input_file: Path
output_file: Path
preset_flag: str = 'slow'

cmd_arguments = sys.argv[1:]

# Used to look ahead of a list without worrying about whether the value exists
def peek(input: list, position: int):
    if len(input) > position+1:
        return input[position+1]
    
    # Returns nothing if value a cannot be found
    return None

# Checks for any command line arguments.
# If none are provided, app gets them manually.
if len(cmd_arguments) < 2:
    print('No arguments were passed.')
    print('At least two arguments are required:\n1. Input file (the one to be compressed)\n2. Output file (where that compressed file will go)')
    print('You can also add a `-preset` flag to specify the libx265 preset. (Defaults to slow)')

    # Some error handling might be a possibility here.
    input_file = Path(input('Input file: '))
    output_file = Path(input('Output file: '))
    preset_flag_buffer = input('Preset flag (leave blank if none): ')

    # Check preset flag values
    if preset_flag_buffer != '':
        preset_flag = preset_flag_buffer
        
# Case that arguments were given
else:
    paths: list = []

    # Parse arguments
    position: int = 0
    while position < len(cmd_arguments):
        # Preset flag
        if cmd_arguments[position] == '-preset':
            next_token = peek(cmd_arguments, position)

            if next_token != None:
                preset_flag = next_token
                position += 2 
        # Path
        else:
            paths.append(cmd_arguments[position])
            position += 1


    # Check for potential errors
    if len(paths) !=  2:
        raise ValueError("Incorrect count of paths was provided.\nExactly two paths should be given: 1 in and 1 out.")
    
    input_file = Path(paths[0])
    output_file = Path(paths[1])
    
compress(input_file, output_file, preset_flag)