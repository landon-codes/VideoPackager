from enum import Enum
from pathlib import Path
import sys

# Metadata
program_structure = "command <arguments> input_path relative_output_path"
valid_commands = ["pack", "compress"]

# An enum containing the commands that can be run
class CommandType(Enum):
    Pack = "pack"
    Compress = "compress"
    Undefined = "undefined" # Only used as starting value

class Program:
    def __init__(self, program_type: CommandType, progam_input: Path, program_output: Path, program_arguments: list):
        self.command: CommandType = program_type
        self.arguments: list = program_arguments 
        self.input_path: Path = progam_input
        self.output_path: Path = program_output

def parse(input: list) -> Program:
    # Checks for sufficient arguments
    if len(input) < 3:
        print("Insufficient arguments.\nAt least three arguments are required:")
        print("- command\n- input path\n- output path (relative to the input path)") 

    # Required/Default values
    type: CommandType = CommandType.Undefined
    arguments: list = []
    preset: str = "" 

    # Gets the base command
    if (input[0] == "pack"):
        type = CommandType.Pack
    elif (input[0] == "compress"):
        type = CommandType.Compress
    # Invalid command
    else: 
        print(f"{input[0]} is not a valid command. Here is a list of valid commands:")
        for comm in valid_commands:
            print(f"- {comm}")
        sys.exit(1)

    # Parses the remaining arguments and paths
    position: int = 1
    has_input: bool = False
    has_output: bool = False
    input_path: Path 
    output_path: Path

    while position < len(input):
        # -preset
        if input[position] == "-preset" and position+1 < len(input):
            position += 1
            arguments.append(("preset", input[position]))
            position += 1
        # Paths
        else:
            if not has_input:
                input_path = Path(input[position])
                has_input = True
                position += 1
            elif not has_output:
                output_path = Path(input[position])
                has_output = True
                position += 1

    return Program(type, input_path, output_path, arguments)