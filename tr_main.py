import logging
import numpy as np
import math as m
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import Button, BOTH, Tk, ttk, Toplevel, messagebox, Label, Entry
from PIL import ImageTk, Image
logging.basicConfig(level=logging.INFO)

root = Tk()
root.title("Graphene")
root.resizable(width=False, height=False)

# создаем набор вкладок
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text="COS")
tab_control.add(tab2, text="SIN")
tab_control.add(tab3, text="LOG")

tab_control.pack(fill=BOTH, expand=1)


im1 = Image.open("/Users/baddikushai/PycharmProjects/moduless/TASKS/Work_with_MAT/r_app/форкос.jpg")
ph1 = ImageTk.PhotoImage(im1)

im2 = Image.open("/Users/baddikushai/PycharmProjects/moduless/TASKS/Work_with_MAT/r_app/форсин.jpg")
ph2 = ImageTk.PhotoImage(im2)

im3 = Image.open("/Users/baddikushai/PycharmProjects/moduless/TASKS/Work_with_MAT/r_app/форлог.png")
ph3 = ImageTk.PhotoImage(im3)

# создание функций построения графиков
def show_cos():
    w = Toplevel(root)
    w.title("Graphic")
    w.resizable(width=False, height=False)
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=w)
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, pack_toolbar=False)
    toolbar.update()
    toolbar.pack()
    try:
        a = float(cea.get())
        b = float(ceb.get())
        c = float(cec.get())
        d = float(ced.get())
        x = np.arange((-10) * np.pi, 10 * np.pi, 0.01)
        y = a * (np.cos(b * x - c) + d)
        plt.title("y=cos(x)")  # заголовок
        plt.xlabel("x")  # ось абсцисс
        plt.ylabel("y")  # ось ординат
        plt.grid()  # включение отображение сетки
        plt.plot(x, y, "g-.")
    except:
        messagebox.showerror(title="Ошибка", message="Некоректное введенное значение. \nПовторите запрос")
        w.destroy()

def show_sin():
    w = Toplevel(root)
    w.title("Graphic")
    w.resizable(width=False, height=False)
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=w)
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, pack_toolbar=False)
    toolbar.update()
    toolbar.pack()
    try:
        a = float(sea.get())
        b = float(seb.get())
        c = float(sec.get())
        d = float(sed.get())
        x = np.arange((-10) * np.pi, 10 * np.pi, 0.001)
        y = a * (np.sin(b * x - c) + d)
        plt.title("y=sin(x)")  # заголовок
        plt.xlabel("x")  # ось абсцисс
        plt.ylabel("y")  # ось ординат
        plt.grid()  # включение отображение сетки
        plt.plot(x, y, "r--")
    except:
        messagebox.showerror(title="Ошибка", message="Некоректное введенное значение. \nПовторите запрос")
        w.destroy()

def show_log():
    w = Toplevel(root)
    w.title("Graphic")
    w.resizable(width=False, height=False)
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=w)
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, pack_toolbar=False)
    toolbar.update()
    toolbar.pack()
    try:
        a = int(la.get())
        k = int(lk.get())
        x = [i for i in range(1, 500)]
        y = [k * m.log(int(x[i]), a) for i in range(len(x))]
        plt.title("y=log(x)")  # заголовок
        plt.xlabel("x")  # ось абсцисс
        plt.ylabel("y")  # ось ординат
        plt.grid()
        plt.plot(x, y, "b-")
    except:
        messagebox.showerror(title="Ошибка", message="Некоректное введенное значение. \nПовторите запрос")
        w.destroy()



