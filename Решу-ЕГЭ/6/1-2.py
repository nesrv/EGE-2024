
from tkinter import *
root = Tk()

canvas = Canvas(root, width=500, height=500, bg='white')
canvas.pack()

canvas.create_line(0, 0, 50, 50, fill='red')

root.mainloop()


