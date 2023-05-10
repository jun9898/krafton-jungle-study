import shutil
import datetime as dt
import os
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
import configparser

config_ini = configparser.ConfigParser()

config_ini['DEFAULT'] = {}
config_ini['DEFAULT']['root_directory'] = ''
config_ini['DEFAULT']['old_str_1st_config'] = ''
config_ini['DEFAULT']['old_str_2nd_config'] = ''
config_ini['DEFAULT']['old_str_3rd_config'] = ''
config_ini['DEFAULT']['new_str_1st_config'] = ''
config_ini['DEFAULT']['new_str_2nd_config'] = ''
config_ini['DEFAULT']['new_str_3rd_config'] = ''


config_ini.read('config.ini', encoding='utf-8')

# ver = config['system']['setting1']
# title = config['system']['setting2']

# print(title,ver)
# how to use configpaser

root = Tk()
root.title("파일명 변경(대흥소프트밀-전병준)")
root.geometry("450x480")
file_roots = ()
dic = {}

# clear files
def clear_list_frame_files():
    add_file_list.delete(0,'end')

# folder select
def add_folder():
    clear_list_frame_files()
    root_config =config_ini['DEFAULT']['root']
    if root_config == '':
        root_config = 'c:/'
    folders = filedialog.askdirectory(title="변경할 폴더를 선택하세요.", \
            initialdir=root_config)
    config_ini['DEFAULT']['root'] = folders
    with open('config.ini', 'w', encoding='utf-8') as configfile:
        config_ini.write(configfile)
    config_ini.read('config.ini', encoding='utf-8')
    global g_last_file_root
    g_last_file_root = os.path.abspath(folders)
    x = dt.datetime.now()
    files = os.listdir(folders)
    for i in files:
        add_file_list.insert(END, i)

# deselect files
def unselect_files():
    for index in reversed(add_file_list.curselection()):
        add_file_list.delete(index)

# mkdir  
def save_original_folder_and_files():
    x = dt.datetime.now()
    shutil.copytree(g_last_file_root,g_last_file_root+"_"+x.strftime("%Y%m%d"))

# renamed fname
def rename_word():
    for i in add_file_list.get(0, END):
        print("before fname ->",i)
        renamed_fname = ""
        for j in i:
            print(" ",j,"in ",i)
            if len(old_str_entry_1st.get()) >= 1  and old_str_entry_1st.get() in j:
                renamed_fname = renamed_fname + dic[old_str_entry_1st.get()]
            elif len(old_str_entry_2nd.get()) >= 1 and old_str_entry_2nd.get() in j:
                renamed_fname = renamed_fname + dic[old_str_entry_2nd.get()]
            elif len(old_str_entry_3rd.get()) >= 1 and old_str_entry_3rd.get() in j:
                renamed_fname = renamed_fname + dic[old_str_entry_3rd.get()]
            else:
                renamed_fname = renamed_fname + j
        os.rename(g_last_file_root+"\\"+i,g_last_file_root+"\\"+renamed_fname)

# start_button
def start():
    if len(old_str_entry_1st.get()) >= 1:
        dic[old_str_entry_1st.get()] = new_str_entry_1st.get()
    if len(old_str_entry_2nd.get()) >= 1:
        dic[old_str_entry_2nd.get()] = new_str_entry_2nd.get()
    if len(old_str_entry_3rd.get()) >= 1:
        dic[old_str_entry_3rd.get()] = new_str_entry_3rd.get()
    if add_file_list.size() == 0:
        msgbox.showwarning("경고", "파일을 추가하세요")
    config_ini['DEFAULT']['button1'] = old_str_entry_1st.get()
    # old_str_entry_1st_config = config['DEFAULT']['button1']
    config_ini['DEFAULT']['button2'] = new_str_entry_1st.get()
    # new_str_entry_1st_config = config['DEFAULT']['button2']
    config_ini['DEFAULT']['button3'] = old_str_entry_2nd.get()
    # old_str_entry_2nd_config = config['DEFAULT']['button3']
    config_ini['DEFAULT']['button4'] = new_str_entry_2nd.get()
    # new_str_entry_2nd_config = config['DEFAULT']['button4']
    config_ini['DEFAULT']['button5'] = old_str_entry_3rd.get()
    # old_str_entry_3rd_config = config['DEFAULT']['button5']
    config_ini['DEFAULT']['button6'] = new_str_entry_3rd.get()
    # new_str_entry_3rd_config = config['DEFAULT']['button6']
    with open('config.ini', 'w', encoding='utf-8') as configfile:
        config_ini.write(configfile)
    save_original_folder_and_files()
    rename_word()

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

add_file_list = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
add_file_list.pack(side="left", fill="both", expand=True)
scrollbar.config(command=add_file_list.yview)

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

old_str_entry_1st = Entry(frame_word, width=10)
old_str_entry_1st_config = config_ini['DEFAULT']['button1']
old_str_entry_1st.insert(0, old_str_entry_1st_config)
old_str_entry_1st.pack(side="left")

lbl_width = Label(frame_word, text="------->", width=10)
lbl_width.pack(side="left")

new_str_entry_1st = Entry(frame_word, width=10)
new_str_entry_1st_config = config_ini['DEFAULT']['button1']
new_str_entry_1st.insert(0, new_str_entry_1st_config)
new_str_entry_1st.pack(side="left")

lbl_width1 = Label(frame_word2, text="두번째 변경단어 입력", width=20)
lbl_width1.pack(side="left")

old_str_entry_2nd = Entry(frame_word2, width=10)
old_str_entry_2nd_config = config_ini['DEFAULT']['button3']
old_str_entry_2nd.insert(0, old_str_entry_2nd_config)
old_str_entry_2nd.pack(side="left")

lbl_width = Label(frame_word2, text="------->", width=10)
lbl_width.pack(side="left")

new_str_entry_2nd = Entry(frame_word2, width=10)
new_str_entry_2nd_config = config_ini['DEFAULT']['button4']
new_str_entry_2nd.insert(0, new_str_entry_2nd_config)
new_str_entry_2nd.pack()

lbl_width2 = Label(frame_word3, text="세번째 변경단어 입력", width=20)
lbl_width2.pack(side="left")

old_str_entry_3rd = Entry(frame_word3, width=10)
old_str_entry_3rd_config = config_ini['DEFAULT']['button5']
old_str_entry_3rd.insert(0, old_str_entry_3rd_config)
old_str_entry_3rd.pack(side="left")

lbl_width = Label(frame_word3, text="------->", width=10)
lbl_width.pack(side="left")

new_str_entry_3rd = Entry(frame_word3, width=10)
new_str_entry_3rd_config = config_ini['DEFAULT']['button6']
new_str_entry_3rd.insert(0, new_str_entry_3rd_config)
new_str_entry_3rd.pack()

# exit frame
frame_end = LabelFrame(root, relief="flat", borderwidth=2, padx=5)
frame_end.pack(side="right")

# exit button
break_btn = Button(frame_end, text="닫기", width=10, padx=5, command=root.quit)
break_btn.pack(side="right")

# start button
rename_files_btn = Button(frame_end, text="실행", width=10, padx=5, command=start)
rename_files_btn.pack(side="right")

with open('config.ini', 'w', encoding='utf-8') as configfile:
    config_ini.write(configfile)

root.resizable(False,False)
root.mainloop()