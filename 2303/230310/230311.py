import shutil
import datetime as dt
import os
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog

# How to ues config?

root = Tk()
root.title("파일명 변경(대흥소프트밀-전병준)")
root.geometry("450x470")
file_roots = ()
dic = {}

# clear files
def clear_files():
    list_file.delete(0,'end')

# folder select
def add_folder():
    clear_files()
    folders = filedialog.askdirectory(title="변경할 폴더를 선택하세요.", \
            initialdir=r"C:/")
    global g_last_file_root
    g_last_file_root = os.path.abspath(folders)
    x = dt.datetime.now()
    files = os.listdir(folders)
    for i in files:
        list_file.insert(END, i)

# deselect files
def unselect_files():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# mkdir  
def save_original_folder_and_files():
    x = dt.datetime.now()
    shutil.copytree(g_last_file_root,g_last_file_root+"_"+x.strftime("%Y%m%d"))

# renamed fname
def cha_word():
    for i in list_file.get(0, END):
        print("before fname ->",i)
        renamed_fname = ""
        for j in i:
            print(" ",j,"in ",i)
            if len(txt_1.get()) >= 1  and txt_1.get() in j:
                renamed_fname = renamed_fname + dic[txt_1.get()]
            elif len(txt_3.get()) >= 1 and txt_3.get() in j:
                renamed_fname = renamed_fname + dic[txt_3.get()]
            elif len(txt_5.get()) >= 1 and txt_5.get() in j:
                renamed_fname = renamed_fname + dic[txt_5.get()]
            else:
                renamed_fname = renamed_fname + j
        os.rename(g_last_file_root+"\\"+i,g_last_file_root+"\\"+renamed_fname)

# start_button
def start():
    if len(txt_1.get()) >= 1:
        dic[txt_1.get()] = txt_2.get()
    if len(txt_3.get()) >= 1:
        dic[txt_3.get()] = txt_4.get()
    if len(txt_5.get()) >= 1:
        dic[txt_5.get()] = txt_6.get()
    if list_file.size() == 0:
        msgbox.showwarning("경고", "파일을 추가하세요")
    save_original_folder_and_files()
    cha_word()

# file frame
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5,pady=5, width=12, text="폴더 선택", command=add_folder)
btn_add_file.pack(side="left")

btn_unselect_file = Button(file_frame, padx=5,pady=5, width=12, text="파일 취소", command=unselect_files)
btn_unselect_file.pack(side="right")

# list frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side = "right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# entry frame
frame_word = LabelFrame(root, text="옵션1", relief="ridge", borderwidth=2, padx=5)
frame_word.pack()

frame_word2 = LabelFrame(root, text="옵션2",relief="ridge", borderwidth=2, padx=5)
frame_word2.pack()

frame_word3 = LabelFrame(root, text="옵션3", relief="ridge", borderwidth=2, padx=5)
frame_word3.pack()

# entry word
lbl_width = Label(frame_word, text="첫번째 변경단어 입력", width=20)
lbl_width.pack(side="left")

txt_1 = Entry(frame_word, width=10)
txt_1.pack(side="left")

lbl_width = Label(frame_word, text="------->", width=10)
lbl_width.pack(side="left")

txt_2 = Entry(frame_word, width=10)
txt_2.pack(side="left")

lbl_width1 = Label(frame_word2, text="두번째 변경단어 입력", width=20)
lbl_width1.pack(side="left")

txt_3 = Entry(frame_word2, width=10)
txt_3.pack(side="left")

lbl_width = Label(frame_word2, text="------->", width=10)
lbl_width.pack(side="left")

txt_4 = Entry(frame_word2, width=10)
txt_4.pack()

lbl_width2 = Label(frame_word3, text="세번째 변경단어 입력", width=20)
lbl_width2.pack(side="left")

txt_5 = Entry(frame_word3, width=10)
txt_5.pack(side="left")

lbl_width = Label(frame_word3, text="------->", width=10)
lbl_width.pack(side="left")

txt_6 = Entry(frame_word3, width=10)
txt_6.pack()

# exit frame
frame_end = LabelFrame(root, relief="flat", borderwidth=2, padx=5)
frame_end.pack(side="right")

# exit button
btn3 = Button(frame_end, text="닫기", width=10, padx=5, command=root.quit)
btn3.pack(side="right")

# start button
btn1 = Button(frame_end, text="실행", width=10, padx=5, command=start)
btn1.pack(side="right")

root.resizable(False,False)
root.mainloop()