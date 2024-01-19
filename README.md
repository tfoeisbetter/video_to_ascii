# Video to ASCII CLI Command

A command-line tool to convert videos to ASCII art and display it in the terminal.
Supported video formats: AVI (.avi), MP4 (.mp4, .m4v), MOV (.mov), MKV (.mkv), FLV (.flv), and WMV (.wmv). 

## Installation

1. Clone the repository:

```shell
git clone https://github.com/ciameksw/video_to_ascii.git
```

2. Navigate to the project directory:

```shell
cd video_to_ascii
```

3. Install the required dependencies:

```shell
pip3 install -r requirements.txt
```

4. Install the video_to_ascii package:

```shell
pip3 install .
```

## Development

To install the package in editable mode for development:

```shell
pip3 install -e .
```

## Usage

To convert a video to ASCII art, run the following command:

```shell
videotoascii -f <FILENAME>
```

> :warning: **Don't resize the terminal after running the command**: Its dimensions are used to scale the video

## Project Structure

Here's an overview of the project's structure:

- `video_to_ascii/`: This directory contains the main Python package.
  - `__init__.py`: Required to make Python treat the directory as a package.
  - `__main__.py`: Contains the main functionality of the package.
  - `ascii_read.py`: Contains functions for reading ASCII art and displaying it.
  - `ascii_write.py`: Contains functions for converting video frames to ASCII and writing them to a file.
  - `constants.py`: Contains constants used across the package.
  - `utils.py`: Contains utility functions used across the package.
  - `video_to_ascii.py`: Contains the core logic for converting videos to ASCII.
- `README.md`: Contains documentation for the project.
- `requirements.txt`: Contains required dependencies.
- `setup.py`: Used by pip to install the package.

## License

This project is licensed under the terms of the MIT license.