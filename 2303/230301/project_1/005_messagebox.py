import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Gui.change")
root.geometry("630x480")

#기차예매
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료했습니다.")

def warn():
    msgbox.showwarning("경고", "해당좌석은 이미 예매되었습니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생하였습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아 동반석입니다. 예매하시겠습니까?.")

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

def yesno():
    msgbox.askyesno("예 / 아니요", "해당좌석은 역방향입니다. 예매 하시곗습니까?")

def yesnocancel():
    respones = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n 저장시겠습니까?")
    print("응답 :", respones)
    if respones == 1:
        print("yes")
    elif respones == 0:
        print("no")
    else:
        print("cancel")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 / 취소").pack()
Button(root, command=retrycancel, text="재시도 / 취소").pack()
Button(root, command=yesno, text="예 아니요").pack()
Button(root, command=yesnocancel, text="예 아니요 취소").pack()
root.mainloop()