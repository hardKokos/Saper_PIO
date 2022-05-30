import tkinter
from tkinter import *
from cell import Cell
import constants
import tools


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
        width=constants.WIDTH - (2*tools.width_percentage(4)),
        height=constants.HEIGHT - tools.height_percentage(15+6+6)
    )
    gameFrame.place(x=0,y=50)

    # grid metoda podobna do place tylko dzieli obiekt w ktorym jest
    # (rodzica) na wiesze i kolumny

    pixel = tkinter.PhotoImage(width=1, height=1)

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
