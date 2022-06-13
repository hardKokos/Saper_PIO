from tkinter import messagebox
from tkinter import *
import random
import constants
import userInput
import sys


class Cell:
    cells = []
    cellTimer = None
    cellCount = 0
    mineCount = 0
    flagCount = 0
    correctlyGuessedCount = 0
    cellCountLabelObj = None
    bombImage = PhotoImage
    flagImage = PhotoImage

    def __init__(self, x, y, bombCount, cellCount, isMine=False, flagCount=0, ):
        self.isMine = isMine
        self.cellButtonObject = None
        Cell.cells.append(self)
        self.x = x
        self.y = y
        self.is_opened = False
        self.isFlagged = False
        self.mineCount = bombCount
        self.flagCount = flagCount
        self.cellCount = cellCount

    def createButtonObject(self, location, pixel):
        button = Button(
            location,
            width=constants.CELL_SIZE,
            height=constants.CELL_SIZE,
            image=pixel,
            bd=constants.MAP_BUTTON_MARGIN,
            compound='center',
            padx=0,
            pady=0
        )
        button.bind('<Button-1>', self.leftClickAction)
        button.bind('<Button-3>', self.rightClickAction)
        self.cellButtonObject = button

    def leftClickAction(self, event):
        if self.isFlagged:
            return
        if self.isMine:
            self.showMine()
        else:
            self.showCell()
        self.checkIfWon()

    def getCell(self, x, y):
        for cell in Cell.cells:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surroundingCells(self):
        surroundingCells = [
            self.getCell(self.x - 1, self.y - 1),
            self.getCell(self.x - 1, self.y),
            self.getCell(self.x - 1, self.y + 1),
            self.getCell(self.x, self.y - 1),
            self.getCell(self.x + 1, self.y - 1),
            self.getCell(self.x + 1, self.y),
            self.getCell(self.x + 1, self.y + 1),
            self.getCell(self.x, self.y + 1)
        ]
        surroundingCells = [cell for cell in surroundingCells if cell is not None]
        return surroundingCells

    @property
    def surroundingMines(self):
        amountOfMines = 0
        for cell in self.surroundingCells:
            if cell.isMine:
                amountOfMines += 1
        return amountOfMines

    def showCell(self):
        if self.isMine:
            return
        if not self.is_opened:
            Cell.cellCount -= 1
        self.is_opened = True
        surroundMines = self.surroundingMines
        if surroundMines == 0:
            self.cellButtonObject.configure(bg='gray')
            self.cellButtonObject.configure(state='disabled')
            self.pixel = PhotoImage(width=1, height=1)
            self.cellButtonObject.configure(image=self.pixel)
            for cell in self.surroundingCells:
                if cell.isFlagged:
                    Cell.flagCount -= 1
                    cell.isFlagged = False

                if not cell.isMine and not cell.is_opened:
                    cell.showCell()
        if surroundMines != 0:
            self.cellButtonObject.configure(text=self.surroundingMines)
        if surroundMines == 1:
            self.cellButtonObject.configure(fg='blue')
        elif surroundMines == 2:
            self.cellButtonObject.configure(fg='green')
        elif surroundMines == 3:
            self.cellButtonObject.configure(fg='red')
        self.cellButtonObject.unbind('<Button-1>')
        self.cellButtonObject.unbind('<Button-3>')

    def showMine(self):
        self.bombImage = PhotoImage(file='mine.png')
        self.cellButtonObject.configure(image=self.bombImage)
        for c in self.cells:
            if c.isMine:
                c.cellButtonObject.configure(image=self.bombImage)

        self.cellTimer.stopTimer()
        messagebox.showinfo("Przegrana", "Przegrana!")
        sys.exit()

    def rightClickAction(self, event):
        self.flagImage = PhotoImage(file='kozacka_flaga.png')
        if not self.isFlagged:
            self.cellButtonObject.configure(image=self.flagImage)
            self.isFlagged = True
            Cell.flagCount += 1
            if self.isMine:
                Cell.correctlyGuessedCount += 1
            Cell.cellCountLabelObj.configure(text=f'Ilość flag\n{str(self.mineCount + Cell.mineCount-Cell.flagCount)}')
        else:
            self.pixel = PhotoImage(width=1, height=1)
            self.cellButtonObject.configure(image=self.pixel)
            self.isFlagged = False
            Cell.flagCount -= 1
            if self.isMine:
                Cell.correctlyGuessedCount -= 1
            Cell.cellCountLabelObj.configure(text=f'Ilość flag\n{str(self.mineCount + Cell.mineCount-Cell.flagCount)}')


        self.checkIfWon()

    def checkIfWon(self):
        cellCountState = self.cellCount + Cell.cellCount
        mineCountState = self.mineCount + Cell.mineCount
        flagCountState = Cell.flagCount
        correctGuessState = Cell.correctlyGuessedCount
        #print("CELL:" + str(cellCountState))
        #print("MINE:" + str(mineCountState))
        #print("FLAG:" + str(flagCountState))
        #print("CORRECT:" + str(correctGuessState))
        if cellCountState == mineCountState and correctGuessState == mineCountState and correctGuessState == flagCountState:
            self.cellTimer.stopTimer()
            messagebox.showinfo("Wygrana", "Wygrana!")
            sys.exit()

    @staticmethod
    def putMines():
        pickedCells = random.sample(
            Cell.cells,
            userInput.MINES_NUMBER
        )
        for pickedCells in pickedCells:
            pickedCells.isMine = True

    # wyswietlanie wspolrzenych nie adresow pamieci
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

    @staticmethod
    def createCellCountLabel(location, minesNumber):
        lbl = Label(
            location,
            text=f"Ilość flag\n{minesNumber}",
            font=("", 8)
        )
        Cell.cellCountLabelObj = lbl

    @staticmethod
    def setTimer(timer):
        Cell.cellTimer = timer
