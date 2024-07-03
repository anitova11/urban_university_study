import tkinter as tk

window = tk.Tk()
window.title('Калькулятор Ксюшки')
window.geometry('320x400')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=4, height=1)
button_add.place(x=100, y=280)
button_sub = tk.Button(window, text='-', width=4, height=1)
button_sub.place(x=190, y=280)
button_div = tk.Button(window, text='/', width=4, height=1)
button_div.place(x=190, y=330)
button_mul = tk.Button(window, text='*', width=4, height=1)
button_mul.place(x=100, y=330)

first_number = tk.Entry(window, width=21)
first_number.place(x=100, y=70)
number1 = tk.Label(window, text='Ваше первое число')
number1.place()

second_number = tk.Entry(window, width=21)
second_number.place(x=100, y=120)
number2 = tk.Label(window, text='Ваше первое число')
number2.place()

answer_text = tk.Entry(window, width=21)
answer_text.place(x=100, y=170)
answer = tk.Label(window, text='Ваше первое число')
answer.place()


window.mainloop()
