import tkinter as tk

#instanta ferestrei
root = tk.Tk()

root.title("CLICKER GAME")
root.geometry("300x125")
root.resizable(width=False, height=False)
root.iconbitmap('data/icon.ico')
root.attributes('-fullscreen', False)

def inchidere():
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
eticheta = (tk.Label(root, text="PRESS THE BUTTON!"))
eticheta.pack()

cnt=0
def update():
    global cnt
    cnt+=1
    label.config(text="You pressed the button "+str(cnt)+" times!")

label = tk.Label(root, text="You pressed the button  "+str(cnt)+" times!", bg="white")
label.pack()

buton = tk.Button(root, text="Buton", command=update, bg="#ff0000")
buton.pack()

exit_b = tk.Button(root, text="Exit", command=inchidere)
exit_b.pack()

rgb(15,15,0,0,0,0, 1, 0, root)
root.protocol("WM_DELETE_WINDOW", inchidere)

#loop main
root.mainloop()