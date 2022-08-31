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

     #==================================Buttons=======================================================================
        self.btnGoals = Button(self.frame, text="Goals", bg="lightblue", padx=5, pady=5, command=self.goal_page)
        self.btnGoals.pack()

        self.btnCalendar = Button(self.frame, text="Calendar", bg="lightblue", padx=5, pady=5, command=self.calendar_page)
        self.btnCalendar.pack()

        self.btnDeadline = Button(self.frame, text="Deadlines", bg="lightblue", padx=5, pady=5, command=self.deadline_page)
        self.btnDeadline.pack()


        self.btnExit = Button(self.master, text="Exit", bg="lightblue", padx=5, pady=5, command=self.Exit)
        self.btnExit.place(x=10, y=460)

        #self.btnExit = Button(goalWindow(self.newWindow), text="Exit", bg="lightblue")
        #self.btnExit.place(x=10, y=470)x


#==================================Buttons=======================================================================

#==================================Button Functions==============================================================
    def goal_page(self):
        self.newWindow = Toplevel(self.master)
        self.app = goalWindow(self.newWindow)

    def calendar_page(self):
        self.newWindow = Toplevel(self.master)
        self.app = calendarWindow(self.newWindow)

    def deadline_page(self):
        self.newWindow = Toplevel(self.master)
        self.app = deadlineWindow(self.newWindow)

    def Exit(self):
        self.Exit = tkinter.messagebox.askyesno("Exit confirmation", "Confirm if you want to exit")
        if self.Exit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return
#==================================Button Functions==============================================================

class goalWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Your Goals")
        self.master.geometry('350x500')
        self.master.config(bg='light yellow')
        self.frame = Frame(self.master, bg='light yellow')
        self.frame.pack()

class calendarWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar")
        self.master.geometry('350x500')
        self.master.config(bg='light yellow')
        self.frame = Frame(self.master, bg='light yellow')
        self.frame.pack()

class deadlineWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Deadlines")
        self.master.geometry('350x500')
        self.master.config(bg='light yellow')
        self.frame = Frame(self.master, bg='light yellow')
        self.frame.pack()

main()
