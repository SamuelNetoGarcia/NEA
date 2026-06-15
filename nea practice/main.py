import tkinter as tk
from menuscreen import menuscreen


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("tile")
        self.geometry("1000x1000")

        self.thestart()

    def thestart(self):

        self.frame = menuscreen(self)

        self.frame.pack()

# Main program
root = MainApplication()
root.mainloop()