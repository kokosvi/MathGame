import os
from tkinter import *
import random

root = Tk()
root.title("Math Game")
program_directory = sys.path[0]
root.iconphoto(True, PhotoImage(file=os.path.join(program_directory, "test.png")))
root.geometry("400x400")


def generate_num():
    return random.randint(0, 100)


def calculate():
    if first_num + second_num == int(your_answer.get()):
        result_message["text"] = "Correct!"
    else:
        result_message["text"] = "Incorrect!"


def generate():
    global first_num
    first_num = generate_num()
    global second_num
    second_num = generate_num()
    sum_expression["text"] = str(first_num) + " + " + str(second_num) + " ="


title = Label(root, text="Calculate this:", anchor=CENTER, width=30, padx=5, pady=5)
title.grid(row=0, column=0, columnspan=2)

first_num = generate_num()
second_num = generate_num()
sum_expression = Label(root, text=str(first_num) + " + " + str(second_num) + " =", anchor=CENTER, width=30, padx=5, pady=5)
sum_expression.grid(row=1, column=0, columnspan=2)

your_answer = Entry(root)
your_answer.grid(row=2, column=0, columnspan=2)

btn_calculate = Button(root, text="Calculate", command=calculate)
btn_calculate.grid(row=3, column=0)

btn_generate = Button(root, text="Generate", command=generate)
btn_generate.grid(row=3, column=1)

result_message = Label(root)
result_message.grid(row=4, column=0)

root.mainloop()
