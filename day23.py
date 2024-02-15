import tkinter as tk


def fibo(n):
    l = [0, 1]

    for _ in range(n - 1):
        l.append(l[len(l) - 1] + l[len(l) - 2])
    return l[n]

w = tk.Tk() # create window object
w.title("Fibonacci")
w.geometry("250x150")

# create widget
lbl_display_fibonacci_result = tk.Label(w, text='Fibonacci by memorization')
en_input_number = tk.Entry(w)
btn_click = tk.Button(w, text = 'Click')

# layout
lbl_display_fibonacci_result.pack()
en_input_number.pack(fill='x')
btn_click.pack(fill='x')

w.mainloop()

