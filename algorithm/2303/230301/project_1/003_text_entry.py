from tkinter import *

root = Tk()
root.title("Gui.change")
root.geometry("630x480")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END,"insert word")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력가능함")

def btncmd():
    print(txt.get("1.0", END)) # 1 : 첫번째 라인, 0 : 0번째 column  위치
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()