import tkinter
from tkinter import *
from cell import Cell
import constants
import tools
from resetButton import Reset


class Map:
    # stworzenie okna
    window = Tk()

    # ustawienie koloru tla
    window.configure(bg="gray")
    # wymiary mapy
    window.geometry(f'{constants.WIDTH}x'f'{constants.HEIGHT}')
    # tytul mapy
    window.title("Saper")
    # zabrania powiekszac mape
    window.resizable(False,False)

    # Fragment gdzie znajdzie sie licznik czasu, ilosc flag itd...
    topFrame = Frame(
        window,
        bg='#696969',
        width=constants.WIDTH,
        height=constants.TOP_FRAME,
    )
    topFrame.place(x=0,y=0)

    gameFrame = Frame(
        window,
        bg='green', #bez koloru pozniej
        width=constants.WIDTH,
        height=constants.HEIGHT - constants.TOP_FRAME
    )
    gameFrame.place(x=0, y=constants.TOP_FRAME)

    # grid metoda podobna do place tylko dzieli obiekt w ktorym jest
    # (rodzica) na wiesze i kolumny

    topFrameResetButton = Frame(
        topFrame,
        width=constants.WIDTH // constants.GRID_SIZE,
        height=constants.TOP_FRAME
    )
    if constants.GRID_SIZE % 2 != 0:
        leftCells = (constants.GRID_SIZE - 1) / 2
        topFrameResetButton.place(x=constants.WIDTH * (leftCells / constants.GRID_SIZE), y=3)
    else:
        topFrameResetButton.place(
            x=(constants.WIDTH // 2) - constants.MARGIN_BETWEEN_BUTTONS - constants.CELL_WIDTH // 2, y=3)

    pixel = tkinter.PhotoImage(width=1, height=1)

    reset = Reset(0, 0)
    reset.createResetObject(topFrameResetButton, pixel)
    reset.resetButtonObject.grid(
        column=0, row=0
    )

    for x in range(constants.GRID_SIZE):
        for y in range(constants.GRID_SIZE):
            cell = Cell(x, y)
            cell.createButtonObject(gameFrame, pixel)
            cell.cellButtonObject.grid(
                column=x, row=y
            )

    Cell.putMines()

    # Uruchom okno
    window.mainloop()
