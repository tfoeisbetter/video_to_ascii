from PIL import Image

from .constants import ASCII_STRING, MAX_BRIGHTNESS, TXT_FILE

# function to convert pixel to ASCII character by brightness
def pixel_to_ascii(px):
    (r, g, b) = px
    px_brightness = r+g+b
    index = int(len(ASCII_STRING)*px_brightness/MAX_BRIGHTNESS)-1
    if index < 0:
        index = 0
    return ASCII_STRING[index]

# function to saVe ASCII from list of lines to file
def save_ascii_to_file(ascii_list):
    file = open(TXT_FILE, "a")
    for line in ascii_list:
        file.write(line)
        file.write('\n')
    file.close()

# function to convert frame to ASCII list of lines
def convert_frame_to_ascii(fileName, windowWidth, windowHeight):
    image = Image.open(fileName)

    image = image.resize([windowWidth, windowHeight])
    (width, height) = image.size

    ascii = []
    for y in range(0, height - 1):
        line = ""
        for x in range(0, width - 1):
            px = image.getpixel((x, y))
            line += pixel_to_ascii(px)
        ascii.append(line)

    save_ascii_to_file(ascii)