
from tkinter import *

root = Tk()
root.title("Gui.change")
root.geometry("640x480")

label1 = Label(root, text="hi")
label1.pack()

photo = PhotoImage(file="230301/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또만나요")
    global photo2
    photo2 = PhotoImage(file="230301/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()