# 코드
import shutil
import datetime as dt
import os
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog

# ctrl + v ->  영역 설정
# 대문자 I
# 변경될 내용 입력
# esc
g_init_dir = "c:/"
g_cchar_0_src = ""    
g_cchar_0_target = ""    
g_cchar_1_src = ""    
g_cchar_1_target = ""    
g_cchar_2_src = ""    
g_cchar_2_target = ""    
g_last_file_root = ""
g_last_folder_root = ""

root = Tk()
root.title("파일명 변경(대흥소프트밀-전병준)")
root.geometry("450x520")
file_roots = ()

# 폴더 추가
# def add_folder():
#     folders = filedialog.askopenfilenames(title="변경할 폴더를 선택하세요.", \
#             filetypes=(("DXF 파일", "*.dxf"), ("모든 파일", "*.*")), \
#             initialdir="C:/")
# # 사용자가 선택한 파일 목록
#     for folder in folders:
#         list_file.insert(END, folder

def clear_files():
    list_file.delete(0,'end')

def add_folder():
    clear_files()
    folders = filedialog.askdirectory(title="변경할 폴더를 선택하세요.", \
            initialdir=r"C:/")
   
        
# 사용자가 선택한 파일 목록
    global g_last_file_root
    g_last_file_root = os.path.abspath(folders)
    x = dt.datetime.now()
    files = os.listdir(folders)
    for i in files:
        list_file.insert(END, i)
    # list_file.insert(END, folders)
    # print(list_file)
#선택 삭제
def unselect_files():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 폴더 만들기

def save_original_folder_and_files():
    x = dt.datetime.now()
    shutil.copytree(g_last_file_root,g_last_file_root+"_"+x.strftime("%Y%m%d"))


# def test():
#     g_last_file_root ="c:/Temp/a"
#     test_target_dir ="c:/Temp/b"
#     # x = dt.datetime.now()
#     # print("x->",x)
#     # shutil.copytree(g_last_file_root, g_last_file_root+x.strftime("%Y%m%d"))
#     shutil.copytree(g_last_file_root, test_target_dir)

# def getTextInput():
#     print(txt_1.get(1.1,"end"))
    
# 저장경로
# def save_root():
#     if len(list_file.get()) == 0:
#         mbox
#     folder_selected = filedialog.askdirectory()
#     if folder_selected == '':
#         return
    # print(folder_selected)
    # txt_dest_path.delete(0, END)
    # txt_dest_path.insert(0,folder_selected)


# def test_func(list_file):
#     for i in list_file.get(0, END):
#         # print("i->",i)
#         for j in i:
#             if len(txt_1.get()) >= 1  and txt_1.get() in j:
#                 print(dic[txt_1.get()], end="")
#             elif len(txt_3.get()) >= 1 and txt_3.get() in j:
#                 print(dic[txt_3.get()], end="")
#             elif len(txt_5.get()) >= 1 and txt_5.get() in j:
#                 print(dic[txt_5.get()], end="")
#             else:
#                 print(j, end="")    
#             print()
#     return 
# def cha_word_2(list_file):
#     # z = g_last_file_root+"\\"+(test_func(list_file))
#     # print(z)
#     for i in list_file.get(0, END):
#         # print("i->",i)
#         for j in i:
#             print("i--- ",i)
#             # if len(txt_1.get()) >= 1  and txt_1.get() in j:
#             if len(txt_1.get()) >= 1  and txt_1.get() == j:
#                 print(dic[txt_1.get()], end="")
#             # elif len(txt_3.get()) >= 1 and txt_3.get() in j:
#             elif len(txt_3.get()) >= 1 and txt_3.get() == j:
#                 print(dic[txt_3.get()], end="")
#             # elif len(txt_5.get()) >= 1 and txt_5.get() in j:
#             elif len(txt_5.get()) >= 1 and txt_5.get() == j:
#                 print(dic[txt_5.get()], end="")
#             else:
#                 print(j, end="")    
#         print("j--- ",j)
#     return j             
# 파일 이름 변경 (저장은 어떻게)
def cha_word():
    # z = cha_word_2(list_file)
    # z = g_last_file_root+"\\"+(test_func(list_file))
    # print(z)
    for i in list_file.get(0, END):
        print("before fname ->",i)
        renamed_fname = ""
        for j in i:
            print(" ",j,"in ",i)
            if len(txt_1.get()) >= 1  and txt_1.get() in j:
                # print(dic[txt_1.get()], end="")
                renamed_fname = renamed_fname + dic[txt_1.get()]
            elif len(txt_3.get()) >= 1 and txt_3.get() in j:
                # print(dic[txt_3.get()], end="")
                renamed_fname = renamed_fname + dic[txt_3.get()]
            elif len(txt_5.get()) >= 1 and txt_5.get() in j:
                # print(dic[txt_5.get()], end="")
                renamed_fname = renamed_fname + dic[txt_5.get()]
            else:
                # print(j, end="")    
                renamed_fname = renamed_fname + j
        # 변경될 파일 이름
        os.rename(g_last_file_root+"\\"+i,g_last_file_root+"\\"+renamed_fname)
        # print(test_func(list_file))
        # os.rename(g_last_file_root+"\\"+i,g_last_file_root+"\\"+test_func(list_file))
        # list_file.insert(0, END) 

