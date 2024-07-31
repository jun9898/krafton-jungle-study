from tkinter import *

root = Tk()
root.title("Gui.change")
root.geometry("630x480")

frame_burger = Frame(root, relief="solid", bd=2)
frame_burger.pack()

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()



root.mainloop()