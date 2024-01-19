import os
import cv2
import time

from .constants import TXT_FILE, JPG_FILE
from .ascii_write import convert_frame_to_ascii
from .ascii_read import read_ascii_from_file
from .utils import clear_console, print_progress, convertion_finished, delete_existing_file

# main function for converting videos to ASCII and displaying them
def video_to_ascii(videoFile):
    clear_console()

    # get the start time
    start_time = time.time()

    # check if video file exists
    if not os.path.isfile(videoFile):
        print(f"Error: Video file: '{videoFile}' does not exist")
        return
    
    # check if the file is a video file
    video_extensions = ['.avi', '.mp4', '.m4v', '.mkv', '.flv', '.mov', '.wmv']
    if not any(videoFile.endswith(ext) for ext in video_extensions):
        print(f"Error: File: '{videoFile}' is not a recognized video file")
        return

    # create empty file for ascii
    file = open(TXT_FILE, "w")
    file.close()

    # convert video to ascii art
    cap = cv2.VideoCapture(videoFile)
    fps = cap.get(cv2.CAP_PROP_FPS)
    terminal_size = os.get_terminal_size()
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    count = 0
    success, image = cap.read()
    while success:
        cv2.imwrite(JPG_FILE, image)

        convert_frame_to_ascii(JPG_FILE, terminal_size.columns, terminal_size.lines)
        count += 1
        print_progress(count, total_frames)

        success, image = cap.read()
    delete_existing_file(JPG_FILE)
    
    # watch converted video
    convertion_finished(start_time)
    while True:
        read_ascii_from_file(terminal_size.lines-1, fps)
        x = input("Do you want to watch the video again? (Y/N)")

        if x.lower() != 'y':
            break

    # clean up
    delete_existing_file(TXT_FILE)
    clear_console()