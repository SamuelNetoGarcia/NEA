import tkinter as tk
from ViewBookings import ViewBookings
from BookClassroom import BookClassroom
from calenderscreen import CalendarScreen
class TitleScreen(tk.Frame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self.controller = controller





        title = tk.Label(self,text="Menu Screen",font=("consolas",20))
        title.pack(pady=20,padx=5
        )


#buttons for frame swapping
        ViewBookings_Button = tk.Button(self, text="View Bookings",command=lambda:
        controller.show_frame(ViewBookings))
        ViewBookings_Button.pack(pady=20,padx=5)


        Book_Button = tk.Button (self, text="Book a classroom",command=lambda:
        controller.show_frame(BookClassroom))
        Book_Button.pack(pady=20,padx=5)


        Calendar_Button = tk.Button(self, text="Calendar",command=lambda:
        controller.show_frame(CalendarScreen))
        Calendar_Button.pack(pady=20,padx=5)

