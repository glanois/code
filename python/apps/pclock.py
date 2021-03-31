""" pclock.py - Python clock

Synopsis:
    pclock.py

Description:
    A simple clock.

Notes:

https://www.daniweb.com/programming/software-development/code/216785/tkinter-digital-clock-python
https://www.daniweb.com/programming/software-development/threads/70076/disabling-the-title-bar
https://stackoverflow.com/questions/29641616/drag-window-when-using-overrideredirect
https://stackoverflow.com/questions/39529600/remove-titlebar-without-overrideredirect-using-tkinter
https://stackoverflow.com/questions/28467285/how-do-i-bind-the-escape-key-to-close-this-window
"""

import tkinter
import tkinter.font
import sys
import time

class FloatingBorderlessWindow(tkinter.Tk):
    def __init__(self, master=None):
        tkinter.Tk.__init__(self, master)

        ws = self.tk.call('tk', 'windowingsystem')
        if ws == 'x11':
            # Use this on Linux (or anything with X Window).
            self.wm_attributes('-type', 'splash')
        elif ws == 'aqua':
            # MacOS X
            # TODO - figure out how to hide the titlebar on Mac.
            # Tried:
            # self.wm_attributes('-type', 'splash')
            # self.wm_overrideredirect(True)
            # self.overrideredirect(True)
            # self.overrideredirect(1)
            # self.attributes('-toolwindow', 1)
        else:
            # Use this on Windows:
            self.overrideredirect(True)

        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-1>',  self.button1)
        self.bind('<B1-Motion>', self.b1motion)
        self.bind('<Escape>',    self.escape)

    def button1(self, event):
        self._offsetx = event.x
        self._offsety = event.y

    def b1motion(self, event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry(f'+{x}+{y}')

    def escape(self, event):
        self.withdraw()
        sys.exit()


class Clock(FloatingBorderlessWindow):
    def __init__(self, master=None):
        FloatingBorderlessWindow.__init__(self, master)

        # https://www.1001fonts.com/digital-readout-font.html
        # Ubuntu Linux - Download and unzip into ~/.fonts
        # Don't worry if you don't have this font, a default one will
        # be provided for you.
        the_font = tkinter.font.Font(
            family='SF Digital Readout',
            size=36,
            weight=tkinter.font.BOLD),
        self._clock = tkinter.Label(
            self,
            font=the_font,
            fg='green',
            bg='black')
        self._clock.pack(fill=tkinter.BOTH, expand=1)
        self.tick()

    def tick(self):
        # %-I is not supported on all platforms, so you have to remove
        # the leading '0' with lstrip().
        now = time.strftime('%I:%M%p').lstrip('0')

        # Update the time if it has changes since the last time we updated it.
        if now != self._clock['text']:
            self._clock['text'] = now

        # Set a timer to update the label every so often (1000ms = 1s).
        self._clock.after(1000, self.tick)


def main():
    clock = Clock()
    clock.mainloop()


if __name__ == '__main__':
    main()
