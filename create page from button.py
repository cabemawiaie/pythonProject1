# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
import tkinter
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
        self.master.config(bg='light blue')
        self.frame = Frame(self.master, bg='light blue')
        self.frame.pack()

        self.intro = Label(self.frame, text="Welcome to My Study Planner", font=('MS Sans Serif', 10, 'bold'),
                           bg='yellow1')
        self.intro.pack(side=TOP)

        # Buttons
        self.btnGoals = Button(self.frame, text="Goals", bg="white", padx=5, pady=5, command=self.goal_page)
        self.btnGoals.pack()

        self.btnCalendar = Button(self.frame, text="Calendar", bg="white", padx=5, pady=5, command=self.calendar_page)
        self.btnCalendar.pack()

        self.btnDeadline = Button(self.frame, text="Deadlines", bg="white", padx=5, pady=5, command=self.deadline_page)
        self.btnDeadline.pack()

        self.btnExit = Button(self.master, text="Exit", bg="white", padx=5, pady=5, command=self.exit)
        self.btnExit.place(x=10, y=460)

        # self.btnExit = Button(goalWindow(self.newWindow), text="Exit", bg="lightblue")
        # self.btnExit.place(x=10, y=470)x



    # Button FunctionS
    def goal_page(self):
        self.newWindow = Toplevel(self.master)
        self.app = GoalWindow(self.newWindow)

    def calendar_page(self):
        self.newWindow = Toplevel(self.master)
        self.app = CalendarWindow(self.newWindow)

    def deadline_page(self):
        self.newWindow = Toplevel(self.master)
        self.app = DeadlineWindow(self.newWindow)

    def exit(self):
        self.Exit = tkinter.messagebox.askyesno("Exit confirmation", "Confirm if you want to exit")
        if self.Exit > 0:
            self.master.destroy()
        else:
            command = self.new_window
        return


class GoalWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Your Goals")
        self.master.geometry('350x500')
        self.master.config(bg='light blue')
        self.frame = Frame(self.master, bg='light blue')
        self.frame.pack(pady=10)
        self.userGoals = Listbox(self.frame, width=25, height=5, highlightthicknes=0, selectbackground='#a6a6a6', activestyle="none")
        self.userGoals.pack(side=LEFT, fill=BOTH)
        self.goals_list = []
        for goal in self.goals_list:
            self.goals_list.insert(END, goal)
        self.myScrollbar = Scrollbar(self.frame)
        self.myScrollbar.config(command=self.goal.yview)
        self.myScrollbar.pack(side=RIGHT, fill=BOTH)
        self.goals_list.config(yscrollcommand=self.myScrollbar.set)
        self.myEntry = Entry(self.master)
        self.myEntry.pack(pady=20)
        self.btnFrame = Frame(self.master)
        self.btnFrame.pack(pady=20)
        # Goal Buttons
        self.btnDelete = Button(self.btn_frame, text="Delete goal", command=self.delete_goal)
        self.btnAdd = Button(self.btn_frame, text="Add goal", command=self.add_goal)
        self.btnCross = Button(self.btn_frame, text="Cross off goal", command=self.cross_goal)
        self.btnUncross = Button(self.btn_frame, text="Uncross goal", command=self.uncross_goal)
        self.btnDelete.pack()
        self.btnAdd.pack(padx=20)
        self.btnCross.pack()
        self.btnUncross.pack(padx=20)

     # Functions for goal buttons
    def delete_goal(self):

        self.goals_list.delete(ANCHOR)

    def add_goal(self):

        self.goals_list.insert(END, self.myEntry.get())
        self.myEntry.delete(0, END)

    def cross_goal(self):

        pass

    def uncross_goal(self):

        pass



class CalendarWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar")
        self.master.geometry('350x500')
        self.master.config(bg='light yellow')
        self.frame = Frame(self.master, bg='light yellow')
        self.frame.pack()


class DeadlineWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Deadlines")
        self.master.geometry('350x500')
        self.master.config(bg='light yellow')
        self.frame = Frame(self.master, bg='light yellow')
        self.frame.pack()


main()
