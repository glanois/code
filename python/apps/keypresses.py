""" Report keypresses sent to the window. """

import tkinter

class MyWindow(tkinter.Tk):
    def __init__(self, master=None):
        tkinter.Tk.__init__(self, master)

        self.bind_all('<Key>',  self.key)
        prompt = '         Press any key         '
        self._label = tkinter.Label(
            self,
            text=prompt,
            width=len(prompt),
            bg='yellow')
        self._label.pack()

    def key(self, event):
        if event.char == event.keysym:
            msg = 'Normal Key %r' % event.char
        elif len(event.char) == 1:
            msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
        else:
            msg = 'Special Key %r' % event.keysym
        self._label.config(text=msg)

def main():
    w = MyWindow()
    w.mainloop()

if __name__ == '__main__':
    main()
