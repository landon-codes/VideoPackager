import json
import sys
import os
import subprocess
from multiprocessing import Pool
from pathlib import Path

with open('paths.json') as file:
        ffmpeg: str = json.load(file)['ffmpeg']

def compress_single(input_dir: Path, output_dir: Path, input_file: Path) -> None:
    os.makedirs(input_dir / output_dir, exist_ok=True)

    print(f'[Staring: {input_file}]')
    try:
        subprocess.run(
            [ffmpeg, '-y', '-i', input_dir / input_file,
            '-c:v', 'libx265', 
            '-crf', '23',
            '-preset', 'ultrafast', #TODO: impliment manual/custom preset input
            '-c:a', 'copy',
            (input_dir / output_dir) / input_file],
            check=True)
        print(f'[{input_file} completed.]')
    except Exception as e:
        print(f'[{input_file} failed:\n{e}]')

def compress_dir(input: Path, output: Path) -> None:
    # Get all video paths
    video_paths: list = [p.relative_to(input) for p in input.rglob('*.mp4')]

    #TODO: Impliment the remaining logic