""" gcal.py - Graphical calendar

Synopsis:
    gcal.py

Description:
    A simple calendar.

Notes:
    Starts with the current year.
    PageUp/Down - go to previous/next year.
    Home - go to current year.
"""

import tkinter
import sys
import datetime
import calendar

class Window(tkinter.Tk):
    def __init__(self, master=None):
        tkinter.Tk.__init__(self, master)
        self.bind('<Escape>', self.escape)

    def escape(self, event):
        self.withdraw()
        sys.exit()


class Calendar(Window):
    def __init__(self, master=None):
        Window.__init__(self, master)
        self.bind('<Prior>', self.pageup)
        self.bind('<Next>',  self.pagedown)
        self.bind('<Home>',  self.home)

        self._year = datetime.datetime.now().year

        self._text = tkinter.StringVar()
        self._text.set('')
        self.update()

        self._label = tkinter.Label(
            self,
            justify=tkinter.LEFT, # Override default, which is CENTER.
            padx=20,
            pady=0,
            font=('Consolas', 14, 'bold'),
            fg='green',
            bg='black',
            textvariable=self._text)
        self._label.pack()

    def update(self):
        cal = calendar.TextCalendar(calendar.SUNDAY)
        self._text.set(cal.formatyear(self._year))

    def pageup(self, event):
        self._year -= 1
        self.update()

    def pagedown(self, event):
        self._year += 1
        self.update()

    def home(self, event):
        self._year += 1
        self.update()


def main():
    gcalendar = Calendar()
    gcalendar.mainloop()


if __name__ == '__main__':
    main()

        
