# VideoPackager

A Python application to compress videos using FFmpeg.

## Depreciation notice
This project is no longer being maintained due to a lack of a defined goal. You are welcome to fork the repository yourself to continue it.

This project may become unarchived if a better, more specific goal for this project is decided by the original developer.

## Installation

There are two ways you can download the application. 

The first method is to download the source code from the [GitHub repository](https://github.com/landon-codes/VideoPackager).

If you are using Windows, you can install a compiled binary from the release page on the GitHub repository.

## Usage

You will need to open a terminal and change into the directory where you have the project source downloaded.
Once you have moved into the proper directory (which should look something like `C:\~~\VideoPackager` for Windows or `~~/VideoPackager` for Unix systems), you can run the project using `python main.py`. The application will prompt you to enter the video file that you are wanting to compress, where you want to store the compressed version (the output file), and if applicable, a preset.

Or you could bundle everything into one single command:
```bash
python main.py inVideo.mp4 outVideo.mp4 -preset fast
```

Some example values for preset are:
* slow
* fast
* ultrafast

The default value is slow.

*The slower the setting, the smaller the output size will be.*

## License/Contribution

Anyone is welcome to suggest changes or help out with issues if there are any on the [github page](https://github.com/landon-codes/VideoPackager).

This project uses the MIT license.
