import tkinter
from tkinter import Label
import threading
from time import sleep


class Timer:

    def __init__(self, location, mainWindow):
        self.timerLabel = None
        self.mainWindow = mainWindow
        self.currTime = 0
        self.timerText = tkinter.StringVar()
        self.timerText.set(f"TIME: {self.currTime:03d}")
        self.createTimer(location)
        self.timerOn = False

    def createTimer(self, location):
        lbl = Label(
            location,
            textvariable=self.timerText,
            font=("", 12),
            bg='gray',
            fg='red',
            anchor="center"
        )
        self.timerLabel = lbl
        lbl.place(x=8, y=8)

    def countTime(self):
        while self.timerOn:
            sleep(1)
            try:
                if not self.timerOn:
                    break
                self.currTime += 1
                self.timerText.set(f"TIME: {self.currTime:03d}")
            except:
                return

    def startTimer(self):
        self.timerOn = True
        x = threading.Thread(target=self.countTime)
        x.start()

    def stopTimer(self):
        self.timerOn = False
