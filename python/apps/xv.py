r""" 
usage: xv.py [-h] filename

DESCRIPTION
    A simple image viewer and a tribute to the original xv image display 
    editing program for the X Window System.

positional arguments:
  filename    Image file to display.

options:
  -h, --help  show this help message and exit

REQUIREMENTS
    One-time system setup:
        sudo apt update
        sudo apt install python3-tk python3-pil python3-pil.imagetk

    To use this application in a venv, you'll have to bring in
    these system packages when you create the venv:
        python3 -m venv --system-site-packages venv_name
        source venv_name/bin/activate
        pip install -r requirements.txt   # any other deps

NOTES
    http://www.trilon.com/xv/ (gives 404 as of 6/20/2026)
    https://itsfoss.community/t/resurrecting-xv-the-original-linux-image-viewer/12426
    https://github.com/nevillejackson/Unix/tree/main/xv
"""

import argparse
import os
import sys
import tkinter
from PIL import Image, ImageTk, UnidentifiedImageError


class Window(tkinter.Tk):
    def __init__(self, master=None):
        tkinter.Tk.__init__(self, master)
        self.bind('<Escape>', self.escape)
        self.bind('<q>', self.escape)           # classic quit
        self.bind('<f>', self.toggle_fullscreen)

    def escape(self, event=None):
        self.withdraw()
        sys.exit(0)

    def toggle_fullscreen(self, event=None):
        self.attributes('-fullscreen', not self.attributes('-fullscreen'))


class ImageDisplay(Window):
    def __init__(self, filename, master=None):
        Window.__init__(self, master)
        self.title(f'xv - {os.path.basename(filename)}')
        self.configure(background='grey')

        try:
            image = Image.open(filename)
        except (UnidentifiedImageError, FileNotFoundError, PermissionError) as e:
            print(f'ERROR: Could not open {filename}: {e}')
            sys.exit(1)
        except Exception as e:  # fallback for anything else
            print(f'ERROR: Unexpected error opening {filename}: {e}')
            sys.exit(1)

        width, height = image.size
        MAX_DIM = 1024

        if width > MAX_DIM or height > MAX_DIM:
            scale = MAX_DIM / float(max(width, height))
            scaled_width = int(width * scale)
            scaled_height = int(height * scale)

            # Compatibility shim for Pillow >= 10 (ANTIALIAS -> LANCZOS)
            try:
                resample = Image.Resampling.LANCZOS
            except AttributeError:
                resample = Image.LANCZOS  # older Pillow

            image = image.resize((scaled_width, scaled_height), resample)
        else:
            scaled_width, scaled_height = width, height

        # Keep a strong reference to the PhotoImage instance.
        # (Otherwise the label's image would disappear
        #  when the PhotoImage assigned to it goes out
        #  of scope.)
        self._photo_image = ImageTk.PhotoImage(image)

        label = tkinter.Label(self, image=self._photo_image, bg='grey')
        label.pack(side='bottom', fill='both', expand='yes')

        # Size the window to the (possibly scaled) image
        self.geometry(f"{scaled_width}x{scaled_height}")


def main(args):
    image_display = ImageDisplay(args.filename)
    image_display.mainloop()
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""DESCRIPTION
    A simple image viewer and a tribute to the original xv image display editing program for the X Window System.""",
        epilog="""REQUIREMENTS
    One-time system setup:
        sudo apt update
        sudo apt install python3-tk python3-pil python3-pil.imagetk

    To use this application in a venv, you'll have to bring in
    these system packages when you create the venv:
        python3 -m venv --system-site-packages venv_name
        source venv_name/bin/activate
        pip install -r requirements.txt   # any other deps

NOTES
    http://www.trilon.com/xv/ (gives 404 as of 6/20/2026)
    https://itsfoss.community/t/resurrecting-xv-the-original-linux-image-viewer/12426
    https://github.com/nevillejackson/Unix/tree/main/xv""",
    formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        'filename',
        help='Image file to display.')

    args = parser.parse_args()
    sys.exit(main(args))
