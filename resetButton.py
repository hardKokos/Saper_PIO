from tkinter import Button
import random
import constants


class Reset:
    def __init__(self, x, y):
        self.resetButtonObject = None
        self.x = x
        self.y = y

    #obramowka dla przycisku
    def createResetObject(self, location, pixel):
        reset = Button(
            location,
            width=constants.CELL_WIDTH,
            height=constants.CELL_WIDTH,
            image=pixel,
            bd=4,
        )
        self.resetButtonObject = reset