# 저장경로 정하기 (많은 수정 요함 )
# def save_file():
#     file_name = filedialog.SaveFileDialog(initialdir=g_init_dir, filetypes=(("dxf files", "*.dxf"),("allfiles", "*.*")))    
#     print(file_name)    

# 시작
def start():
    print()
    # print(len(txt_1.get()))
    # print(len(txt_3.get()))
    # print(len(txt_5.get()))
    if len(txt_1.get()) >= 1:
        dic[txt_1.get()] = txt_2.get()
    if len(txt_3.get()) >= 1:
        dic[txt_3.get()] = txt_4.get()
    if len(txt_5.get()) >= 1:
        dic[txt_5.get()] = txt_6.get()
    if list_file.size() == 0:
    

        msgbox.showwarning("경고", "파일을 추가하세요")


    
# 파일 이름 변경 후 저장하기

# 원본 파일 만들어진 폴더에 이동하기


    #저장경로 확인
    # if len(txt_dest_path.get()) == 0:
    #     msgbox.showwarning("경고", "저장 경로를 선택하세요")

    print(dic)
    save_original_folder_and_files()
    cha_word()

    # 처음 선택했던 폴더의 경로를 config 값으로 저장해야 다음 작업이 가능함 
    # 폴더 생성 (오늘날짜가 앞에 붙도록)
    # 파일 이름 변경하여 기존 폴더에 저장
    # 기존 파일 새로 생성된 폴더로 이동
    # save_file()

# init_dir c:\temp
# cchar_0 ^ -
# cchar_1 ( ,
# cchar_2 none none
# def get_init_config():
    # read config.ini
    # if ( ! config.txt ):
    #     return
    # init_dir = xxxx
    # cchar_0_src =     
    # cchar_0_target =     
    # cchar_1_src =     
    # cchar_1_target =     
    # cchar_2_src =     
    # cchar_2_target =     
    # return

# get_init_config()


dic = {}


# file 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5,pady=5, width=12, text="폴더 선택", command=add_folder)
btn_add_file.pack(side="left")

btn_unselect_file = Button(file_frame, padx=5,pady=5, width=12, text="파일 취소", command=unselect_files)
btn_unselect_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side = "right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장경로 프레임
# path_frame = LabelFrame(root, text="저장경로")
# path_frame.pack(fill="x", padx=5, pady=5)

# txt_dest_path = Entry(path_frame)
# txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)

# btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=save_root)
# btn_dest_path.pack(side="right")

# 단어  프레임
frame_word = LabelFrame(root, text="옵션1", relief="ridge", borderwidth=2, padx=5)
frame_word.pack()

frame_word2 = LabelFrame(root, text="옵션2",relief="ridge", borderwidth=2, padx=5)
frame_word2.pack()

frame_word3 = LabelFrame(root, text="옵션3", relief="ridge", borderwidth=2, padx=5)
frame_word3.pack()

# 변경 단어 입력 텍스트박스
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

# 닫기 실행 버튼 프레임
frame_end = LabelFrame(root, relief="flat", borderwidth=2, padx=5)
frame_end.pack(side="right")

# 닫기버튼
btn3 = Button(frame_end, text="닫기", width=10, padx=5, command=root.quit)
btn3.pack(side="right")

# 저장버튼
# btn2 = Button(frame_end, text="저장", width=10, padx=5,) #command = save_root)
# btn2.pack(side="right")

# 실행버튼
btn1 = Button(frame_end, text="실행", width=10, padx=5, command=start)
btn1.pack(side="right")

root.resizable(False,False)
root.mainloop()