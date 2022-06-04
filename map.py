import tkinter
from tkinter import *
from cell import Cell
import constants
from resetButton import Reset


class Map:
    window = Tk()
    window.configure(bg="gray")
    window.geometry(f'{constants.WIDTH}x'f'{constants.HEIGHT}')
    window.title("Saper")
    window.resizable(False, False)

    topFrame = Frame(
        window,
        bg='#696969',
        width=constants.WIDTH,
        height=constants.TOP_FRAME,
    )
    topFrame.place(x=0, y=0)

    gameFrame = Frame(
        window,
        width=constants.WIDTH,
        height=constants.HEIGHT - constants.TOP_FRAME
    )
    gameFrame.place(x=0, y=constants.TOP_FRAME)

    topFrameResetButton = Frame(
        topFrame,
        width=constants.WIDTH // constants.GRID_SIZE,
        height=constants.TOP_FRAME
    )
    if constants.GRID_SIZE % 2 != 0:
        leftCells = (constants.GRID_SIZE - 1) / 2
        topFrameResetButton.place(x=constants.WIDTH * (leftCells / constants.GRID_SIZE), y=3)

        flagFrame = Frame(
            topFrame,
            bg='gray',
            width=leftCells * constants.CELL_WIDTH,
            height=constants.TOP_FRAME
        )
        flagFrame.place(x=0, y=0)

        timerFrame = Frame(
            topFrame,
            bg='gray',
            width=leftCells * constants.CELL_WIDTH,
            height=constants.TOP_FRAME
        )
        timerFrame.place(x=constants.WIDTH - leftCells * constants.CELL_WIDTH, y=0)
    else:
        topFrameResetButton.place(x=(constants.WIDTH // 2) - constants.MARGIN_BETWEEN_BUTTONS - constants.CELL_WIDTH // 2, y=3)

        notMiddleCells = (constants.GRID_SIZE - 2) // 2
        flagFrame = Frame(
            topFrame,
            bg='gray',
            width=constants.CELL_WIDTH * notMiddleCells,
            height=constants.TOP_FRAME
        )
        flagFrame.place(x=0, y=0)

        timerFrame = Frame(
            topFrame,
            bg='gray',
            width=constants.CELL_WIDTH * notMiddleCells,
            height=constants.TOP_FRAME
        )
        timerFrame.place(x=constants.WIDTH - constants.CELL_WIDTH * notMiddleCells, y=0)

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

    window.mainloop()
