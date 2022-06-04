from tkinter import Button, Label
import random
import constants


class Cell:
    cells = []
    cellCount = constants.CELL_COUNT
    cellCountLabelObj = None


    def __init__(self, x, y, isMine=False):
        self.isMine = isMine
        self.cellButtonObject = None
        self.x = x
        self.y = y
        self.is_opened = False
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
            if self.surroundingMines==0:
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
            Cell.cellCount-=1
        print(self.surroundingCells)
        self.cellButtonObject.configure(text=self.surroundingMines)
        if Cell.cellCountLabelObj:
            Cell.cellCountLabelObj.configure(text=f"ilość komórek\n{Cell.cellCount}")
        self.is_opened = True

    def showMine(self):
        self.cellButtonObject.configure(bg='red')

    def rightClickAction(event):
        print(event)

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
            font=("",8)
        )
        Cell.cellCountLabelObj = lbl
