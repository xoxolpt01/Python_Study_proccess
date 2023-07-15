from tkinter import *
import Lib
from Lib import *


root = Tk()

# lab = Label(root, text="Something word", font="Arial 16 bold").place(x=15, y=20)
# fr = Frame(root, width=300, height=100, bg="#262626").pack(anchor=CENTER)
l1 = Label(root, text="Summ").grid(row=0, column=0)
e1 = Entry(root, background="BLACK", fg="WHITE")
e1.grid(row=2, column=1)
e2 = Entry(root, background="BLACK", fg="WHITE")
e2.grid(row=1, column=1)

def summ():
    l_answer_result = Label(root, text=f"{int(e1.get())+ int(e2.get())}")
    l_answer_result.grid(row=3, column=1)

but_1 = Button(root, text="Write two numbers to summ they", command=summ).grid(row=0, column=1)

l2 = Label(root, text="Number_1").grid(row=1, column=0)
l3 = Label(root, text="Number_2").grid(row=2, column=0)
l_answer = Label(root, text="Answer ").grid(row=3, column=0)
root.geometry("480x480+690+280")

root.mainloop()