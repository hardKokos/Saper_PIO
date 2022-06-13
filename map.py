import os
import sys
import tkinter
from tkinter import *
from tkinter import messagebox

import constants
import tools
import userInput
from cell import Cell
from resetButton import Reset
from timer import Timer

TOP_FRAME = 50
global CELLS


class Map:
    window = None
    settings = None

    def initSettings(self):
        self.settings = Tk()
        self.settings.configure(bg="gray")
        self.settings.title("Ustawienia")
        self.settings.resizable(False, False)
        center_width = self.settings.winfo_screenwidth()
        center_height = self.settings.winfo_screenheight()
        center_x = int(center_width / 2 - constants.SETTINGS_WIDTH / 2)
        center_y = int(center_height / 2 - constants.SETTINGS_HEIGHT / 2)
        self.settings.geometry(f'{constants.SETTINGS_WIDTH}x{constants.SETTINGS_HEIGHT}+{center_x}+{center_y}')
        btn = Button(self.settings, text="Zatwierdź", width=15, bd=2, command=self.settings.quit)
        btn.place(relx=0.5, rely=0.6, anchor=CENTER)

        mapSize = Entry(self.settings, width=25, bd=3)
        mapSize.place(relx=0.5, rely=0.4, anchor=CENTER)

        minesNumber = Entry(self.settings, width=25, bd=3)
        minesNumber.place(relx=0.5, rely=0.2, anchor=CENTER)

        mapLabel = Label(self.settings, height=1, width=30, bd=0, bg='gray', text="Podaj rozmiar mapy (min 8, max 16)")
        mapLabel.place(relx=0.5, rely=0.3, anchor=CENTER)

        minesLabel = Label(self.settings, height=1, width=25, bd=0, bg='gray', text="Podaj ilosc min")
        minesLabel.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.settings.mainloop()
        try:
            userInput.MINES_NUMBER = int(minesNumber.get())
            userInput.GRID_SIZE = int(mapSize.get())
            if (userInput.MINES_NUMBER > userInput.GRID_SIZE ** 2) or (userInput.GRID_SIZE < 8) or (userInput.GRID_SIZE > 16):
                messagebox.showinfo('Error', 'Złe wymiary mapy lub za duża ilość min!!!')
                self.settings.destroy()
                os.system('python main.py')
                sys.exit()
            CELLS = userInput.GRID_SIZE
            self.settings.destroy()
            self.initGame()
        except:
            pass

    def initGame(self):
        self.window = Tk()
        self.window.configure(bg="gray")
        SCREEN_WIDTH = self.window.winfo_screenwidth()
        SCREEN_HEIGHT = self.window.winfo_screenheight()
        CENTER_X = int(SCREEN_WIDTH / 2 - (constants.WIDTH * userInput.GRID_SIZE) / 2)
        CENTER_Y = int(SCREEN_HEIGHT / 2 - (constants.HEIGHT * userInput.GRID_SIZE) / 2)
        self.window.geometry(
            f'{constants.WIDTH * userInput.GRID_SIZE}x{constants.HEIGHT * userInput.GRID_SIZE + TOP_FRAME}+{CENTER_X}+{CENTER_Y}')
        self.window.title("Saper")
        self.window.resizable(False, False)
        smileDefaultImage = PhotoImage

        topFrame = Frame(self.window, bg='#696969', width=constants.WIDTH * userInput.GRID_SIZE, height=TOP_FRAME)
        topFrame.place(relx=0, rely=0)

        gameFrame = Frame(self.window, width=constants.WIDTH * userInput.GRID_SIZE,
                          height=(constants.HEIGHT * userInput.GRID_SIZE) - TOP_FRAME)
        gameFrame.place(x=0, y=TOP_FRAME)

        topFrameResetButton = Frame(topFrame, width=constants.WIDTH * userInput.GRID_SIZE // userInput.GRID_SIZE,
                                    height=TOP_FRAME)

        if userInput.GRID_SIZE % 2 != 0:
            leftCells = (userInput.GRID_SIZE - 1) / 2
            topFrameResetButton.place(x=(constants.WIDTH * userInput.GRID_SIZE) * (leftCells / userInput.GRID_SIZE), y=3)
            flagFrame = tools.putFrame(0, 0, topFrame, leftCells * constants.CELL_SIZE, TOP_FRAME)
            timerFrame = tools.putFrame((constants.WIDTH * userInput.GRID_SIZE) - leftCells * constants.CELL_SIZE, 0,
                                        topFrame, leftCells * constants.CELL_SIZE, TOP_FRAME)
        else:
            notMiddleCells = (userInput.GRID_SIZE - 2) // 2
            topFrameResetButton.place(x=((
                                                 constants.WIDTH * userInput.GRID_SIZE) // 2) - constants.MARGIN_BETWEEN_BUTTONS - constants.CELL_SIZE // 2,
                                      y=3)
            flagFrame = tools.putFrame(0, 0, topFrame, constants.CELL_SIZE * notMiddleCells, TOP_FRAME)
            timerFrame = tools.putFrame((constants.WIDTH * userInput.GRID_SIZE) - constants.CELL_SIZE * notMiddleCells, 0,
                                        topFrame, constants.CELL_SIZE * notMiddleCells, TOP_FRAME)

        pixel = tkinter.PhotoImage(width=1, height=1)

        smileDefaultImage = PhotoImage(file='smile_default.png')
        reset = Reset(0, 0)
        reset.createResetObject(topFrameResetButton, smileDefaultImage)
        reset.resetButtonObject.grid(column=0, row=0)
        reset.resetButtonObject.configure(command=self.resetGame)

        for x in range(userInput.GRID_SIZE):
            for y in range(userInput.GRID_SIZE):
                cell = Cell(x, y, userInput.MINES_NUMBER, userInput.GRID_SIZE**2)
                cell.createButtonObject(gameFrame, pixel)
                cell.cellButtonObject.grid(column=x, row=y)

        Cell.putMines()
        Cell.createCellCountLabel(flagFrame, userInput.MINES_NUMBER)
        Cell.cellCountLabelObj.place(x=8, y=8)

        timer = Timer(timerFrame, self.window)
        Cell.setTimer(timer)
        timer.startTimer()

        self.window.mainloop()
        timer.stopTimer()
        try:
            self.window.destroy()
        except:
            pass

    def resetGame(self):
        try:
            self.window.destroy()
        except:
            print('Kaput')
        os.system('python main.py')
        sys.exit()
