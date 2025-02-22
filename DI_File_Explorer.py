from tkinter import *


class File_Explorer(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("DI_File_Explorer")


if __name__ == "__main__":
    window = File_Explorer()
