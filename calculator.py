import tkinter as tk
from tkinter import messagebox


def make_digit_button(digit):
    return tk.Button(win, text=digit, font=('Arial', 13), bg='#87CEEB', fg='blue', command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(win, text=operation, font=('Arial', 15), bg='#B0C4DE', fg='red', command=lambda: add_operation(operation))


def make_clear_button(name_clear):
    return tk.Button(win, text=name_clear, font=('Arial', 15), bg='#AFEEEE', fg='green', command=lambda: clear())


def make_calculate_button(name_calc):
    return tk.Button(win, text=name_calc, font=('Arial', 15), bg='#AFEEEE', fg='green', command=lambda: calculate())


def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        operation = value[-1]
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Пожалуйста, вводите только цифры')
        calc.insert(0, eval(value))
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя!!!')
        calc.insert(0, eval(value))


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + str(digit))


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+*/':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, '0')


def press_key(event):
    if event.char.isdigit():
        add_digit(digit)
    elif event.char in '+-/*':
        add_operation(operation)
    elif event.char == '\r':
        calculate()


win = tk.Tk()
win.title('Калькулятор')
win.geometry('240x270+500+200')
win['bg'] = '#6495ED'
win.resizable(False, False)

win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

make_digit_button(1).grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button(2).grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button(3).grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button(4).grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button(5).grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button(6).grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button(7).grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button(8).grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button(9).grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button(0).grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_clear_button('C').grid(row=4, column=2, stick='wens', padx=5, pady=5)

make_calculate_button('=').grid(row=4, column=1, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
