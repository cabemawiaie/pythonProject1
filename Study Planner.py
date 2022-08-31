# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#main function runs code
def main():
    root = Tk()
    app = Menu(root)
    root.mainloop()


class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("My Study Planner")
        self.master.geometry('350x500')
        self.master.config(bg='light yellow')
        self.frame = Frame(self.master, bg='light yellow')
        self.frame.pack()

        self.intro = Label(self.frame, text="Welcome to My Study Planner")
        self.intro.pack(side=TOP, padx=5, pady=5)

#==================================Buttons==============================================================================
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


#==================================Buttons==============================================================================

#==================================Button Functions=====================================================================
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
#==================================Button Functions=====================================================================

class goalWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Your Goals")
        self.master.geometry('350x500')
        self.master.config(bg='light yellow')
        self.frame = Frame(self.master, bg='light yellow')
        self.frame.pack(pady=10)
#==================================Goal List============================================================================
    goals_list = []
    counter = 1
    #Function for checking input error when no goal is entered in task field
    def inputError(self):
        if enterGoalField.get() == " ":
            messagebox.showerror("Please enter a goal")
            return 0
        return 1

    #Function for clearing the contents of task number text field
    def clear_goalNumberField(self):
        goalNumberField.delete(0.0, END)

    #Function for clearing the contents of task entry field
    def clear_goalField(self):
        enterGoalField.delete(0, END)

    #Function for adding the contents from the task entry field to the text area
    def addGoal(self):
        global counter
        value = inputError(self)
        if value ==  0:
            return
        content = enterGoalField.get() + "\n"
        goals_list.append(content)

        #insert content of task entry field to the text area
        TextArea.insert('end -1 chars', "[" + str(counter) + "] " + content)
        counter += 1

        clear_goalField()

    #function for deleting the specified goal
    def delete(self):
        global counter
        #handling the empty goal error
        if len(goals_list) == 0:
            messagebox.showerror("No goal entered")
            return
        #get the goal number which is required to delete
        number = goalNumberField.get(1.0, END)

        if number == "\n":
            messagebox.showerror("Input error")
            return
        else:
            goal_no = int(number)

        clear_goalNumberField()
        goals_list.pop(goal_no - 1)
        counter -=1
        TextArea.delete(1.0, END)
        #rewriting the task after deleting one goal at a time
        for i in range(len(goals_list)):
            TextArea.insert('end -1 chars', "[" + str(i+1)+ "]"+tasks_list[i])
#==================================Widgets for goal list================================================================
    enterGoal = Label(self.frame, text="Enter your Goal: ")
    enterTaskField = Entry(self.frame)
    Upload = Button(self.frame, text = "Upload", commant = addGoal)
    TextArea = Text(self.frame, height=3, width=5)
    goalNumber

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

