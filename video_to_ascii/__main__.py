import argparse

from .video_to_ascii import video_to_ascii
from .utils import clear_console, delete_existing_file
from .constants import TXT_FILE, JPG_FILE

def main():
    parser = argparse.ArgumentParser(description="Convert video to ASCII art")
    parser.add_argument("-f", "--video_file", help="Path to the video file", required=True)

    args = parser.parse_args()
    try:
        video_to_ascii(args.video_file)
    except KeyboardInterrupt:
        clear_console()
        delete_existing_file(TXT_FILE)
        delete_existing_file(JPG_FILE)
        print("Cleaned up and exited")


if __name__ == '__main__':
    main()
