from tkinter import *

menu = Tk()
menu.title('Chess by Shamil')
menu.maxsize(524, 524)
menu.minsize(524, 524)
canvas = Canvas(menu, width=524, height=524)
canvas.pack()

from render import *

map = OpenMap()
RenderMap(map, canvas)


def Check(event):
    global FLAG
    global map
    DX, DY = event.x, event.y
    j, i = int((DX - 2) / STEP), int((DY - 2) / STEP)
    global CHANGE
    if FLAG == True:
        FLAG = False
        CHANGE = map[i][j]

        if CHANGE == '1' and i == 1:
            canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
            if map[i + 1][j] == '0':
                canvas.create_image(3 + STEP * j, 3 + STEP * (i + 1), anchor=NW, image=Now)
                if map[i + 2][j] == '0':
                    canvas.create_image(3 + STEP * j, 3 + STEP * (i + 2), anchor=NW, image=Now)
        elif CHANGE == '1':
            canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
            if j < 7 and i < 7:
                if map[i + 1][j + 1] == 'p' or map[i + 1][j + 1] == 'r' or map[i + 1][j + 1] == 'n' or map[i + 1][
                    j + 1] == 'b' or map[i + 1][j + 1] == 'q' or map[i + 1][j + 1] == 'k':
                    canvas.create_image(3 + STEP * (j + 1), 3 + STEP * (i + 1), anchor=NW, image=Now)
            if j > 0 and i < 7:
                if map[i + 1][j - 1] == 'p' or map[i + 1][j - 1] == 'r' or map[i + 1][j - 1] == 'n' or map[i + 1][
                    j - 1] == 'b' or map[i + 1][j - 1] == 'q' or map[i + 1][j - 1] == 'k':
                    canvas.create_image(3 + STEP * (j - 1), 3 + STEP * (i + 1), anchor=NW, image=Now)
            if i < 7:
                if map[i + 1][j] == '0':
                    canvas.create_image(3 + STEP * j, 3 + STEP * (i + 1), anchor=NW, image=Now)
        elif CHANGE == '2':
            canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
            for I in range(i + 1, len(map)):
                if map[I][j] == '0':
                    canvas.create_image(3 + STEP * j, 3 + STEP * I, anchor=NW, image=Now)
                elif map[I][j] == 'p' or map[I][j] == 'r' or map[I][j] == 'n' or map[I][j] == 'b' or map[I][j] == 'q' or \
                        map[I][j] == 'k':
                    canvas.create_image(3 + STEP * j, 3 + STEP * I, anchor=NW, image=Now)
                    break
                elif map[I][j] != '0':
                    break
            for J in range(j + 1, len(map)):
                if map[i][J] == '0':
                    canvas.create_image(3 + STEP * J, 3 + STEP * i, anchor=NW, image=Now)
                elif map[i][J] == 'p' or map[i][J] == 'r' or map[i][J] == 'n' or map[i][J] == 'b' or map[i][J] == 'q' or \
                        map[i][J] == 'k':
                    canvas.create_image(3 + STEP * J, 3 + STEP * i, anchor=NW, image=Now)
                    break
                elif map[i][J] != '0':
                    break
            for I in range(i - 1, -1, -1):
                if map[I][j] == '0':
                    canvas.create_image(3 + STEP * j, 3 + STEP * I, anchor=NW, image=Now)
                elif map[I][j] == 'p' or map[I][j] == 'r' or map[I][j] == 'n' or map[I][j] == 'b' or map[I][j] == 'q' or \
                        map[I][j] == 'k':
                    canvas.create_image(3 + STEP * j, 3 + STEP * I, anchor=NW, image=Now)
                    break
                elif map[I][j] != '0':
                    break
            for J in range(j - 1, -1, -1):
                if map[i][J] == '0':
                    canvas.create_image(3 + STEP * J, 3 + STEP * i, anchor=NW, image=Now)
                elif map[i][J] == 'p' or map[i][J] == 'r' or map[i][J] == 'n' or map[i][J] == 'b' or map[i][J] == 'q' or \
                        map[i][J] == 'k':
                    canvas.create_image(3 + STEP * J, 3 + STEP * i, anchor=NW, image=Now)
                    break
                elif map[i][J] != '0':
                    break
        elif CHANGE == '3':
            canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
            if j < 6 and i < 7:
                if map[i + 1][j + 2] == '0' or map[i + 1][j + 2] == 'p' or map[i + 1][j + 2] == 'r' or map[i + 1][
                    j + 2] == 'n' or map[i + 1][j + 2] == 'b' or map[i + 1][j + 2] == 'q' or map[i + 1][j + 2] == 'k':
                    canvas.create_image(3 + STEP * (j + 2), 3 + STEP * (i + 1), anchor=NW, image=Now)  # право вниз
            if j < 6 and i > 0:
                if map[i - 1][j + 2] == '0' or map[i - 1][j + 2] == 'p' or map[i - 1][j + 2] == 'r' or map[i - 1][
                    j + 2] == 'n' or map[i - 1][j + 2] == 'b' or map[i - 1][j + 2] == 'q' or map[i - 1][j + 2] == 'k':
                    canvas.create_image(3 + STEP * (j + 2), 3 + STEP * (i - 1), anchor=NW, image=Now)  # право верх
            if j < 7 and i < 6:
                if map[i + 2][j + 1] == '0' or map[i + 2][j + 1] == 'p' or map[i + 2][j + 1] == 'r' or map[i + 2][
                    j + 1] == 'n' or map[i + 2][j + 1] == 'b' or map[i + 2][j + 1] == 'q' or map[i + 2][j + 1] == 'k':
                    canvas.create_image(3 + STEP * (j + 1), 3 + STEP * (i + 2), anchor=NW, image=Now)  # вниз право
            if j > 0 and i < 6:
                if map[i + 2][j - 1] == '0' or map[i + 2][j - 1] == 'p' or map[i + 2][j - 1] == 'r' or map[i + 2][
                    j - 1] == 'n' or map[i + 2][j - 1] == 'b' or map[i + 2][j - 1] == 'q' or map[i + 2][j - 1] == 'k':
                    canvas.create_image(3 + STEP * (j - 1), 3 + STEP * (i + 2), anchor=NW, image=Now)  # вниз лево
            if j > 1 and i < 7:
                if map[i + 1][j - 2] == '0' or map[i + 1][j - 2] == 'p' or map[i + 1][j - 2] == 'r' or map[i + 1][
                    j - 2] == 'n' or map[i + 1][j - 2] == 'b' or map[i + 1][j - 2] == 'q' or map[i + 1][j - 2] == 'k':
                    canvas.create_image(3 + STEP * (j - 2), 3 + STEP * (i + 1), anchor=NW, image=Now)  # лево низ
            if j > 1 and i > 0:
                if map[i - 1][j - 2] == '0' or map[i - 1][j - 2] == 'p' or map[i - 1][j - 2] == 'r' or map[i - 1][
                    j - 2] == 'n' or map[i - 1][j - 2] == 'b' or map[i - 1][j - 2] == 'q' or map[i - 1][j - 2] == 'k':
                    canvas.create_image(3 + STEP * (j - 2), 3 + STEP * (i - 1), anchor=NW, image=Now)  # лево верх
            if j > 0 and i > 1:
                if map[i - 2][j - 1] == '0' or map[i - 2][j - 1] == 'p' or map[i - 2][j - 1] == 'r' or map[i - 2][
                    j - 1] == 'n' or map[i - 2][j - 1] == 'b' or map[i - 2][j - 1] == 'q' or map[i - 2][j - 1] == 'k':
                    canvas.create_image(3 + STEP * (j - 1), 3 + STEP * (i - 2), anchor=NW, image=Now)  # верх лево
            if j < 7 and i > 1:
                if map[i - 2][j + 1] == '0' or map[i - 2][j + 1] == 'p' or map[i - 2][j + 1] == 'r' or map[i - 2][
                    j + 1] == 'n' or map[i - 2][j + 1] == 'b' or map[i - 2][j + 1] == 'q' or map[i - 2][j + 1] == 'k':
                    canvas.create_image(3 + STEP * (j + 1), 3 + STEP * (i - 2), anchor=NW, image=Now)  # верх право
        # elif CHANGE == '4':
        #     canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
        #     check = True
        #     for I in range(i, len(map)):
        #         for J in range(j, len(map[i])):
        #             if I == J:
        #                 if map[I][J] == '0':
        #                     canvas.create_image(3 + STEP * (J+j), 3 + STEP * (I+i), anchor=NW, image=Now)
        #                 elif map[I][J] == 'p' or map[I][J] == 'r' or map[I][J] == 'n' or map[I][J] == 'b' or map[I][J] == 'q' or map[I][J] == 'k':
        #                     canvas.create_image(3 + STEP * (J+j), 3 + STEP * (I+i), anchor=NW, image=Now)
        #                     check = False
        #                     break
        #                 else:
        #                     check = False
        #                     break
        #         if check == False:
        #             check = True
        #             break
        #     for I in range(i, len(map)):
        #         for J in range(j, -1, -1):
        #             if I == J:
        #                 if map[I][J] == '0' or map[I][J] == 'p' or map[I][J] == 'r' or map[I][J] == 'n' or map[I][J] == 'b' or map[I][J] == 'q' or map[I][J] == 'k':
        #                     canvas.create_image(3 + STEP * J, 3 + STEP * I, anchor=NW, image=Now)
        #                 else:
        #                     break
        #     for I in range(i, -1, -1):
        #         for J in range(j, len(map[i])):
        #             if I == J:
        #                 if map[I][J] == '0' or map[I][J] == 'p' or map[I][J] == 'r' or map[I][J] == 'n' or map[I][J] == 'b' or map[I][J] == 'q' or map[I][J] == 'k':
        #                     canvas.create_image(3 + STEP * J, 3 + STEP * I, anchor=NW, image=Now)
        #                 else:
        #                     break
        #     for I in range(i, -1, -1):
        #         for J in range(j, -1, -1):
        #             if I == J:
        #                 if map[I][J] == '0' or map[I][J] == 'p' or map[I][J] == 'r' or map[I][J] == 'n' or map[I][J] == 'b' or map[I][J] == 'q' or map[I][J] == 'k':
        #                     canvas.create_image(3 + STEP * J, 3 + STEP * I, anchor=NW, image=Now)
        #                 else:
        #                     break
        elif CHANGE == '5':
            canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
            canvas.create_image(3 + STEP * j, 3 + STEP * (i + 1), anchor=NW, image=Now)
            canvas.create_image(3 + STEP * j, 3 + STEP * (i + 2), anchor=NW, image=Now)
        elif CHANGE == '6':
            canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
            canvas.create_image(3 + STEP * j, 3 + STEP * (i + 1), anchor=NW, image=Now)
            canvas.create_image(3 + STEP * j, 3 + STEP * (i + 2), anchor=NW, image=Now)
        elif CHANGE == 'p' and i == 6:
            canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
            if map[i - 1][j] == '0':
                canvas.create_image(3 + STEP * j, 3 + STEP * (i - 1), anchor=NW, image=Now)
                if map[i - 2][j] == '0':
                    canvas.create_image(3 + STEP * j, 3 + STEP * (i - 2), anchor=NW, image=Now)
        elif CHANGE == 'p':
            canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
            if j < 7 and i > 0:
                if map[i - 1][j + 1] == '1' or map[i - 1][j + 1] == '2' or map[i - 1][j + 1] == '3' or map[i - 1][
                    j + 1] == '4' or map[i - 1][j + 1] == '5' or map[i - 1][j + 1] == '6':
                    canvas.create_image(3 + STEP * (j + 1), 3 + STEP * (i - 1), anchor=NW, image=Now)
            if j > 0 and i > 0:
                if map[i - 1][j - 1] == '1' or map[i - 1][j - 1] == '2' or map[i - 1][j - 1] == '3' or map[i - 1][
                    j - 1] == '4' or map[i - 1][j - 1] == '5' or map[i - 1][j - 1] == '6':
                    canvas.create_image(3 + STEP * (j - 1), 3 + STEP * (i - 1), anchor=NW, image=Now)
            if i > 0:
                if map[i - 1][j] == '0':
                    canvas.create_image(3 + STEP * j, 3 + STEP * (i - 1), anchor=NW, image=Now)
        elif CHANGE == 'r':
            canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
            for I in range(i + 1, len(map)):
                if map[I][j] == '0':
                    canvas.create_image(3 + STEP * j, 3 + STEP * I, anchor=NW, image=Now)
                elif map[I][j] == '1' or map[I][j] == '2' or map[I][j] == '3' or map[I][j] == '4' or map[I][j] == '5' or \
                        map[I][j] == '6':
                    canvas.create_image(3 + STEP * j, 3 + STEP * I, anchor=NW, image=Now)
                    break
                elif map[I][j] != '0':
                    break
            for J in range(j + 1, len(map)):
                if map[i][J] == '0':
                    canvas.create_image(3 + STEP * J, 3 + STEP * i, anchor=NW, image=Now)
                elif map[i][J] == '1' or map[i][J] == '2' or map[i][J] == '3' or map[i][J] == '4' or map[i][J] == '5' or \
                        map[i][J] == '6':
                    canvas.create_image(3 + STEP * J, 3 + STEP * i, anchor=NW, image=Now)
                    break
                elif map[i][J] != '0':
                    break
            for I in range(i - 1, -1, -1):
                if map[I][j] == '0':
                    canvas.create_image(3 + STEP * j, 3 + STEP * I, anchor=NW, image=Now)
                elif map[I][j] == '1' or map[I][j] == '2' or map[I][j] == '3' or map[I][j] == '4' or map[I][j] == '5' or \
                        map[I][j] == '6':
                    canvas.create_image(3 + STEP * j, 3 + STEP * I, anchor=NW, image=Now)
                    break
                elif map[I][j] != '0':
                    break
            for J in range(j - 1, -1, -1):
                if map[i][J] == '0':
                    canvas.create_image(3 + STEP * J, 3 + STEP * i, anchor=NW, image=Now)
                elif map[i][J] == '1' or map[i][J] == '2' or map[i][J] == '3' or map[i][J] == '4' or map[i][J] == '5' or \
                        map[i][J] == '6':
                    canvas.create_image(3 + STEP * J, 3 + STEP * i, anchor=NW, image=Now)
                    break
                elif map[i][J] != '0':
                    break
        elif CHANGE == 'n':
            canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
            if j < 6 and i < 7:
                if map[i + 1][j + 2] == '0' or map[i + 1][j + 2] == '1' or map[i + 1][j + 2] == '2' or map[i + 1][
                    j + 2] == '3' or map[i + 1][j + 2] == '4' or map[i + 1][j + 2] == '5' or map[i + 1][j + 2] == '6':
                    canvas.create_image(3 + STEP * (j + 2), 3 + STEP * (i + 1), anchor=NW, image=Now)  # право вниз
            if j < 6 and i > 0:
                if map[i - 1][j + 2] == '0' or map[i - 1][j + 2] == '1' or map[i - 1][j + 2] == '2' or map[i - 1][
                    j + 2] == '3' or map[i - 1][j + 2] == '4' or map[i - 1][j + 2] == '5' or map[i - 1][j + 2] == '6':
                    canvas.create_image(3 + STEP * (j + 2), 3 + STEP * (i - 1), anchor=NW, image=Now)  # право верх
            if j < 7 and i < 6:
                if map[i + 2][j + 1] == '0' or map[i + 2][j + 1] == '1' or map[i + 2][j + 1] == '2' or map[i + 2][
                    j + 1] == '3' or map[i + 2][j + 1] == '4' or map[i + 2][j + 1] == '5' or map[i + 2][j + 1] == '6':
                    canvas.create_image(3 + STEP * (j + 1), 3 + STEP * (i + 2), anchor=NW, image=Now)  # вниз право
            if j > 0 and i < 6:
                if map[i + 2][j - 1] == '0' or map[i + 2][j - 1] == '1' or map[i + 2][j - 1] == '2' or map[i + 2][
                    j - 1] == '3' or map[i + 2][j - 1] == '4' or map[i + 2][j - 1] == '5' or map[i + 2][j - 1] == '6':
                    canvas.create_image(3 + STEP * (j - 1), 3 + STEP * (i + 2), anchor=NW, image=Now)  # вниз лево
            if j > 1 and i < 7:
                if map[i + 1][j - 2] == '0' or map[i + 1][j - 2] == '1' or map[i + 1][j - 2] == '2' or map[i + 1][
                    j - 2] == '3' or map[i + 1][j - 2] == '4' or map[i + 1][j - 2] == '5' or map[i + 1][j - 2] == '6':
                    canvas.create_image(3 + STEP * (j - 2), 3 + STEP * (i + 1), anchor=NW, image=Now)  # лево низ
            if j > 1 and i > 0:
                if map[i - 1][j - 2] == '0' or map[i - 1][j - 2] == '1' or map[i - 1][j - 2] == '2' or map[i - 1][
                    j - 2] == '3' or map[i - 1][j - 2] == '4' or map[i - 1][j - 2] == '5' or map[i - 1][j - 2] == '6':
                    canvas.create_image(3 + STEP * (j - 2), 3 + STEP * (i - 1), anchor=NW, image=Now)  # лево верх
            if j > 0 and i > 1:
                if map[i - 2][j - 1] == '0' or map[i - 2][j - 1] == '1' or map[i - 2][j - 1] == '2' or map[i - 2][
                    j - 1] == '3' or map[i - 2][j - 1] == '4' or map[i - 2][j - 1] == '5' or map[i - 2][j - 1] == '6':
                    canvas.create_image(3 + STEP * (j - 1), 3 + STEP * (i - 2), anchor=NW, image=Now)  # верх лево
            if j < 7 and i > 1:
                if map[i - 2][j + 1] == '0' or map[i - 2][j + 1] == '1' or map[i - 2][j + 1] == '2' or map[i - 2][
                    j + 1] == '3' or map[i - 2][j + 1] == '4' or map[i - 2][j + 1] == '5' or map[i - 2][j + 1] == '6':
                    canvas.create_image(3 + STEP * (j + 1), 3 + STEP * (i - 2), anchor=NW, image=Now)  # верх право
        elif CHANGE == 'b':
            canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
            canvas.create_image(3 + STEP * j, 3 + STEP * (i + 1), anchor=NW, image=Now)
            canvas.create_image(3 + STEP * j, 3 + STEP * (i + 2), anchor=NW, image=Now)
        elif CHANGE == 'q':
            canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
            canvas.create_image(3 + STEP * j, 3 + STEP * (i + 1), anchor=NW, image=Now)
            canvas.create_image(3 + STEP * j, 3 + STEP * (i + 2), anchor=NW, image=Now)
        elif CHANGE == 'k':
            canvas.create_image(3 + STEP * j, 3 + STEP * i, anchor=NW, image=Now)
            canvas.create_image(3 + STEP * j, 3 + STEP * (i + 1), anchor=NW, image=Now)
            canvas.create_image(3 + STEP * j, 3 + STEP * (i + 2), anchor=NW, image=Now)
        elif CHANGE == '0':
            FLAG = True
        menu.update()
        map[i][j] = '0'
        menu.bind("<Button-1>", Check)
    elif FLAG == False:
        FLAG = True
        map[i][j] = CHANGE
        RenderMap(map, canvas)


def Quit(event):
    menu.quit()


menu.bind("<Escape>", Quit)
menu.bind("<Button-1>", Check)
menu.mainloop()
