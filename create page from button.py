# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    app = Menu(root)
    root.mainloop()


class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("My Study Planner")
        self.master.geometry('350x500')
        self.master.config(bg='yellow1')
        self.frame = Frame(self.master, bg='yellow1')
        self.frame.pack()

        self.intro = Label(self.frame, text="Welcome to My Study Planner", font=('MS Sans Serif', 10, 'bold'), bg='yellow1')
        self.intro.pack(side=TOP)

        self.btnGoals = Button(self.frame, text="Goals", bg="wheat1", padx=5, pady=5, command=self.new_window)
        self.btnGoals.pack()

        self.btnCalendar = Button(self.frame, text="Calendar", bg="wheat1", padx=5, pady=5, command=self.new_window)
        self.btnCalendar.pack()

        self.btnDeadline = Button(self.frame, text="Deadlines", bg="wheat1", padx=5, pady=5, command=self.new_window)
        self.btnDeadline.pack()

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = goalWindow(self.newWindow)


class goalWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Goals Page")
        self.master.geometry('350x500')
        self.master.config(bg='yellow1')
        self.frame = Frame(self.master, bg='yellow1')
        self.frame.pack()


main()









