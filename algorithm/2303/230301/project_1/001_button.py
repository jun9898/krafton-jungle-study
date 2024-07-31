
from tkinter import *

root = Tk()
root.title("Gui.change")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text= "button2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text= "button3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="button4")
btn4.pack()

photo = PhotoImage(file="230301/img.png")

btn5 = Button(root, image=photo)
btn5.pack()

def btntest():
    print("buttom on")

btn6 = Button(root, text="button_test", command=btntest)
btn6.pack()

root.mainloop()