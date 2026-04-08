import json
import os
import compress
from pathlib import Path
import subprocess
import shutil

with open('paths.json') as file:
    zipper: str = json.load(file)["7zip"] # Loads 7zip as 'zipper' because 
                                          # variables cannot start with numbers.

def pack(input: Path, output: Path, arguments: list):
    print('[Starting compressing.]')
    compress.compress_dir(input, output, arguments)
    print('[Compression finished!]')

    if os.path.isdir(f'{input}/Thumbnail Art'):
        shutil.copytree(f'{input}/Thumbnail Art', f'{input / output}/Thumbnail Art', dirs_exist_ok=True)

    print('[Starting packaging.]')
    subprocess.run([
        zipper, 'a', '-t7z',
        '-m0=lzma2', '-mx=9',
        f'{input / output}/{output}.7z', input / output
    ])
    print('[Packaging finished!]')