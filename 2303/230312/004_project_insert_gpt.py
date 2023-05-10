import shutil
import datetime as dt
import os
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
import configparser

#config 파일 불러오기
def load_config():
    config_path = 'config.ini'

    if not os.path.exists(config_path):
        create_config()

    config = configparser.ConfigParser()
    config.read(config_path)

    error_case = 0
    # if not config.has_option('DEFAULT', 'root_diractory') :
    #      error_case = 1
    # if error_case != 0 and not config.has_option('DEFAULT', 'old_str_1st_ini') :
    #      error_case = 1
    # if error_case != 0 and not config.has_option('DEFAULT', 'old_str_2nd_ini') :
    #      error_case = 1
    # if error_case != 0 and not config.has_option('DEFAULT', 'old_str_3rd_ini') :
    #      error_case = 1
    # if error_case != 0 and not config.has_option('DEFAULT', 'new_str_1st_ini') :
    #      error_case = 1
    # if error_case != 0 and not config.has_option('DEFAULT', 'new_str_2nd_ini') :
    #      error_case = 1
    # if error_case != 0 and not config.has_option('DEFAULT', 'new_str_3rd_ini') :
    #      error_case = 

    # 만약 config 파일이 온전하지 않다면 다시 만들어서 config.ini에 저장하기
    if not config.has_option('DEFAULT', 'root_directory') \
    or not config.has_option('DEFAULT', 'old_str_1st_ini') \
    or not config.has_option('DEFAULT', 'old_str_2nd_ini') \
    or not config.has_option('DEFAULT', 'old_str_3rd_ini') \
    or not config.has_option('DEFAULT', 'new_str_1st_ini') \
    or not config.has_option('DEFAULT', 'new_str_2nd_ini') \
    or not config.has_option('DEFAULT', 'new_str_3rd_ini'):
        error_case = 1
    if error_case == 1:
        create_config()
        config.read(config_path)

    return config



def create_config():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'root_diractory':'', 'old_str_1st_ini':'', 'old_str_2nd_ini':'', 'old_str_3rd_ini':'', 
                         'new_str_1st_ini':'', 'new_str_2nd_ini':'', 'new_str_3rd_ini':''}
    with open('config.ini','w') as config_file:
        config.write(config_file)
# config_ini = configparser.ConfigParser(기

# config_ini['DEFAULT'] = {}
# config_ini['DEFAULT']['root_directory'] = ''
# config_ini['DEFAULT']['old_str_1st_config'] = ''
# config_ini['DEFAULT']['old_str_2nd_config'] = ''
# config_ini['DEFAULT']['old_str_3rd_config'] = ''
# config_ini['DEFAULT']['new_str_1st_config'] = ''
# config_ini['DEFAULT']['new_str_2nd_config'] = ''
# config_ini['DEFAULT']['new_str_3rd_config'] = ''


# config_ini.read('config.ini', encoding='utf-8')

# ver = config['system']['setting1']
# title = config['system']['setting2']

# print(title,ver)
# how to use configpaser

dic = {}

# clear files
def clear_list_frame_files():
    g_add_file_list.delete(0,'end')

# folder select
def add_folder():
    clear_list_frame_files()
    folders_root = filedialog.askdirectory(title="변경할 폴더를 선택하세요.", \
            initialdir='c:/')
    files = os.listdir(folders_root)
    for i in files:
        g_add_file_list.insert(END, i)

# deselect files
def unselect_files():
    for index in reversed(g_add_file_list.curselection()):
        g_add_file_list.delete(index)

def rename_file():
    

# mkdir  
def save_original_folder_and_files():
    x = dt.datetime.now()
    shutil.copytree(g_last_file_root,g_last_file_root+"_"+x.strftime("%Y%m%d"))

# renamed fname
def rename_word():
    for i in g_add_file_list.get(0, END):
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
def main():
    # file frame

    global g_add_file_list
    g_add_file_list = add_file_list

    root = Tk()
    root.title("파일명 변경(대흥소프트밀-전병준)")
    root.geometry("450x480")

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
    rename_files_btn = Button(frame_end, text="실행", width=10, padx=5, command=rename_files)
    rename_files_btn.pack(side="right")

    with open('config.ini', 'w', encoding='utf-8') as configfile:
        config_ini.write(configfile)

if __name__ == '__main__':
    main()

root.resizable(False,False)
root.mainloop()