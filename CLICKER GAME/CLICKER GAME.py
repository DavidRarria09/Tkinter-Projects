import tkinter as tk
from tkinter import messagebox as mb
import math

#main window
root = tk.Tk()

stats = {
    "clicks":0,
    "pow":1,
    "auto_clickers":0
}
price = {
    "pow":50,
    "auto_clickers":100
}
base_price={
    "pow": 50,
    "auto_clickers": 200
}
opened ={
    "shop" : False
}
buttons={
    "counter":lambda:"Clicks: "+str(stats["clicks"]),
    "button_p":lambda:"Buy "+str(price["pow"]),
    "label_p":lambda:"Buy click power! ({0})".format(str(stats["pow"])),
    "button_c":lambda:"Buy " + str(price["auto_clickers"]),
    "label_c":lambda:"Buy auto clickers! ({0})".format(str(stats["auto_clickers"]))
}

root.title("CLICKER GAME")
root.geometry("300x125")
root.resizable(width=False, height=False)
root.iconbitmap('data/icon.ico')
root.attributes('-fullscreen', False)

def error():
    mb.showerror("Broke boi", "Insufficient funds!")
def buy(stat_key):
    if stats["clicks"] >= price[stat_key]:
        stats["clicks"]-=price[stat_key]
        update_b(counter, "counter")
        stats[stat_key]+=1
        multiplier = 1
        if stat_key=="pow": multiplier=1.15
        elif stat_key=="auto_clickers": multiplier=1.20
        price[stat_key] = math.ceil(base_price[stat_key] * (multiplier ** stats[stat_key]))
    else: error()
def update_b(key, key_str):
    key.config(text=buttons[key_str]())
def update_clicks(val):
    stats["clicks"] += val
def auto_click():
    update_clicks(stats["auto_clickers"])
    update_b(counter, "counter")
    root.after(1000, auto_click)
def new_window(name):
    #shop window
    def close_window(win):
        opened[name] = False
        win.destroy()
    if name=="shop" and opened[name]==False:
        opened[name] = True
        shop = tk.Toplevel()
        shop.title("SHOP")
        shop.geometry("200x300")
        shop.iconbitmap("data/icon.ico")
        shop.resizable(width=False, height=False)

        label_p = tk.Label(shop, text="Buy click power! ({0})".format(str(stats["pow"])))
        label_p.pack()
        button_p = tk.Button(shop, text="Buy "+str(price["pow"]),
                             command=lambda:(buy("pow"),update_b(button_p,"button_p"),update_b(label_p, "label_p")))
        button_p.pack()

        label_c = tk.Label(shop, text="Buy auto clickers! ({0})".format(str(stats["auto_clickers"])))
        label_c.pack()
        button_c = tk.Button(shop, text="Buy " + str(price["auto_clickers"]),
                             command=lambda: (buy("auto_clickers"), update_b(button_c, "button_c"), update_b(label_c, "label_c")))
        button_c.pack()

        rgb(15,15,0,0,0,0,1, 0, shop)
        shop.protocol("WM_DELETE_WINDOW",lambda:close_window(shop))
def close_app():
    answer = mb.askyesno("Exit", "Are you sure you want to exit?")
    if answer:
        print("See you next time!")
        root.destroy()
def rgb(r1, r2, g1, g2, b1, b2, c, pos, ob):
    color = ["0","1","2","3","4","5","6","7","8","9","a", "b", "c", "d", "e", "f"]
    sol = [r1,r2,g1,g2,b1,b2]
    ob.config(bg="#"+color[sol[0]]+color[sol[1]]+color[sol[2]]+color[sol[3]]+color[sol[4]]+color[sol[5]])
    if(c%2):
        if pos<=3:
            if sol[pos]!=0:
                sol[pos]-=1
                sol[pos+2]+=1
            else: pos+=1
        else: c+=1
    else:
        if pos>=2:
            if sol[pos]!=0:
                sol[pos]-=1
                sol[pos-2]+=1
            else: pos-=1
        else:
            c+=1
            pos=0
    ob.after(25, lambda: rgb(sol[0], sol[1], sol[2], sol[3], sol[4], sol[5], c, pos, ob))

header = tk.Label(root, text="PRESS THE BUTTON")
header.pack()

counter = tk.Label(root, text="Clicks: "+str(stats["clicks"]), bg="white")
counter.pack()

button_main = tk.Button(root, text="Buton",
                        command=lambda:(update_clicks(stats["pow"]), update_b(counter,"counter")), bg="#99f2f9")
button_main.pack()

shop_b = tk.Button(root, text="Shop", bg="#99f2f9", command=lambda:new_window("shop"))
shop_b.pack()

exit_b = tk.Button(root, text="Exit", command=close_app, bg="#ff4d4d")
exit_b.pack()

rgb(15,15,0,0,0,0, 1, 0, root)
auto_click()
root.protocol("WM_DELETE_WINDOW", close_app)

#loop main
root.mainloop()