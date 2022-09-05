# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
import tkinter
from tkinter import *
from tkinter import ttk


# need to explain class
class StudyPlannerapp(ttk.Tk):
    def __init__(self, *args, **kwargs):
        ttk.Ttk.__init__(self, *args, **kwargs)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = ttk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for Page in (Main, GoalPage, ToDoPage):
            window = Main(container, self)
            self.window[Main] = window
            window.grid(row=0, column=0, sticky="nsew")

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            window.grid(row=0, column=0, sticky="nsew")
            self.show_frame(Main)

    def show_frame(self, cont):
        # Show window for the given page name
        window = self.frames[cont]
        window.ttkraise()


class Main(ttk.frame):
    def __init__(self, master, controller):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.master.geometry('350x500')
        self.master.title("Main Page")

        label = ttk.Label(self, text="My Study Planner", font=('MS Sans Serif', 10, 'bold'))
        label.pack(pady=10, padx=10)

        # Buttons
        btn_goals = ttk.Button(self, text="Goals", padx=5, pady=5, command=lambda: controller.show_frame(GoalPage))
        btn_goals.pack()

        btn_calendar = ttk.Button(self, text="Calendar", padx=5, pady=5,
                                  command=lambda: controller.show_frame(ToDoPage))
        btn_calendar.pack()

        # self.btnExit = Button(goalWindow(self.newWindow), text="Exit", bg="lightblue")
        # self.btnExit.place(x=10, y=470)x


class GoalPage(ttk.frame):
    def __init__(self, master, controller):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Your Goals")
        self.master.geometry('350x500')
        label = ttk.Label(self, text="My Study Planner", font=('MS Sans Serif', 10, 'bold'))
        label.pack(pady=10, padx=10)

        btn_exit = ttk.Button(self, text="Back to Main Page", padx=5, pady=5,
                              command=lambda: controller.show_frame(Main))
        btn_exit.place(x=10, y=460)


class ToDoPage(ttk.frame):
    def __init__(self, master):
        self.master = master
        self.master.title("To Do List")
        self.master.geometry('350x500')


if __name__ == "__main__":
    app = StudyPlannerapp()
    app.mainloop()

