import tkinter as tk
from tkinter import messagebox
from  TitleScreen import TitleScreen

class SignUp(tk.Frame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self.controller = controller





        title = tk.Label(self,text="sign up here\\the password must have at least 8 characters",font=("consolas",20))
        title.pack(pady=20,padx=5
        )
#spot to putin username/password, and validation
        username = tk.Entry(self)
        username.pack(pady=20,padx=5)
        password = tk.Entry(self,show = "*")
        password.pack(pady=20,padx=5)



        def login():
            user=username.get()
            pw=password.get()
            if len(pw) <8:
                messagebox.showerror("Error","Password must be at least 8 characters")

            else:
                controller.show_frame(TitleScreen)




#signup button
        signup = tk.Button(self, text="sign up",command=login)
        signup.pack(pady=20,padx=5)
