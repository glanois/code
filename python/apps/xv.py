""" xv.py - Display an image.

Notes:
    sudo apt-get install python3-pip
    sudo pip3 install pillow
    sudo apt-get install python3-pil.imagetk
    http://www.trilon.com/xv/
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
            print('ERROR: IOError - Cound not open %s' % (filename))
        else:
            width, height = image.size
            scale = 1.0
            if width > 1024:
                scale = 1024 / float(width)

            scaled_width  = int((scale * float(width)))
            scaled_height = int((scale * float(height)))
            image = image.resize((scaled_width, scaled_height), PIL.Image.ANTIALIAS)

            # Keep a reference to the PhotoImage instance.
            # (Otherwise the label's image would disappear
            #  when the PhotoImage assigned to it goes out
            #  of scope.)
            self._photo_image = PIL.ImageTk.PhotoImage(image)

            label = tkinter.Label(self, image=self._photo_image)
            label.pack(side='bottom', fill='both', expand='yes')


def main(options):
    image_display = ImageDisplay(options.filename[0])
    image_display.mainloop()
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename',
        help='Display an image.',
        nargs=1)
    options = parser.parse_args()
    sys.exit(main(options))
