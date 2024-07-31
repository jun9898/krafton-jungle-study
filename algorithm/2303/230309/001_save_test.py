import shutil
import datetime as dt
import os
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog


a = "c:\Temp\\a"
b = "c:\Temp\\b"

# print(a)
# print(b)
# g_last_file_root ="c:/Temp/a"
# test_target_dir ="c:/Temp/b"
# # x = dt.datetime.now()
# # print("x->",x)
# # shutil.copytree(g_last_file_root, g_last_file_root+x.strftime("%Y%m%d"))
# shutil.copytree(g_last_file_root, test_target_dir)
shutil.copytree(a,b)

# a\a
# a = "a\\a"

# print(a)
