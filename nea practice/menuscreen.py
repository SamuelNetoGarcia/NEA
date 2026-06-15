import tkinter as tk


class menuscreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.parent.geometry("1000x1000")
        self.parent.title("start screen")

        # Grid fing
        for i in range(3):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)

        # Title fing
        self.label = tk.Label(
            self,
            text="scheduling system\n"
                 "This is the title screen\n"
                 "Press button to sign up",
            font=("Consolas", 20, "bold")
        )
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # frame for more options later idk
        self.frame1 = tk.Frame(self, relief="groove", borderwidth=3)
        self.frame1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


        # Button frame fingy
        self.frame2 = tk.Frame(self, relief="groove", borderwidth=3)
        self.frame2.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.start_btn = tk.Button(
            self.frame2,
            text="sign up",
            command= signup
        )
        self.start_btn.pack(expand=True)
        def signup ():
            if
