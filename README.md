# VideoPackager
A Python program for Windows that bundles 7Zip and FFmpeg to compress and package videos into a single file for easy archiving/sharing.

## Installation

You will have to download the project's source code and run it yourself using a python interperator.
This application is built for Windows only.

## Usage

This tool provides a few functions for encoding and packaging video projects.

- pack <ROOT_FOLDER_PATH> <OUTPUT_DIRECTORY> arguments

`pack` uses FFmpeg to compile all videos in a folder, and pack those images with potential thumbnail art into a .7z file for extreme storage savings.

The root folder path is the path to your project. I reccomend it be absolute. 
The output directory is the directory where you want your compiled videos/thumbnails to be outputed; this path is relative to the input directory. It **CANNOT** be absolute, and will always be placed under the input directory.

Currently the only argument is `-preset`, which sets the speed and quality FFmpeg uses to compress videos. Due to the amount of time it takes to compile large directories, this defaults to `faster`, but you can view FFmpeg documentation for other presets.

If a folder titled `Thumbnail Art` is included in the folder, images included in this folder will be packaged with the video files.

- compileDir <ROOT_FOLDER_PATH> <OUTPUT_DIRECTORY> arguments

`compileDir` uses FFmpeg to only compile video files. The arguments behave the same as the `pack` function.

- compress <ROOT_FOLDER_PATH> <OUTPUT_DIRECTORY> <OUTPUT_FILE> arguments

`compress` uses FFmpeg to only compile a single file. It takes the absolute path where the file is located, the relative directory where to store the file, and the file to store the encoded video in.

Just as before, the only argument is `-preset`.

## License/Contribution

Anyone is welcome to suggest changes or help out with issues if there are any on the (github page)[https://github.com/landon-codes/VideoPackager].

This project uses the MIT License, so anyone is able to derive work of any kind from this project.