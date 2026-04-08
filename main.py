import package
import compress
import sys
from pathlib import Path
from datetime import datetime

start = datetime.now()

# Get the command arguments
args: list = sys.argv[1:]

command: str
arguments: list = []

# Get the command
if args[0] == 'pack':
    command = 'pack'
elif args[0] == 'compressDir':
    command = 'compressDir'
elif args[0] == 'compress':
    command = 'compress'
else:
    print(f'Unkown command: {args[0]}')
    sys.exit(1)

# Parse the arguments
pos: int = 1 # Position in arguments
length: int = len(args)
has_input_file: bool = False
input_file: str
has_output_file: bool = False
output_file: str
has_second_input_file: bool = False
second_input_file: str
while length > pos:
    if args[pos] == '-preset' and len(args) > pos:
        arguments.append(('-preset', args[pos+1]))
        pos += 2
    else:
        if not has_input_file:
            has_input_file = True
            input_file = args[pos]
            pos += 1
        elif not has_output_file:
            has_output_file = True
            output_file = args[pos]
            pos += 1
        elif not has_second_input_file:
            has_second_input_file = True
            second_input_file = args[pos]
            pos += 1


# Run the program
if __name__ == '__main__':
    if command == 'pack':
        package.pack(Path(input_file), Path(output_file), arguments)
    elif command == 'compressDir':
        compress.compress_dir(Path(input_file), Path(output_file), arguments)
    elif command == 'compress':
        compress.compress_single(Path(input_file), Path(output_file), Path(second_input_file), arguments)

end = datetime.now()

print(f'Operation complete!\tTime elapsed: {start - end}')