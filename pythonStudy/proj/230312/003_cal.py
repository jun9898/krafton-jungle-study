import tkinter as tk

# 계산기 창 생성
root = tk.Tk()
root.title("계산기")

# 결과 표시 라벨
result_label = tk.Label(root, text="0", width=25, height=2, font=("Arial", 18))
result_label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# 숫자 버튼 클릭 시 실행되는 함수
def click_number(number):
    current = result_label.cget("text")
    if current == "0":
        current = ""
    result_label.configure(text=current + str(number))

# 연산 버튼 클릭 시 실행되는 함수
def click_operator(operator):
    global first_number, operation
    first_number = float(result_label.cget("text"))
    operation = operator
    result_label.configure(text="0")

# "=" 버튼 클릭 시 실행되는 함수
def click_equal():
    global first_number, operation
    second_number = float(result_label.cget("text"))
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number
    else:
        result = 0
    result_label.configure(text=str(result))

# "C" 버튼 클릭 시 실행되는 함수
def click_clear():
    result_label.configure(text="0")

# 숫자 버튼 생성
for i in range(1, 10):
    button = tk.Button(root, text=str(i), width=5, height=2, font=("Arial", 18), command=lambda number=i: click_number(number))
    button.grid(row=((i-1)//3)+1, column=(i-1)%3, padx=5, pady=5)

# 0 버튼 생성
button_0 = tk.Button(root, text="0", width=5, height=2, font=("Arial", 18), command=lambda number=0: click_number(number))
button_0.grid(row=4, column=1, padx=5, pady=5)

# 연산 버튼 생성
button_add = tk.Button(root, text="+", width=5, height=2, font=("Arial", 18), command=lambda operator="+": click_operator(operator))
button_add.grid(row=1, column=3, padx=5, pady=5)

button_subtract = tk.Button(root, text="-", width=5, height=2, font=("Arial", 18), command=lambda operator="-": click_operator(operator))
button_subtract.grid(row=2, column=3, padx=5, pady=5)

button_multiply = tk.Button(root, text="*", width=5, height=2, font=("Arial", 18), command=lambda operator="*": click_operator(operator))
button_multiply.grid(row=3, column=3, padx=5, pady=5)

button_divide = tk.Button(root, text="/", width=5, height=2, font=("Arial", 18), command=lambda operator="/": click_operator(operator))
button_divide.grid(row=4, column=3, padx=5, pady=5)

# "=" 버튼 생성
button_equal = tk.Button(root, text="=", width=5, height=2, font=("Arial", 18), command=click
