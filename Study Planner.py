
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My Study Planner")


main_frame = Frame(root, height=250, width=250)
main_frame.pack_propagate(0)
main_frame.pack(padx=5, pady=5)

intro = Label(main_frame, text="Welcome to My Study Planner")
intro.pack(side=TOP)


calendar_button = ttk.Button(main_frame, text="Calendar")
calendar_button.pack()

goals_button = ttk.Button(main_frame, text="Goals")
goals_button.pack()

deadline_button = ttk.Button(main_frame, text="Deadlines")
deadline_button.pack()

root.mainloop()
