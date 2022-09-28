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
        label = tk.Label(self, text="Your Goals", font=('MS Sans Serif', 12, 'bold'))
        label.pack(pady=10, padx=10)
        short_term_label = tk.Label(self, text="Short Term Goals", font=('MS Sans Serif', 10, 'bold'))
        short_term_label.place(x=50, y=100)
        long_term_label = tk.Label(self, text="Long Term Goals", font=('MS Sans Serif', 10, 'bold'))
        long_term_label.place(x=200, y=100)
        entry_label = tk.Label(self, text="Enter goal:", font=('MS Sans Serif', 10))
        entry_label.place(x=50, y=65)

        btn_exit = tk.Button(self, text="Back to Main Page",
                             command=lambda: controller.show_frame(Main))
        btn_exit.place(x=10, y=460)

        # widgets for goal list
        self.my_entry = tk.Entry(self)

        self.short_term_listbox = tk.Listbox(self, width=20, height=10, activestyle='none', bg='light blue',
                                             selectbackground='powder blue')
        self.long_term_listbox = tk.Listbox(self, width=20, height=10, activestyle='none', bg='light blue',
                                            selectbackground='powder blue')

        btn_add = tk.Button(self, text='Add Goal', command=self.goal_choice)
        btn_del = tk.Button(self, text='Delete \n Goal', command=self.delete_goal)
        btn_del_all = tk.Button(self, text='Delete All \n Short Term Goals', command=self.delete_all_goals)

        # setting position of the widgets in app
        btn_add.place(x=50, y=350)
        btn_del.place(x=150, y=350)
        btn_del_all.place(x=225, y=350)
        self.long_term_listbox.place(x=200, y=130)
        self.short_term_listbox.place(x=50, y=130)
        self.my_entry.place(x=125, y=65)

    # Functions

    # Add goals to short-term or long-term list box depending on user action and input
    def goal_choice(self):
        task = self.my_entry.get()
        if 5 >= len(task) > 0:
            self.choice = Toplevel(self)
            choice_label = tk.Label(self.choice, text='Please choose the \n type of goal',
                                    font=('MS Sans Serif', 8, 'bold'))
            choice_label.pack(side=TOP)
            self.choice.geometry('200x150')
            btn_short = tk.Radiobutton(self.choice, text='Short Term', command=self.add_short_goal)
            btn_short.place(x=50, y=50)
            btn_long = tk.Radiobutton(self.choice, text='Long Term', command=self.add_long_goal)
            btn_long.place(x=50, y=100)
        elif len(task) > 5:
            messagebox.showinfo('Too long', 'Please consider shortening the length of your goal')
        else:
            if len(task) == 0:
                messagebox.showwarning('No input entered', 'Please enter a goal')

    def add_long_goal(self):
        task = self.my_entry.get()
        self.long_term_listbox.insert(END, task)
        self.my_entry.delete(0, 'end')
        self.choice.destroy()

    def add_short_goal(self):
        task = self.my_entry.get()
        self.short_term_listbox.insert('end', task)
        self.my_entry.delete(0, 'end')
        self.choice.destroy()

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
        label = tk.Label(self, text="To Do List", font=('MS Sans Serif', 10, 'bold'))
        label.pack(pady=10, padx=10)

        btn_exit = tk.Button(self, text="Back to Main Page",
                             command=lambda: controller.show_frame(Main))
        btn_exit.place(x=10, y=460)

        # widgets for to do list
        self.my_entry = tk.Entry(self)
        self.to_do_listbox = tk.Listbox(self, width=20, height=10, activestyle='none', bg='light blue',
                                        selectbackground='powder blue')
        self.long_term_listbox = tk.Listbox(self, width=20, height=10, activestyle='none', bg='light blue',
                                            selectbackground='powder blue')

        btn_add = tk.Button(self, text='Add Task', command=self.add_task)
        btn_del = tk.Button(self, text='Delete \n Task', command=self.delete_task)
        btn_del_all = tk.Button(self, text='Delete All \n Tasks', command=self.delete_all_tasks)
        btn_mark = tk.Button(self, text='Mark as \n completed', command=self.mark_completed)

        # setting position of the widgets in app
        btn_add.place(x=50, y=350)
        btn_del.place(x=150, y=350)
        btn_del_all.place(x=225, y=350)
        btn_mark.place(x=50, y=450)
        self.to_do_listbox.place(x=120, y=130)
        self.my_entry.place(x=100, y=50, width=150, height=50)

    # Functions

    # Add tasks to to-do list depending on user-input
    def add_task(self):
        task = self.my_entry.get()
        if 5 >= len(self.my_entry.get()) > 0:
            self.to_do_listbox.insert(END, task)
            self.my_entry.delete(0, 'end')
        elif len(self.my_entry.get()) > 5:
            messagebox.showinfo('Too long', 'Please consider shortening the length of your task')
        else:
            if len(self.my_entry.get()) == "":
                messagebox.showwarning('No input entered', 'Please enter a task')

    def delete_task(self):
        self.to_do_listbox.delete(ANCHOR)

    # Delete all tasks in task listbox once user has confirmed
    def delete_all_tasks(self):
        size = self.to_do_listbox.size()
        if size != 0:
            message_box = messagebox.askyesno('Delete All Tasks', 'Are you sure?')
            if message_box:
                self.to_do_listbox.delete(0, 'end')

    def mark_completed(self):
        marked = self.to_do_listbox.curselection()
        temp = marked[0]
        temp_marked = self.to_do_listbox.get(marked)
        temp_marked = temp_marked+" ✔"
        self.to_do_listbox.insert(temp, temp_marked)


if __name__ == "__main__":
    app = StudyApp()
    app.mainloop()
