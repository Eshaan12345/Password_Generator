from tkinter import *
import random
root = Tk()
root.title("Password Generator")
root.geometry("400x400")

text = Entry(root)
label1 = Label(root)
label = Label(root)

array_3d = [[["I", "J", "K", "L", "M", "N", "O"], ["king", "queen"], ["!", "@", "#", "$", "%", "^", "&", "*"]]]
def check():
    r1 = random.randint(0,6)
    r2 = random.randint(0,1)
    r3 = random.randint(0,7)
    answer = text.get()
    label1["text"] = "Guessed Password = " + str(answer)
    
    letter1 = str(array_3d[0][0][r1]) # casting to a string
    letter2 = array_3d[0][1][r2]
    letter3 = array_3d[0][2][r3]
    
    label["text"] = "Correct Password = " + letter1 + "" + letter2 + "" + letter3
    
btn = Button(root, text = "Check", command = check)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
text.place(relx = 0.5, rely = 0.3, anchor = CENTER)
label1.place(relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()