from tkinter import Button, Label, messagebox
from tkinter import *
import random
import constants
import sys

class Cell:
    cells = []
    cellCount = constants.CELL_COUNT
    cellCountLabelObj = None
    bombImage = PhotoImage
    flagImage = PhotoImage
    def __init__(self, x, y, isMine=False):
        self.isMine = isMine
        self.cellButtonObject = None
        self.x = x
        self.y = y
        self.is_opened = False
        self.isMineCandidate = False
        Cell.cells.append(self)

    def createButtonObject(self, location, pixel):
        button = Button(
            location,
            width=constants.CELL_WIDTH,
            height=constants.CELL_HEIGHT,
            image=pixel,
            bd=constants.MAP_BUTTON_MARGIN,
            compound='center',
            padx=0,
            pady=0
        )
        # bind - wyswietl po press <Button-1> lewy <Button-3> prawy
        button.bind('<Button-1>', self.leftClickAction)
        button.bind('<Button-3>', self.rightClickAction)
        self.cellButtonObject = button

    def leftClickAction(self, event):
        if self.isMine:
            self.showMine()
        else:
            if self.surroundingMines == 0:
                for cell_obj in self.surroundingCells:
                    cell_obj.showCell()
            self.showCell()

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
        if not self.is_opened:
            Cell.cellCount -= 1
        if self.surroundingMines == 0:
            self.cellButtonObject.configure(bg='gray')
            self.cellButtonObject.configure(state='disabled')
        if self.surroundingMines != 0:
            self.cellButtonObject.configure(text=self.surroundingMines)
        if self.surroundingMines == 1:
            self.cellButtonObject.configure(fg='blue')
        if self.surroundingMines == 2:
            self.cellButtonObject.configure(fg='green')
        if self.surroundingMines == 3:
            self.cellButtonObject.configure(fg='red')
        if Cell.cellCountLabelObj:
            Cell.cellCountLabelObj.configure(text=f"ilość komórek\n{Cell.cellCount}")
        self.is_opened = True


    def showMine(self):
        self.bombImage = PhotoImage(file='mine.png')

        self.cellButtonObject.configure(image = self.bombImage)

        for c in self.cells:
            if c.isMine:
                c.cellButtonObject.configure(image = self.bombImage)
        messagebox.showinfo("Przegrana", "Przegrana!")
        sys.exit()

    def rightClickAction(self, event):
        self.flagImage=PhotoImage(file='kozacka_flaga.png')
        if not self.isMineCandidate:
            self.cellButtonObject.configure(image = self.flagImage)
            self.isMineCandidate = True
        else:
            self.pixel=PhotoImage(width=1, height=1)
            self.cellButtonObject.configure(image=self.pixel)
            self.isMineCandidate = False


    @staticmethod
    def putMines():
        pickedCells = random.sample(
            Cell.cells,
            constants.MINES_NUMBER
        )
        for pickedCells in pickedCells:
            pickedCells.isMine = True

    # wyswietlanie wspolrzenych nie adresow pamieci
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

    @staticmethod
    def createCellCountLabel(location):
        lbl = Label(
            location,
            text=f"ilość komórek\n{Cell.cellCount}",
            font=("", 8)
        )
        Cell.cellCountLabelObj = lbl
