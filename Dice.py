import random
import tkinter as tk
from tkinter import messagebox

def dice1():
    d1 = str(random.randint(1, 6))
    d2 = str(random.randint(1, 6))
    c=str("You Got:- "+d1+" at First Dice.\n You Got:- "+d2+" at Second Dice.")
    return c
def show_message1():
    messagebox.showinfo("Rolled",dice1())


root=tk.Tk()
root.title("Dice Roll")
root.geometry("400x300")
root.maxsize(500,400)
label=tk.Label(root,text="Roll Dice")
label.size()
button=tk.Button(root,text="Roll Dice",command=show_message1)
label.grid(row=0, column=0, padx=170, pady=10)
button.grid(row=2, column=0, padx=100, pady=10)

label.pack
button.pack
root.mainloop()

