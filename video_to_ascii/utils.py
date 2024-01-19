import math
import os
import time

# function to clear the console on both windows and linux
def clear_console(): os.system('clear' if os.name == 'posix' else 'cls')

# function to print the progress of the convertion
def print_progress(count, total_frames):
    clear_console()
    percent = round(count*100/total_frames)
    print("Don't resize the terminal while converting and watching the video")
    print(F"Converting: {progress_bar(percent)} {percent}%")
    print(f"Frames: {count}/{total_frames}")

# function to create the progress bar
def progress_bar(percent):
    num_of_blocks = math.floor(percent/5)
    bar = "[" + "#"*num_of_blocks + "-"*(20-num_of_blocks) + "]"
    return bar

# function to handle the convertion finished
def convertion_finished(start_time):
    clear_console()
    print("Done, convertion time:",round(time.time() - start_time,2),"seconds")
    input("Press any key to watch the video")

# function that deletes the file if it exists
def delete_existing_file(file):
    if os.path.isfile(file):
        os.remove(file)