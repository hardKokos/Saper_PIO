from tkinter import Frame

def putFrame(x, y, parent, width, height):
    frame = Frame(parent, bg="gray", width=width, height=height)
    frame.place(x=x, y=y)
    return frame