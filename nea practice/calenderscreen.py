import tkinter as tk


class CalendarScreen(tk.Frame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self.controller = controller





        title = tk.Label(self,text="view all classes",font=("consolas",20))
        title.pack(pady=20,padx=5
        )
