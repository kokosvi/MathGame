import os
from tkinter import *
import random

root = Tk()
root.title("Math Game")
program_directory = sys.path[0]
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "test.png")))
root.geometry("400x400")


def generateNum():
    return random.randint(0, 100)


def calculate():
    global e
    global x
    global y
    # if (lab1.winfo_exists()):
    #     lab1.destroy()
    # if (lab.winfo_exists()):
    #     lab.destroy()

    lab = Label(root)
    lab.grid(row=4, column=0)
    if x + y == int(e.get()):
        lab['text'] = "Correct!"
    else:
        lab['text'] = "Incorrect!"

def generate():
    global x
    global y
    x = generateNum()
    y = generateNum()
    exercise.destroy()
    exercise1 = Label(root, text=str(x) + " + " + str(y) + " =", anchor=CENTER, width=30, padx=5, pady=5)
    exercise1.grid(row=1, column=0, columnspan=2)


x = generateNum()
y = generateNum()
titlel = Label(root, text="Calculate this:", anchor=CENTER, width=30, padx=5, pady=5)
titlel.grid(row=0, column=0, columnspan=2)
exercise = Label(root, text=str(x) + " + " + str(y) + " =", anchor=CENTER, width=30, padx=5, pady=5)
exercise.grid(row=1, column=0, columnspan=2)
e = Entry(root)
e.grid(row=2, column=0, columnspan=2)
btn_e = Button(root, text="Calculate", command=calculate)
btn_e.grid(row=3, column=0)
btn_g = Button(root, text="Generate", command=generate)
btn_g.grid(row=3, column=1)

root.mainloop()
