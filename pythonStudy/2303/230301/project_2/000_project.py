import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("word change")
root.geometry("450x520")
# file 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5,pady=5, width=12, text="파일 추가")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5,pady=5, width=12, text="파일 삭제")
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side = "right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right")

# 단어  프레임
frame_word = LabelFrame(root, text="옵션", relief="ridge", borderwidth=2, padx=5)
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

lbl_width2 = Label(frame_word3, text="3번째 변경단어 입력", width=20)
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
btn2 = Button(frame_end, text="닫기", width=10, padx=5, command=root.quit)
btn2.pack(side="right")

btn1 = Button(frame_end, text="실행", width=10, padx=5)
btn1.pack(side="right")

root.resizable(False,False)
root.mainloop()