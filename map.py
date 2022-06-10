import tkinter
from tkinter import *
import constants
import tools
import userInput
from cell import Cell
from resetButton import Reset

TOP_FRAME = 50
global CELLS


class Map:
    settings = Tk()
    settings.configure(bg="gray")
    settings.title("Ustawienia")
    settings.resizable(False, False)
    settings.geometry("400x200")

    btn = Button(settings, text="Zatwierdź", width=15, bd=2, command=settings.quit)
    btn.place(relx=0.5, rely=0.6, anchor=CENTER)

    mapSize = Entry(settings, width=25, bd=3)
    mapSize.place(relx=0.5, rely=0.4, anchor=CENTER)

    minesNumber = Entry(settings, width=25, bd=3)
    minesNumber.place(relx=0.5, rely=0.2, anchor=CENTER)

    mapLabel = Label(settings, height=1, width=30, bd=0, bg='gray', text="Podaj rozmiar mapy (min 8, max 22)")
    mapLabel.place(relx=0.5, rely=0.3, anchor=CENTER)

    minesLabel = Label(settings, height=1, width=25, bd=0, bg='gray', text="Podaj ilosc min")
    minesLabel.place(relx=0.5, rely=0.1, anchor=CENTER)

    settings.mainloop()
    userInput.MINES_NUMBER = int(minesNumber.get())
    userInput.GRID_SIZE = int(mapSize.get())
    CELLS = userInput.GRID_SIZE
    settings.destroy()

    window = Tk()
    window.configure(bg="gray")
    SCREEN_WIDTH = window.winfo_screenwidth()
    SCREEN_HEIGHT = window.winfo_screenheight()
    CENTER_X = int(SCREEN_WIDTH / 2 - (constants.WIDTH * userInput.GRID_SIZE) / 2)
    CENTER_Y = int(SCREEN_HEIGHT / 2 - (constants.HEIGHT * userInput.GRID_SIZE) / 2)
    window.geometry(f'{constants.WIDTH * userInput.GRID_SIZE}x{constants.HEIGHT * userInput.GRID_SIZE + TOP_FRAME}+{CENTER_X}+{CENTER_Y}')
    window.title("Saper")
    window.resizable(False, False)
    smileDefaultImage = PhotoImage

    topFrame = Frame(window, bg='#696969', width=constants.WIDTH * userInput.GRID_SIZE, height=TOP_FRAME)
    topFrame.place(relx=0, rely=0)

    gameFrame = Frame(window, width=constants.WIDTH * userInput.GRID_SIZE, height=(constants.HEIGHT * userInput.GRID_SIZE) - TOP_FRAME)
    gameFrame.place(x=0, y=TOP_FRAME)

    topFrameResetButton = Frame(topFrame, width=constants.WIDTH * userInput.GRID_SIZE // userInput.GRID_SIZE, height=TOP_FRAME)

    if userInput.GRID_SIZE % 2 != 0:
        leftCells = (userInput.GRID_SIZE - 1) / 2
        topFrameResetButton.place(x=(constants.WIDTH * userInput.GRID_SIZE) * (leftCells / userInput.GRID_SIZE), y=3)
        flagFrame = tools.putFrame(0, 0, topFrame, leftCells * constants.CELL_SIZE, TOP_FRAME)
        timerFrame = tools.putFrame((constants.WIDTH * userInput.GRID_SIZE) - leftCells * constants.CELL_SIZE, 0,
                                    topFrame, leftCells * constants.CELL_SIZE, TOP_FRAME)
    else:
        notMiddleCells = (userInput.GRID_SIZE - 2) // 2
        topFrameResetButton.place(x=((constants.WIDTH * userInput.GRID_SIZE) // 2) - constants.MARGIN_BETWEEN_BUTTONS - constants.CELL_SIZE // 2, y=3)
        flagFrame = tools.putFrame(0, 0, topFrame, constants.CELL_SIZE * notMiddleCells, TOP_FRAME)
        timerFrame = tools.putFrame((constants.WIDTH * userInput.GRID_SIZE) - constants.CELL_SIZE * notMiddleCells, 0,
                                    topFrame, constants.CELL_SIZE * notMiddleCells, TOP_FRAME)

    pixel = tkinter.PhotoImage(width=1, height=1)

    smileDefaultImage = PhotoImage(file='smile_default.png')
    reset = Reset(0, 0)
    reset.createResetObject(topFrameResetButton, smileDefaultImage)
    reset.resetButtonObject.grid(
        column=0, row=0
    )

    for x in range(userInput.GRID_SIZE):
        for y in range(userInput.GRID_SIZE):
            cell = Cell(x, y)
            cell.createButtonObject(gameFrame, pixel)
            cell.cellButtonObject.grid(
                column=x, row=y
            )

    Cell.putMines()
    print(userInput.GRID_SIZE)
    print(userInput.MINES_NUMBER)

    Cell.createCellCountLabel(timerFrame)
    Cell.cellCountLabelObj.place(
        x=8, y=8
    )
    window.mainloop()
