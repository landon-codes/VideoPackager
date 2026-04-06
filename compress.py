import json
import sys
import os
import subprocess
from multiprocessing import Pool
from pathlib import Path

with open('paths.json') as file:
        ffmpeg: str = json.load(file)['ffmpeg']

def compress_single(input: Path, output: Path) -> None:
    os.makedirs(input / output, exist_ok=True)

    print(f'Staring: {input}')
    try:
        subprocess.run(
            [ffmpeg, '-y', '-i', input,
            '-c:v', 'libx265', 
            '-crf', '23',
            '-preset' 'ultrafast', #TODO: impliment manual/custom preset input
            '-c:a', 'copy',
            input / output],
            check=True)
        print(f'{input} completed.')
    except Exception as e:
        print(f'{input} failed:\n{e}')

def compress_dir(input: Path, output: Path) -> None:
    # Get all video paths
    video_paths: list = [p.relative_to(input) for p in input.rglob('*.mp4')]

    #TODO: Impliment the remaining logic