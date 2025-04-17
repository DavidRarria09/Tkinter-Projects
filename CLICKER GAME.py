import tkinter as tk

stats = {
    "clicks":0,
    "pow":1,
}
price = {
"pow":100
}
opened ={
    "shop" : False
}
buttons={
    "counter":lambda:"Clicks: "+str(stats["clicks"]),
    "button_p":lambda:"Buy "+str(price["pow"])
}

#main window
root = tk.Tk()

root.title("CLICKER GAME")
root.geometry("300x125")
root.resizable(width=False, height=False)
root.iconbitmap('data/icon.ico')
root.attributes('-fullscreen', False)

def buy(stat_key):
    stats[stat_key]+=1
    price[stat_key]+=50
def update_b(key, key_str):
    key.config(text=buttons[key_str]())
def update_clicks():
    stats["clicks"] += stats["pow"]
def new_window(name):
    #shop window
    def close_shop():
        opened["shop"] = False
        shop.destroy()
    if name=="shop" and opened["shop"]==False:
        opened["shop"]=True
        shop = tk.Toplevel()
        shop.title("SHOP")
        shop.geometry("200x300")
        shop.iconbitmap("data/icon.ico")
        shop.resizable(width=False, height=False)

        label_p = tk.Label(shop, text="Buy click power!")
        label_p.pack()
        button_p = tk.Button(shop, text="Buy "+str(price["pow"]), command=lambda:(buy("pow"),update_b(button_p,"button_p")))
        button_p.pack()

        rgb(15,15,0,0,0,0,1, 0, shop)
        shop.protocol("WM_DELETE_WINDOW", close_shop)
def close_app():
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

header = (tk.Label(root, text="PRESS THE BUTTON!"))
header.pack()

counter = tk.Label(root, text="Clicks: "+str(stats["clicks"]), bg="white")
counter.pack()

button_main = tk.Button(root, text="Buton", command=lambda:(update_clicks(), update_b(counter,"counter")), bg="#99f2f9")
button_main.pack()

shop_b = tk.Button(root, text="Shop", bg="#99f2f9", command=lambda:new_window("shop"))
shop_b.pack()

exit_b = tk.Button(root, text="Exit", command=close_app, bg="#ff4d4d")
exit_b.pack()

rgb(15,15,0,0,0,0, 1, 0, root)
root.protocol("WM_DELETE_WINDOW", close_app)

#loop main
root.mainloop()