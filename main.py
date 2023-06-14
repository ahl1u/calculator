import tkinter as tk

calculation = "0"

def add(symbol):
    global calculation
    if calculation == "0":
        if str(symbol) == '0':
            return
        else:
            calculation = ''
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate():
    global calculation
    try:
        check_num = eval(calculation)
        if check_num == round(check_num):
            check_num = int(check_num)
        calculation = str(check_num)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear()
        text_result.insert(1.0, "Error!")

def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.insert(1.0, calculation)
text_result.grid(columnspan=5)

button_1 = tk.Button(root, text = "1", command=lambda: add(1), width=5, font=("Calibri", 12))
button_1.grid(row=2, column=1)
button_2 = tk.Button(root, text = "2", command=lambda: add(2), width=5, font=("Calibri", 12))
button_2.grid(row=2, column=2)
button_3 = tk.Button(root, text = "3", command=lambda: add(3), width=5, font=("Calibri", 12))
button_3.grid(row=2, column=3)
button_4 = tk.Button(root, text = "4", command=lambda: add(4), width=5, font=("Calibri", 12))
button_4.grid(row=3, column=1)
button_5 = tk.Button(root, text = "5", command=lambda: add(5), width=5, font=("Calibri", 12))
button_5.grid(row=3, column=2)
button_6 = tk.Button(root, text = "6", command=lambda: add(6), width=5, font=("Calibri", 12))
button_6.grid(row=3, column=3)
button_7 = tk.Button(root, text = "7", command=lambda: add(7), width=5, font=("Calibri", 12))
button_7.grid(row=4, column=1)
button_8 = tk.Button(root, text = "8", command=lambda: add(8), width=5, font=("Calibri", 12))
button_8.grid(row=4, column=2)
button_9 = tk.Button(root, text = "9", command=lambda: add(9), width=5, font=("Calibri", 12))
button_9.grid(row=4, column=3)
button_0 = tk.Button(root, text = "0", command=lambda: add(0), width=5, font=("Calibri", 12))
button_0.grid(row=5, column=2)

button_plus = tk.Button(root, text = "+", command=lambda: add("+"), width=5, font=("Calibri", 12))
button_plus.grid(row=2, column=4)

button_minus = tk.Button(root, text = "-", command=lambda: add("-"), width=5, font=("Calibri", 12))
button_minus.grid(row=3, column=4)

button_mult = tk.Button(root, text = "*", command=lambda: add("*"), width=5, font=("Calibri", 12))
button_mult.grid(row=4, column=4)

button_div = tk.Button(root, text = "/", command=lambda: add("/"), width=5, font=("Calibri", 12))
button_div.grid(row=5, column=4)

button_open = tk.Button(root, text = "(", command=lambda: add("("), width=5, font=("Calibri", 12))
button_open.grid(row=5, column=1)

button_close = tk.Button(root, text = ")", command=lambda: add(")"), width=5, font=("Calibri", 12))
button_close.grid(row=5, column=3)

button_equals = tk.Button(root, text = "=", command= evaluate, width=15, font=("Calibri", 12))
button_equals.grid(row=6, column=1, columnspan=2)

button_clear = tk.Button(root, text = "C", command= clear, width=5, font=("Calibri", 12))
button_clear.grid(row=6, column=3)

button_decimal = tk.Button(root, text = ".", command= lambda: add("."), width=5, font=("Calibri", 12))
button_decimal.grid(row=6, column=4)

root.mainloop()
