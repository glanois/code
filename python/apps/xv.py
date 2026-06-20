r""" 
usage: xv.py [-h] filename

A simple image viewer and a tribute to the original xv image display editing program for the X Window System.

positional arguments:
  filename    Image file to display.

options:
  -h, --help  show this help message and exit

"""

import argparse
import sys
import tkinter
import PIL.Image
import PIL.ImageTk


class Window(tkinter.Tk):
    def __init__(self, master=None):
        tkinter.Tk.__init__(self, master)
        self.bind('<Escape>', self.escape)

    def escape(self, event):
        self.withdraw()
        sys.exit()


class ImageDisplay(Window):
    def __init__(self, filename, master=None):
        Window.__init__(self, master)
        self.title('xv')
        self.configure(background='grey')
        try:
            image = PIL.Image.open(filename)
        except:
            print('ERROR: IOError - Could not open %s' % (filename))
        else:
            width, height = image.size
            scale = 1.0
            if width > 1024:
                scale = 1024 / float(width)

            scaled_width  = int((scale * float(width)))
            scaled_height = int((scale * float(height)))

            # Used to use PIL.Image.ANTIALIAS.  But that was dropped in
            # Pillow 10.0.0.  It was an alias to LANCZOS anyway.
            try:
                RESAMPLE_LANCZOS = PIL.Image.Resampling.LANCZOS
            except AttributeError:
                # Pillow < 9.1 or so
                RESAMPLE_LANCZOS = PIL.Image.LANCZOS
                # or PIL.Image.ANTIALIAS if you really need to support ancient versions

            image = image.resize((scaled_width, scaled_height), RESAMPLE_LANCZOS)

            # Keep a reference to the PhotoImage instance.
            # (Otherwise the label's image would disappear
            #  when the PhotoImage assigned to it goes out
            #  of scope.)
            self._photo_image = PIL.ImageTk.PhotoImage(image)

            label = tkinter.Label(self, image=self._photo_image)
            label.pack(side='bottom', fill='both', expand='yes')


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
