import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as ask
import random

def inchidere():
    print("Sigma")
    root.destroy()

def citire_num():
    rezultat = ask.askinteger("Citire date", "Citeste un nr: ")
    mb.showinfo("Info","Numarul citit a fost: {0}".format(rezultat))

root = tk.Tk()
root.title("Practice")
root.geometry("200x200")
root.resizable(width=False, height=False)
root.protocol("WM_DELETE_WINDOW", lambda:inchidere())

button = tk.Button(root, text="info", command=lambda:mb.showinfo("Title", "Esti sigma"))
button.pack()

button_i = tk.Button(root, text="citeste un nr", command=lambda:citire_num())
button_i.pack()

root.mainloop()