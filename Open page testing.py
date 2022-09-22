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
        self.minsize(350, 500)
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

            # put all of the pages in the same location;
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
        label = tk.Label(self, text="Main Page", font=('MS Sans Serif', 10, 'bold'))
        label.pack(padx=10, pady=10)

        # Buttons
        btn_goals = tk.Button(self, text="Goals", padx=5, pady=5, command=lambda: controller.show_frame(GoalPage))
        btn_goals.pack()

        btn_to_do = tk.Button(self, text="To Do List",
                              command=lambda: controller.show_frame(ToDoPage))
        btn_to_do.pack()


class GoalPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, height=500, width=350)
        label = tk.Label(self, text="Your Goals", font=('MS Sans Serif', 10, 'bold'))
        label.pack(pady=10, padx=10)
        btn_exit = tk.Button(self, text="Back to Main Page",
                             command=lambda: controller.show_frame(Main))
        btn_exit.place(x=10, y=460)
        self.goal_list = ['Enter you goals here']

            # widgets for goal list
        self.my_entry = tk.Entry(self)

        self.short_term_listbox = tk.Listbox(self, width=20, height=10, activestyle='none', bg='light blue', selectbackground='powder blue')
        self.long_term_listbox = tk.Listbox(self, width=20, height=10, activestyle='none', bg='purple1', selectbackground='powder blue')

        btn_add = tk.Button(self, text='Add Goal', command=self.add_goal)
        btn_del = tk.Button(self, text='Delete', command=self.delete_goal)
        btn_del_all = tk.Button(self, text='Delete All Goals', command=self.delete_all_goals)

        # setting position of the widgets in app
        btn_add.place(x=50, y=350)
        btn_del.place(x=150, y=350)
        btn_del_all.place(x=225, y=350)
        self.short_term_listbox.place(x=200, y=130)
        self.long_term_listbox.place(x=50, y=130)
        self.my_entry.pack(pady=20)

    # Functions for button

    # Add tasks to to-do list
    def add_goal(self):
        task = self.my_entry.get()
        if 5 > len(self.my_entry.get()) > 0:
            self.goal_listbox.insert(END, task)
            self.my_entry.delete(0, 'end')
        elif len(self.my_entry.get()) > 5:
            messagebox.showinfo('Invalid length', 'Please consider shortening the length of your goal')
        else:
            if len(self.my_entry.get()) == 0:
                messagebox.showinfo('No input entered', 'Please enter a goal')

    # Delete task from to-do list
    def delete_goal(self):
        self.goal_listbox.delete(ANCHOR)

    def delete_all_goals(self):
        message_box = messagebox.askyesno('Delete All', 'Are you sure?')
        if message_box:
            self.goal_listbox.delete(0, 'end')



class ToDoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="To Do List", font=('MS Sans Serif', 10, 'bold'))
        label.pack(pady=10, padx=10)

        btn_exit = tk.Button(self, text="Back to Main Page",
                             command=lambda: controller.show_frame(Main))
        btn_exit.place(x=10, y=460)

        # widgets for to do list
        task_label = tk.Label(self, text='Enter the Task')
        task_label.place(x=0, y=0)

        task_field = tk.Entry(self, width=18)
        task_field.place(x=30, y=30)

        btn_add = tk.Button(self, text='Add Task', command=self.add_task)
        btn_del = tk.Button(self, text='Delete', command=self.delete_task)
        btn_del_all = tk.Button(self, text='Delete All Tasks', command=self.delete_all_tasks)

        self.tasks = []

        task_listbox = tk.Listbox(self, width=26, height=13)

        # setting position of the widgets in app using place() method
        btn_add.place(x=30, y=120)
        btn_del.place(x=30, y=160)
        btn_del_all.place(x=30, y=200)
        task_listbox.place(x=30, y=240)

    # Functions for buttons
    # Add tasks to to-do list
    def add_task(self, the_cursor=None):
        task_string = self.task_field.get()
        if len(task_string) == 0:
            messagebox.showinfo('Error', 'Please enter a task')
        else:
            self.tasks.append(task_string)
            the_cursor.execute('insert into tasks values (?)', (task_string,))
            self.update_list()
            self.task_field.delete(0, 'end')

    # Update task list
    def update_list(self):
        self.clear_list()
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    # Delete task from to-do list
    def delete_task(self, the_cursor=None):
        try:
            the_value = self.task_listbox.get(self.task_listbox.curselection())
            if the_value in self.tasks:
                self.tasks.remove(the_value)
                self.update_list()
                the_cursor.execute('delete from tasks where title = ?', (the_value,))
        except:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete')

    def delete_all_tasks(self, the_cursor=None):
        message_box = messagebox.askyesno('Delete All', 'Are you sure?')
        if message_box:
            while len(self.tasks) != 0:
                self.tasks.pop()
            the_cursor.execute('delete from tasks')
            self.update_list()

    def clear_list(self):
        self.task_listbox.delete(0, 'end')

    def retrieve_database(self, the_cursor=None):
        while len(self.tasks) != 0:
            self.tasks.pop()
        for row in the_cursor.execute('select title from tasks'):
            self.tasks.append(row[0])


if __name__ == "__main__":
    app = StudyApp()
    app.mainloop()

