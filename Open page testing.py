# importing required modules
import tkinter as tk
from tkinter import *
from tkinter import messagebox


# need to explain class
class StudyApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        width = 350
        height = 500

        self.geometry(f'{width}x{height}')
        self.minsize(width, height)
        self.title('My Study Planner')

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self, width=350, height=500)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_propagate(0)

        self.frames = {}

        for F in (Main, GoalPage, ToDoPage):
            frame = F(container, self)
            self.frames[F] = frame

            # put all the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Main)

    def show_frame(self, cont):
        # Show window for the given page name
        frame = self.frames[cont]
        frame.tkraise()


class Main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        label = tk.Label(self, text="Main Page", font=('MS Sans Serif', 12, 'bold'))
        label.pack(padx=10, pady=10)

        welcome_msg = "Welcome to My Study Planner \n To create your short/long term goal lists, click Goals \n " \
                      "To create your school and extracurricular to do lists, click To Do List"
        welcome_label = tk.Label(self, text=welcome_msg, font=('MS Sans Serif', 8))
        welcome_label.pack(padx=10, pady=10)

        # Buttons
        btn_goals = tk.Button(self, text="Goals", padx=5, pady=5, command=lambda: controller.show_frame(GoalPage))
        btn_goals.pack(padx=5, pady=5)

        btn_to_do = tk.Button(self, text="To Do List",
                              command=lambda: controller.show_frame(ToDoPage))
        btn_to_do.pack(padx=5, pady=5)


class GoalPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.confirm = None
        self.choice = None

        # Goal page labels
        label = tk.Label(self, text="Your Goals", font=('MS Sans Serif', 12, 'bold'))
        short_term_label = tk.Label(self, text="Short Term Goals", font=('MS Sans Serif', 10, 'bold'))
        long_term_label = tk.Label(self, text="Long Term Goals", font=('MS Sans Serif', 10, 'bold'))
        entry_label = tk.Label(self, text="Enter goal:", font=('MS Sans Serif', 10))

        label.pack(pady=10, padx=10)
        short_term_label.place(x=50, y=100)
        long_term_label.place(x=200, y=100)
        entry_label.place(x=50, y=65)

        # widgets for goal list
        self.my_entry = tk.Entry(self)

        self.short_term_listbox = tk.Listbox(self, width=20, height=10, activestyle='none', bg='light blue',
                                             selectbackground='powder blue')
        self.long_term_listbox = tk.Listbox(self, width=20, height=10, activestyle='none', bg='light blue',
                                            selectbackground='powder blue')

        btn_add = tk.Button(self, text='Add Goal', command=self.goal_choice)
        btn_del = tk.Button(self, text='Delete \n Goal', command=self.delete_goal)
        btn_del_all = tk.Button(self, text='Delete All \n Short Term Goals', command=self.delete_all_goals)
        btn_exit = tk.Button(self, text="Back to Main Page",
                             command=lambda: controller.show_frame(Main))

        # setting position of the widgets in app
        btn_add.place(x=50, y=350)
        btn_del.place(x=150, y=350)
        btn_del_all.place(x=225, y=350)
        btn_exit.place(x=10, y=460)
        self.long_term_listbox.place(x=200, y=130)
        self.short_term_listbox.place(x=50, y=130)
        self.my_entry.place(x=125, y=65)

    # Functions
    def confirmation(self):
        goal = self.my_entry.get()
        message_box = messagebox.askyesno('Confirm addition of goal',
                                          f'Are you sure you would like to add "{goal}" to your goal list')
        if message_box:
            return True
        else:
            return False

    # Add goals to short-term or long-term list box depending on user action and input

    def goal_choice(self):
        goal = self.my_entry.get()

        if 5 >= len(goal) > 0:
            self.choice = Toplevel(self)
            choice_label = tk.Label(self.choice, text='Please choose the \n type of goal',
                                    font=('MS Sans Serif', 8, 'bold'))
            choice_label.pack(side=TOP)
            self.choice.geometry('200x150')
            btn_short = tk.Radiobutton(self.choice, text='Short Term', command=self.add_short_goal)
            btn_short.place(x=50, y=50)
            btn_long = tk.Radiobutton(self.choice, text='Long Term', command=self.add_long_goal)
            btn_long.place(x=50, y=100)
        elif len(goal) > 5:
            messagebox.showinfo('Too long', 'Please consider shortening the length of your goal')
        else:
            if len(goal) == 0:
                messagebox.showwarning('No input entered', 'Please enter a goal')

    def add_long_goal(self):
        if self.confirmation():
            goal = self.my_entry.get()
            self.long_term_listbox.insert(END, goal)
            self.my_entry.delete(0, 'end')
            self.choice.destroy()
        else:
            pass

    def add_short_goal(self):
        if self.confirmation():
            goal = self.my_entry.get()
            self.short_term_listbox.insert('end', goal)
            self.my_entry.delete(0, 'end')
            self.choice.destroy()
        else:
            pass

    def delete_goal(self):
        self.short_term_listbox.delete(ANCHOR)
        self.long_term_listbox.delete(ANCHOR)

    # Delete all goals from short term goal listbox once user has confirmed deletion
    def delete_all_goals(self):
        size = self.short_term_listbox.size()
        if size != 0:
            message_box = messagebox.askyesno('Delete Short Term Goals', 'Are you sure?')
            if message_box:
                self.short_term_listbox.delete(0, 'end')


class ToDoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.choice = None
        self.type = None

        # To Do Page Labels
        title_label = tk.Label(self, text="To Do List", font=('MS Sans Serif', 12, 'bold'))
        academic_label = tk.Label(self, text="Academic \n To Do List", font=('MS Sans Serif', 10, 'bold'))
        extra_label = tk.Label(self, text="Extracurricular \n To Do List", font=('MS Sans Serif', 10, 'bold'))
        entry_label = tk.Label(self, text="Enter Task:", font=('MS Sans Serif', 10))

        # Setting positions for labels in to do frame
        title_label.pack(pady=10, padx=10)
        academic_label.place(x=70, y=100)
        extra_label.place(x=200, y=100)
        entry_label.place(x=40, y=65)

        # widgets for to do list
        btn_exit = tk.Button(self, text="Back to Main Page",
                             command=lambda: controller.show_frame(Main))
        self.my_entry = tk.Entry(self)
        self.academic_listbox = tk.Listbox(self, width=20, height=10, activestyle='none', bg='light blue',
                                           selectbackground='powder blue')
        self.extra_listbox = tk.Listbox(self, width=20, height=10, activestyle='none', bg='light blue',
                                        selectbackground='powder blue')

        btn_add = tk.Button(self, text='Add Task', command=self.task_type)
        btn_del = tk.Button(self, text='Delete \n Task', command=self.delete_task)
        btn_del_all = tk.Button(self, text='Delete All \n Tasks', command=self.delete_choice)

        # setting position of the widgets in to do frame
        btn_add.place(x=50, y=350)
        btn_del.place(x=150, y=350)
        btn_del_all.place(x=225, y=350)
        btn_exit.place(x=10, y=460)

        self.academic_listbox.place(x=50, y=140)
        self.extra_listbox.place(x=200, y=140)
        self.my_entry.place(x=125, y=65, width=150, height=25)

    # Functions
    def confirmation(self):
        task = self.my_entry.get()
        message_box = messagebox.askyesno('Confirm addition of task',
                                          f'Are you sure you would like to add "{task}" to your task list')
        if message_box:
            return True
        else:
            return False

    def task_type(self):
        task = self.my_entry.get()
        if 5 >= len(task) > 0:
            self.type = Toplevel(self)
            type_label = tk.Label(self.type, text='Please choose the \n type of task',
                                  font=('MS Sans Serif', 8, 'bold'))
            type_label.pack(side=TOP)
            self.type.geometry('200x150')

            btn_academic = tk.Radiobutton(self.type, text='Academic task',
                                          command=self.add_academic_task)
            btn_academic.place(x=50, y=50)
            btn_extra = tk.Radiobutton(self.type, text='Extracurricular task',
                                       command=self.add_extra_task)
            btn_extra.place(x=50, y=100)
        elif len(task) > 5:
            messagebox.showinfo('Too long', 'Please consider shortening the length of your task')
        else:
            if len(task) == 0:
                messagebox.showwarning('No input entered', 'Please enter a task')

    # Add tasks to to-do list depending on user-input
    def add_academic_task(self):
        if self.confirmation():
            task = self.my_entry.get()
            self.academic_listbox.insert(END, task)
            self.my_entry.delete(0, 'end')
            self.type.destroy()
        else:
            pass

    def add_extra_task(self):
        if self.confirmation():
            task = self.my_entry.get()
            self.extra_listbox.insert(END, task)
            self.my_entry.delete(0, 'end')
            self.type.destroy()
        else:
            pass

    def delete_task(self):
        self.add_extra_task().delete(ANCHOR)
        self.add_academic_task().delete(ANCHOR)

    # Delete all tasks in task listbox once user has confirmed
    def delete_choice(self):
        self.choice = Toplevel(self)
        self.choice.geometry('200x150')

        choice_label = tk.Label(self.choice,
                                text='Would you like to delete all \n academic tasks or extracurricular tasks?',
                                font=('MS Sans Serif', 9))
        btn_del_academic = tk.Radiobutton(self.choice, text='Academic Tasks',
                                          state='normal',
                                          command=self.delete_academic_tasks)
        btn_del_extra = tk.Radiobutton(self.choice, text='Extracurricular tasks',
                                       state='active',
                                       command=self.delete_extra_tasks)

        choice_label.pack(side=TOP)
        btn_del_academic.place(x=50, y=50)
        btn_del_extra.place(x=50, y=100)

    def delete_academic_tasks(self):
        size = self.academic_listbox.size()
        if size > 0:
            message_box = messagebox.askyesno('Delete All Academic Tasks', 'Are you sure?')
            if message_box:
                self.academic_listbox.delete(0, 'end')
                self.choice.destroy()
        else:
            self.choice.destroy()
            messagebox.showwarning('Error', 'No Tasks to Delete')

    def delete_extra_tasks(self):
        size = self.extra_listbox.size()
        if size > 0:
            message_box = messagebox.askyesno('Delete All Extracurricular Tasks', 'Are you sure?')
            if message_box:
                self.extra_listbox.delete(0, 'end')
                self.choice.destroy()
        else:
            self.choice.destroy()
            messagebox.showwarning('Error', 'No Tasks to Delete')


if __name__ == "__main__":
    app = StudyApp()
    app.mainloop()

