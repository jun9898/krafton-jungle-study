import tkinter as tk
from tkinter import filedialog
import os
import configparser
import shutil
from tkinter import filedialog, messagebox # messagebox 모듈 불러오기

def load_config():
    config_path = 'config.ini'

    if not os.path.exists(config_path):
        create_config()

    config = configparser.ConfigParser()
    config.read(config_path)

    if not config.has_option('DEFAULT', 'old_str') or not config.has_option('DEFAULT', 'new_str'):
        create_config()
        config.read(config_path)

    return config

def create_config():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'old_str': '', 'new_str': '', 'folder_path': '.'}

    with open('config.ini', 'w') as config_file:
        config.write(config_file)

def select_folder():
    folder_selected = filedialog.askdirectory()
    g_folder_path_entry.delete(0, tk.END)
    g_folder_path_entry.insert(0, folder_selected)

def show_changed_files(changed_files):
    top = tk.Toplevel()
    top.title('Changed Files')
    lb = tk.Listbox(top)
    lb.pack(fill='both', expand=True)
    for f in changed_files:
        lb.insert('end', f)
    top.mainloop()

def rename_files():
    folder_path = g_folder_path_entry.get()
    old_str = g_old_str_entry.get()
    new_str = g_new_str_entry.get()
    changed_files = []
    changed_files_cnt = 0

    if len(old_str)==0:
        messagebox.showinfo('Complete', 'old_str is empty!')
        return

    if len(new_str)==0:
        messagebox.showinfo('Complete', 'new_str is empty!')
        return

    config = configparser.ConfigParser()
    config.read('config.ini')
    config.set('DEFAULT', 'folder_path', folder_path)
    config.set('DEFAULT', 'old_str', old_str)
    config.set('DEFAULT', 'new_str', new_str)
    with open('config.ini', 'w') as config_file:
        config.write(config_file)

    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            if old_str in file_name:
                old_file_path = os.path.join(folder_path, file_name)
                new_file_name = file_name.replace(old_str, new_str)
                new_file_path = os.path.join(folder_path, new_file_name)
                ori_folder = os.path.join(folder_path, 'ori')
                if not os.path.exists(ori_folder):
                    os.makedirs(ori_folder)
                ori_file_path = os.path.join(ori_folder, file_name)
                shutil.copyfile(old_file_path, ori_file_path)
                os.rename(old_file_path, new_file_path)
                changed_files_cnt += 1 
                changed_files.append(new_file_name)

    if changed_files_cnt:
        messagebox.showinfo('Complete', 'File renaming complete!')
        show_changed_files(changed_files)
    else:
        messagebox.showinfo('Complete', 'None!')


def main():
    global g_folder_path_entry, g_old_str_entry, g_new_str_entry

    # Create window
    root = tk.Tk()
    root.geometry('500x300')
    root.title('File Renamer')

    # Create label for folder path input
    folder_path_label = tk.Label(root, text='Select Folder Path')
    folder_path_label.pack()

    # Create entry for folder path input
    g_folder_path_entry = tk.Entry(root, width=50)
    g_folder_path_entry.pack()

    # Create button to select folder
    select_folder_button = tk.Button(root, text='Select Folder', command=select_folder)
    select_folder_button.pack()

    # Create label for old string input
    old_str_label = tk.Label(root, text='Enter Old String')
    old_str_label.pack()

    # Create entry for old string input
    g_old_str_entry = tk.Entry(root, width=50)
    g_old_str_entry.pack()

    # Create label for new string input
    new_str_label = tk.Label(root, text='Enter New String')
    new_str_label.pack()

    # Create entry for new string input
    g_new_str_entry = tk.Entry(root, width=50)
    g_new_str_entry.pack()

    # Create button to rename files
    rename_button = tk.Button(root, text='Change', command=rename_files)
    rename_button.pack()

    load_config()

    # Read config.ini for previously selected folder, old string, and new string
    config = configparser.ConfigParser()
    config.read('config.ini')
    folder_path = config.get('DEFAULT', 'folder_path')
    old_str = config.get('DEFAULT', 'old_str')
    new_str = config.get('DEFAULT', 'new_str')

    if folder_path:
        g_folder_path_entry.insert(0, folder_path)
    if old_str:
        g_old_str_entry.insert(0, old_str)
    if new_str:
        g_new_str_entry.insert(0, new_str)

    # Start GUI event loop
    root.mainloop()

if __name__ == '__main__':
    main()