from tkinter import *
root.geometry('800x600')  # size of the root window

def move(event):
    #button = Button(root, bg='green', width=20, height=4, activeforeground='gray', activebackground='gray')
    x = event.x
    y = event.y
    s = "Движение мышью {}x{}".format(x, y)
    root.Button(root, bg='green', width=20, height=4, activeforeground='gray', activebackground='gray')


# bottom button
button = Button(root, bg='red', width=20, height=4, text='BOTTOM button')
button.pack(side=BOTTOM, pady=50)
button.bind('<Motion>', move)

root.mainloop()