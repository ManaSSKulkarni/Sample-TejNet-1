"""tkinter"""

from tkinter import *
from tkinter import messagebox

# Create main window
top = Tk()
top.title("WELCOME")
top.geometry("400x300")

# Create 'Login' button and place it on the grid
btn1 = Button(top, text="Login")
btn1.grid(row=0, column=0, padx=10, pady=10)

# Create 'Name' label and entry field
name = Label(top, text="Name:")
name.grid(row=1, column=0, pady=10, padx=5, sticky=W)

e1 = Entry(top)
e1.grid(row=1, column=1, pady=10, padx=5)

# Create 'Regd No' label and entry field
regno = Label(top, text="Regd No:")
regno.grid(row=2, column=0, pady=10, padx=5, sticky=W)

e2 = Entry(top)
e2.grid(row=2, column=1, pady=10, padx=5)

# Create 'Submit' button and place it on the grid
btn2 = Button(top, text="Submit")
btn2.grid(row=3, column=1, pady=10, padx=5)


# Function for the button click
def fun():
    messagebox.showinfo("Hello", "Blue Button clicked")


# Create Red Button
btn3 = Button(top, text="RED", bg="red", fg="white", width=10, height=5, command=fun)
btn3.grid(row=4, column=0, padx=10, pady=10)

# Create Yellow Button
btn4 = Button(
    top, text="YELLOW", bg="yellow", fg="white", width=10, height=5, command=fun
)
btn4.grid(row=4, column=1, padx=10, pady=10)

# Entry Box
enty1 = Entry(top, fg="white", show="---")
enty1.grid(row=5, column=1, padx=10, pady=10)

# Label
lbl1 = Label(top, text="Metropolitan Cities", bg="green")
lbl1.grid(row=6, column=1, padx=12, pady=12)

# List Box
lb1 = Listbox(top, height=7)
lb1.insert(7, "Bengaluru")
lb1.insert(6, "Delhi")
lb1.insert(1, "Mumbai")
lb1.insert(2, "Chennai")
lb1.insert(3, "Hyderabad")
lb1.insert(4, "Bhopal")
lb1.insert(5, "Kolkata")
lb1.grid(row=7, column=1)

# Scale widget
scale = Scale(top, from_=-1000, to=1000, orient=HORIZONTAL)
scale.grid(row=10, column=1)

# Start the Tkinter event loop
top.mainloop()
