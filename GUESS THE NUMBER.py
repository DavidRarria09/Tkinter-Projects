import random
import math
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import simpledialog as ask

Light=False
is_playing = False
opened_w = False
stats = {
    "games_played":0,
    "average_guesses":0
}

def change_style():
    global Light
    if Light:
        Light=False
        root.config(bg="#1a1a1a")
        header.config(bg="#15557f")
        dark_mode.config(bg="#0c2a46",text="Light Mode")
        label_space.config(bg="#1a1a1a")
        play.config(bg="#0c2a46")
        stat.config(bg="#0c2a46")
        exit.config(bg="#0c2a46")
    else:
        Light = True
        root.config(bg="#ffffff")
        header.config(bg="#7cfffd")
        dark_mode.config(bg="#ffa200",text="Dark Mode")
        label_space.config(bg="#ffffff")
        play.config(bg="#ffa200")
        stat.config(bg="#ffa200")
        exit.config(bg="#ffa200")
def gameplay():
    global is_playing
    stats["games_played"]+=1
    print(stats["games_played"])
    if not is_playing:
        is_playing = True
        result = mb.askyesno("Play?", "Do you want to play?")
        if result:
            tries = 1
            guessed = False
            num = random.randint(1, 100)
            guess = ask.askinteger("Ask", "Choose a number between 1 and 100!", minvalue=1, maxvalue=100)
            while not guessed and is_playing:
                if guess is None:
                    mb.showerror("YOU LOSE", "YOU LOST! THE NUMBER WAS {0}!".format(num))
                    is_playing=False
                elif guess == num:
                    guessed = True
                else:
                    tries+=1
                    if guess < num:
                        guess = ask.askinteger("Ask", "The value is higher than {0}".format(guess), minvalue=1, maxvalue=100)
                    else:
                        guess = ask.askinteger("Ask", "The value is lower than {0}".format(guess), minvalue=1, maxvalue=100)
            if guessed:
                form = "TRIES"
                if tries==1:
                    form="TRY"
                mb.showinfo("YOU WIN", "THE NUMBER IS {0}! YOU GUESSED IN {1} {2}!".format(num, tries, form))
            stats["average_guesses"]=stats["average_guesses"]+tries
        is_playing = False
def stat_win():
    global opened_w
    def close():
        global opened_w
        opened_w=False
        win.destroy()
    if not opened_w:
        opened_w = True
        win = tk.Toplevel()
        win.iconbitmap("data/icon.ico")
        win.title("STATS")
        win.geometry("400x300")
        win.resizable(width=False, height=False)

        head = tk.Label(win, text="STATS")
        head.pack()

        played = tk.Label(win, text="GAMES PLAYED: {0}".format(stats["games_played"]))
        played.pack()

        if stats["games_played"] ==0:
            avg = tk.Label(win, text="AVERAGE TRIES: 0")
        else:
            avg = tk.Label(win, text="AVERAGE TRIES: {0}".format(math.ceil(stats["average_guesses"] / stats["games_played"])))
        avg.pack()

        win.protocol("WM_DELETE_WINDOW", lambda:close())

root = tk.Tk()
root.iconbitmap("data/icon.ico")
root.title("GUESS THE NUMBER")
root.geometry("200x150")
root.resizable(width=False, height=False)

header=tk.Label(root, text="GUESS THE NUMBER")
header.pack()

dark_mode=tk.Button(root, text="Dark Mode", command=lambda:change_style())
dark_mode.pack()

label_space =  tk.Label(bg="#ffffff")
label_space.pack()

play=tk.Button(root, text="PLAY", command=lambda:gameplay())
play.pack()

stat = tk.Button(root, text="STATS", command=lambda:stat_win())
stat.pack()

exit=tk.Button(root, text="EXIT", command=lambda:root.destroy())
exit.pack()

change_style()
root.mainloop()