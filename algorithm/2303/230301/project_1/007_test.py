import os
from tkinter import *

root = Tk()
root.title("window 메모장")
root.geometry("630x480")


#열기, 저장 파일 이름
filename = "mynote.txt"

def create_new_file():
    if os.path.isfile(filename): #파일이 있다면 열면 된다
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))

def close_file():
    root.quit #파일 종료하는 코드 찾아서 입력하기

#메뉴 만들기
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="save_file", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="close_file", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)
menu.add_cascade(label="edit")
menu.add_cascade(label="show")
menu.add_cascade(label="how")
root.config(menu=menu)

#스크롤 바 만들기
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

#텍스트 박스 만들기
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.mainloop()