# создание текстовой метки на второй вкладке text='y=a*cos(b*x-c)+d', font=("Arial Bold", 24), fg="#000000", background="#399200")
cos = Label(tab1, image=ph1).grid(row=1, column=1, sticky="N") # создание текстовой метки на первой вкладке , font=("Arial Bold", 20)
lc1 = Label(tab1, text='Коэффициент a:', background="#ffffff", foreground="#000000", font=("Arial Bold", 18)).grid(row=3, sticky="W")
lc2 = Label(tab1, text='Коэффициент b:', background="#ffffff", foreground="#000000", font=("Arial Bold", 18)).grid(row=4, sticky="W")
lc3 = Label(tab1, text='Коэффициент c:', background="#ffffff", foreground="#000000", font=("Arial Bold", 18)).grid(row=5, sticky="W")
lc4 = Label(tab1, text='Коэффициент d:', background="#ffffff", foreground="#000000", font=("Arial Bold", 18)).grid(row=6, sticky="W")

cea = Entry(tab1, width=10, bg="#b8b6b6", fg="#000000", font=("Arial Bold", 18))
ceb = Entry(tab1, width=10, bg="#b8b6b6", fg="#000000", font=("Arial Bold", 18))
cec = Entry(tab1, width=10, bg="#b8b6b6", fg="#000000", font=("Arial Bold", 18))
ced = Entry(tab1, width=10, bg="#b8b6b6", fg="#000000", font=("Arial Bold", 18))

cea.grid(row=3, column=1, sticky="W")
ceb.grid(row=4, column=1, sticky="W")
cec.grid(row=5, column=1, sticky="W")
ced.grid(row=6, column=1, sticky="W")

# создание текстовой метки на первой вкладке , font=("Arial Bold", 20)
s = Label(tab2, image=ph2).grid(row=1, column=1, sticky="N")
ls1 = Label(tab2, text='Коэффициент a:', background="#ffffff", foreground="#000000", font=("Arial Bold", 18)).grid(row=3, sticky="E")
ls2 = Label(tab2, text='Коэффициент b:', background="#ffffff", foreground="#000000", font=("Arial Bold", 18)).grid(row=4, sticky="W")
ls3 = Label(tab2, text='Коэффициент c:', background="#ffffff", foreground="#000000", font=("Arial Bold", 18)).grid(row=5, sticky="W")
ls4 = Label(tab2, text='Коэффициент d:', background="#ffffff", foreground="#000000", font=("Arial Bold", 18)).grid(row=6, sticky="W")

sea = Entry(tab2, width=10, bg="#b8b6b6", fg="#000000", font=("Arial Bold", 18))
seb = Entry(tab2, width=10, bg="#b8b6b6", fg="#000000", font=("Arial Bold", 18))
sec = Entry(tab2, width=10, bg="#b8b6b6", fg="#000000", font=("Arial Bold", 18))
sed = Entry(tab2, width=10, bg="#b8b6b6", fg="#000000", font=("Arial Bold", 18))

sea.grid(row=3, column=1, sticky="W")
seb.grid(row=4, column=1, sticky="W")
sec.grid(row=5, column=1, sticky="W")
sed.grid(row=6, column=1, sticky="W")

l = Label(tab3, image=ph3).grid(row=1, column=1, sticky="W")
ll1 = Label(tab3, text='Введите коэффициент k:', bg="#ffffff", fg="#000000", font=("Arial Bold", 18)).grid(row=3, sticky="W")
ll2 = Label(tab3, text='Основание логарифма a:', bg="#ffffff", fg="#000000", font=("Arial Bold", 18)).grid(row=4, sticky="W")
lk = Entry(tab3, width=10, bg="#b8b6b6", fg="#000000", font=("Arial Bold", 18))
la = Entry(tab3, width=10, bg="#b8b6b6", fg="#000000", font=("Arial Bold", 18))
lk.grid(row=3, column=1, sticky="W")
la.grid(row=4, column=1, sticky="W")

btn1 = Button(tab1, text='Показать график', command=show_cos)
btn1.grid(row=7, column=2, sticky="E")

btn2 = Button(tab2, text='Показать график', command=show_sin)
btn2.grid(row=7, column=2, sticky="E")

btn3 = Button(tab3, text='Показать график', command=show_log)
btn3.grid(row=5, column=2, sticky="N")

if __name__=="__main__":
    root.mainloop()
