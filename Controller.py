# Запуск модулей

from random import *
from tkinter import *

# GUI программы
root = Tk()
root.geometry('800x600')  # size of the root window

# Счетчик
i = 0
# функция счетчика
def button_count(event):
    global i
    if randint(1,4) ==randint(1,4):
        i = i+1
        counter.config(text="{}".format(i))
        print(i)

# top button
def mouse_motion(event):
    top_button["text"] = "TOP button"


def mouse_leave(event):
    top_button["text"] = "Кликни"


top_button = Button(root, bg='green', width=20, height=4, text='Кликни', activebackground='green2')
top_button.pack(side=TOP, pady=50)
top_button.bind("<Enter>", mouse_motion)
top_button.bind("<Leave>", mouse_leave)
top_button.bind("<Button-1>", button_count)

# bottom button
def mouse_motion(event):
    bottom_button["text"] = "BOTTOM button"


def mouse_leave(event):
    bottom_button["text"] = "Кликни"


bottom_button = Button(root, bg='red', width=20, height=4, text='Кликни', activebackground='red3')
bottom_button.pack(side=BOTTOM, pady=50)
bottom_button.bind("<Enter>", mouse_motion)
bottom_button.bind("<Leave>", mouse_leave)
bottom_button.bind("<Button-1>", button_count)

# right button
def mouse_motion(event):
    right_button["text"] = "RIGHT button"


def mouse_leave(event):
    right_button["text"] = "Кликни"


right_button = Button(root, bg='blue', width=20, height=4, text='Кликни', activebackground='blue3')
right_button.pack(side=RIGHT, padx=50)
right_button.bind("<Enter>", mouse_motion)
right_button.bind("<Leave>", mouse_leave)
right_button.bind("<Button-1>", button_count)

# left button
def mouse_motion(event):
    left_button["text"] = "LEFT button"


def mouse_leave(event):
    left_button["text"] = "Кликни"


left_button = Button(root, bg='purple', width=20, height=4, text='Кликни', activebackground='purple2')
left_button.pack(side=LEFT, padx=50)
left_button.bind("<Enter>", mouse_motion)
left_button.bind("<Leave>", mouse_leave)
left_button.bind("<Button-1>", button_count)

# central label
counter = Label(bg='yellow', width=20, height=4, text="i")
counter.config(text="{}".format(i))
counter.pack(side=BOTTOM, expand=1)

root.mainloop()
