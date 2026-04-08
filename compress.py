import json
import sys
import os
import subprocess
from multiprocessing import Pool
from pathlib import Path
import psutil

p = psutil.Process(os.getpid())
p.nice(psutil.IDLE_PRIORITY_CLASS)

with open('paths.json') as file:
        ffmpeg: str = json.load(file)['ffmpeg']

def compress_single(input_dir: Path, output_dir: Path, input_file: Path, arguments: list) -> None:
    # Default argument values
    preset: str = 'faster'
    
    for argument in arguments:
        if argument[0] == '-preset':
             preset = argument[1]
    
    os.makedirs((input_dir / output_dir) / os.path.dirname(input_file), exist_ok=True)

    print(f'[Staring: {input_file}]')
    try:
        subprocess.run(
            [ffmpeg, '-y', '-i', input_dir / input_file,
            '-c:v', 'libx265', 
            '-crf', '23',
            '-preset', preset,
            '-c:a', 'copy',
            '-threads', '2'
            (input_dir / output_dir) / input_file],
            check=True)
        print(f'[{input_file} completed.]')
    except Exception as e:
        print(f'[{input_file} failed:\n{e}]')

# Remember to use `if __name__ == '__main__'`
def compress_dir(input: Path, output: Path, arguments: list) -> None:
    # Get all video paths
    video_paths: list = [p.relative_to(input) for p in input.rglob('*.mp4')]

    jobs = [(input, output, p, arguments) for p in video_paths]

    with Pool(2) as pool:
         pool.starmap(compress_single, jobs)
