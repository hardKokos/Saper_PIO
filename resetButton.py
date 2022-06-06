from tkinter import Button, PhotoImage
import constants


class Reset:
    smileDefaultImage = PhotoImage

    def __init__(self, x, y):
        self.resetButtonObject = None
        self.x = x
        self.y = y

    def createResetObject(self, location, pixel):

        reset = Button(
            location,
            width=constants.CELL_WIDTH,
            height=constants.CELL_WIDTH,
            image=pixel,
            bd=constants.RESET_BUTTON_MARGIN
        )
        self.resetButtonObject = reset
