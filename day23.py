import tkinter as tk


def fibo(n):
    l = [0, 1]

    for _ in range(n - 1):
        l.append(l[len(l) - 1] + l[len(l) - 2])
    return l[n]

def process_fibonacci():
    number = int(en_input_number.get())
    lbl_display_fibonacci_result.config(text = f'fibonacci{[number]} = {fibo(number)}')


if __name__ == '__main__':

    w = tk.Tk() # create window object
    w.title("Fibonacci")
    w.geometry("250x150")

    # create widget
    lbl_display_fibonacci_result = tk.Label(w, text='Fibonacci by memorization')
    en_input_number = tk.Entry(w)
    btn_click = tk.Button(w, text = 'Click',command = process_fibonacci) # bind function

    # layout
    lbl_display_fibonacci_result.pack()
    en_input_number.pack(fill='x')
    btn_click.pack(fill='x')

    en_input_number.focus()
    w.mainloop()

