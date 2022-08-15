# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My Study Planner")
root.geometry('350x500')
main_frame = Frame(root, height=150, width=100)
main_frame.pack()

intro = Label(main_frame, text="Welcome to My Study Planner")
intro.pack(side=TOP, padx=5, pady=5)

# Fuction to open new window on button click
def create_page():
    goals_page = Toplevel(root)
    goals_page.geometry('350x500')
    goals_page.title("Goals")
    goals_page.grab_set()

calendar_button = Button(main_frame, text="Calendar", bg="lightblue")
calendar_button.pack(padx=5, pady=5)

goals_button = Button(main_frame, text="Goals", bg="lightblue", command=create_page)
goals_button.pack(padx=5, pady=5)

deadline_button = Button(main_frame, text="Deadlines", bg="lightblue")
deadline_button.pack(padx=5, pady=5)

back_button = Button(root, text="Back", bg="lightblue")
back_button.place(x=10, y=470)








root.mainloop()
