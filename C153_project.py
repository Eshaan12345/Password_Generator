from tkinter import *
import random
root = Tk()
root.title("Password Generator")
root.geometry("400x400")


label = Label(root)

array_3d = [[["I", "J", "K", "L", "M", "N", "O"], ["king", "queen"], ["!", "@", "#", "$", "%", "^", "&", "*"]]]
def new_password():
    r1 = random.randint(0,6)
    r2 = random.randint(0,1)
    r3 = random.randint(0,7)
    
    letter1 = str(array_3d[0][0][r1]) # casting to a string
    letter2 = array_3d[0][1][r2]
    letter3 = array_3d[0][2][r3]
    
    label["text"] = letter1 + "" + letter2 + "" + letter3
    
btn = Button(root, text = "New Password", command = new_password)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()