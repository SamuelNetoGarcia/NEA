import tkinter as tk
from TitleScreen import TitleScreen
from SignUp import SignUp
from BookClassroom import BookClassroom
from ViewBookings import ViewBookings
from calenderscreen import CalendarScreen
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("RoomBooker")
        self.geometry("1000x800")
#create a frame that allows me to just put in all the rest of the frames in easily
        container = tk.Frame(self)
        container.pack()
        self.frames = {}

#addign all the pages
        for frameclass1 in (TitleScreen, SignUp,BookClassroom, CalendarScreen,ViewBookings):
            #create all the classes
            frame = frameclass1(container,self)

            #store all the frames/pages in a dictionary (asking chatgpt how i should go about the process, it suggested i do this)

            self.frames[frameclass1] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        #start on signup screen
        self.show_frame(SignUp)







    #function to swap a frame
    def show_frame(self, frameclass2):
        frame = self.frames[frameclass2]
        frame.tkraise()























# Main program
root = MainApplication()
root.mainloop()