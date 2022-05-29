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
        height=tools.height_percentage(15),
    )
    topFrame.place(x=0,y=0)

    topTopFrame = Frame(
        window,
        bg='black',
        highlightbackground='white',
        highlightthickness=2,
        width=constants.WIDTH,
        height=tools.width_percentage(4)
    )
    topTopFrame.place(x=0,y=tools.height_percentage(15))

    leftFrame = Frame(
        window,
        bg='black',
        highlightbackground='white',
        highlightthickness=2,
        width=tools.width_percentage(4),
        height=tools.height_percentage(85)
    )
    leftFrame.place(x=0,y=tools.height_percentage(15))

    rightFrame = Frame(
        window,
        bg='black',
        highlightbackground='white',
        highlightthickness=2,
        width=tools.width_percentage(4),
        height=tools.height_percentage(85)
    )
    rightFrame.place(x=constants.WIDTH-tools.width_percentage(4),y=tools.height_percentage(15))

    downFrame = Frame(
        window,
        bg='black',
        highlightbackground='white',
        highlightthickness=2,
        width=constants.WIDTH,
        height=tools.width_percentage(4)
    )
    downFrame.place(x=0,y=tools.height_percentage(94))

    gameFrame = Frame(
        window,
        bg='gray', #bez koloru pozniej
        width=constants.WIDTH - (2*tools.width_percentage(4)),
        height=constants.HEIGHT - tools.height_percentage(15+6+6)
    )
    gameFrame.place(x=tools.width_percentage(4),y=tools.height_percentage(21))

    # grid metoda podobna do place tylko dzieli obiekt w ktorym jest
    # (rodzica) na wiesze i kolumny

    for x in range(constants.GRID_SIZE):
        for y in range(constants.GRID_SIZE):
            cell = Cell(x, y)
            cell.createButtonObject(gameFrame)
            cell.cellButtonObject.grid(
                column=x, row=y
            )

    Cell.putMines()

    # Uruchom okno
    window.mainloop()
