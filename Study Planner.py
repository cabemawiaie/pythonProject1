
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My Study Planner")
root.geometry('350x500')
main_frame = Frame(root, height=150, width=100)
main_frame.pack()

intro = Label(main_frame, text="Welcome to My Study Planner")
intro.pack(side=TOP, padx=5, pady=5)

calendar_button = ttk.Button(main_frame, text="Calendar")
calendar_button.pack(padx=5, pady=5)

goals_button = ttk.Button(main_frame, text="Goals")
goals_button.pack(padx=5, pady=5)

deadline_button = ttk.Button(main_frame, text="Deadlines")
deadline_button.pack(padx=5, pady=5)

back_button = ttk.Button(root, text="Back")
back_button.place(x=10, y=470)

root.mainloop()
