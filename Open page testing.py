# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
import tkinter as tk


# need to explain class
class StudyApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        width = 350
        height = 500

        self.geometry(f'{width}x{height}')
        self.minsize(350, 500)

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

    def bigger(self):
        x = self.parent.winfo_height() + 350
        y = self.parent.winfo_width() + 500

        # self.btnExit = Button(goalWindow(self.newWindow), text="Exit", bg="lightblue")
        # self.btnExit.place(x=10, y=470)x


class GoalPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, height=500, width=350)
        label = tk.Label(self, text="Your Goals", font=('MS Sans Serif', 10, 'bold'))
        label.pack(pady=10, padx=10)

        btn_exit = tk.Button(self, text="Back to Main Page",
                             command=lambda: controller.show_frame(Main))
        btn_exit.place(x=10, y=460)


class ToDoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="To Do List", font=('MS Sans Serif', 10, 'bold'))
        label.pack(pady=10, padx=10)

        btn_exit = tk.Button(self, text="Back to Main Page",
                             command=lambda: controller.show_frame(Main))
        btn_exit.place(x=10, y=460)

    def bigger(self):
        x = self.parent.winfo_height() + 350
        y = self.parent.winfo_width() + 500
        self.parent.geometry(f'{y}x{x}')


if __name__ == "__main__":
    app = StudyApp()
    app.mainloop()
