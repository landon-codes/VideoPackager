import subprocess
from pathlib import Path
import imageio_ffmpeg as ffmpeg

def compress(input_file: Path, output_file: Path, preset="slow"):
    ffmpeg_path = ffmpeg.get_ffmpeg_exe()

    cmd = [
        ffmpeg_path, "-y",
        "-i", str(input_file),
        "-c:v", "libx265",
        "-crf", "23",
        "-preset", preset,
        "-c:a", "copy",
        "-threads", "2",
        str(output_file)
    ]

    subprocess.run(cmd, check=True)