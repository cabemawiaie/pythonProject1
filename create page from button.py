# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    app = Menu(root)

class Menu:
    def __init__(self, master):
        self.master =master
        self.master.title("My Study Planner")
        self.geometry('350x500')
        self.master.config(bg='light yellow')
        self.frame = Frame(self.master, height=150, width=100, bg='light yellow')
        self.frame.pack()

        self.intro = Label(main_frame, text="Welcome to My Study Planner")
        self.intro.pack(side=TOP, padx=5, pady=5)
        
        self.btnGoals = Button(self.frame, text="Goals", bg="lightblue", padx=5, pady=5, command=self.new_window)
        self.btnGoals.pack()
	
        self.btnCalendar = Button(self.frame, text="Calendar", bg="lightblue", padx=5, pady=5, command=self.new_window)
        self.btnCalendar.pack()
	
        self.btnDeadline = Button(self.frame, text="Deadlines", bg="lightblue", padx=5, pady=5, command=self.new_window)
        self.btnDeadline.pack()
	
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = goals_window(self.newWindow)


class Goals:
    def __init__(self, master):
        self.master =master
        self.master.title("Goals Page")
        self.geometry('350x500')
        self.master.config(bg='light yellow')
        self.frame = Frame(self.master, height=150, width=100, bg='light yellow')
        self.frame.pack()








