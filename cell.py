from tkinter import Button
import random
import constants

class Cell:
    cells = []
    # konstruktor
    def __init__(self, x, y, isMine=False):
        # na poczatku pole nie jest mina
        self.isMine = isMine
        # na poczatku none by potem cos do niego przypisac
        self.cellButtonObject = None
        self.x = x
        self.y = y
        Cell.cells.append(self)

    # metoda pozwalajaca tworzyc przyciski w wyznaczonym miescu (location)
    def createButtonObject(self, location, pixel):
        button = Button(
            location,
            width=constants.CELL_WIDTH,
            height=constants.CELL_HEIGHT,
            image=pixel,
            bd=2
        )
        # bind - wyswietl po press <Button-1> lewy <Button-3> prawy
        button.bind('<Button-1>', self.leftClickAction)
        button.bind('<Button-3>', self.rightClickAction)
        self.cellButtonObject = button

    def leftClickAction(self, event):
        if self.isMine:
            self.showMine()
        else:
            self.showCell()

    # start here
    def showCell(self):
        print(self.cells)

    def showMine(self):
        # configure zmiena zawartosc
        self.cellButtonObject.configure(bg='red') #jak dodac pnga?

    def rightClickAction(self, event):
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