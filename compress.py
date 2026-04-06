import json
import os
import sys
import subprocess
from multiprocessing import Pool
from pathlib import Path

with open("paths.json") as file:
    ffmpeg = json.load(file)["ffmpeg"]

# Make sure enough aruments are provided.
if len(sys.argv) < 3:
    print("Usage: py compress.py <input_folder> <output_subfolder>")
    sys.exit(1)

in_dir = Path(sys.argv[1]).resolve()
out_dir = in_dir / sys.argv[2]

# Create output directory
out_dir.mkdir(parents=True, exist_ok=True)

# Collect all .mp4 files (relative paths)
videos = [p.relative_to(in_dir) for p in in_dir.rglob("*.mp4")]

if not videos:
    print("No .mp4 files found.")
    sys.exit(0)

# Compresses a single video using FFmpeg
def compress(relative_path: Path):
    video_path_in = in_dir / relative_path
    video_path_out = out_dir / relative_path

    # Ensure output subfolders exist
    video_path_out.parent.mkdir(parents=True, exist_ok=True)

    command = [
        ffmpeg,
        "-y",
        "-i", str(video_path_in),
        "-c:v", "libx265",
        "-crf", "24",
        "-preset", "faster",
        "-c:a", "copy",
        str(video_path_out)
    ]

    print(f"[START] {relative_path}")

    try:
        subprocess.run(command, check=True)
        print(f"[OK] {relative_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[FAILED] {relative_path} — {e}")
        return False

# Main multiprocessing block
if __name__ == "__main__":
    print(f"Input directory:  {in_dir}")
    print(f"Output directory: {out_dir}")
    print(f"Found {len(videos)} videos.\n")

    with Pool(processes=3) as pool:
        pool.map(compress, videos)

    print("\nDone.")