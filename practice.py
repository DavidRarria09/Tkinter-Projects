import tkinter as tk
from tkinter import messagebox as mb

def info():
    mb.showinfo("Info", "Text informativ")
def avertisment():
    mb.showwarning("Avertisment", "Text informativ")
def eroare():
    mb.showerror("Eroare", "Text informativ")
def yn():
    raspuns=mb.askyesno("Alegere", "Vrei?")
    if raspuns:
        print("Yay!")
    else:
        print("Bruh")
root = tk.Tk()
root.title("Test app")
root. geometry("250x250")
b1 = tk.Button(text="Info", command=info)
b1.pack()
b2=tk.Button(text="Avertisment", command=avertisment)
b2.pack()
b3=tk.Button(text="Eroare", command=eroare)
b3.pack()
b4=tk.Button(text="Yes or No", command=yn)
b4.pack()
root.mainloop()