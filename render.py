from tkinter import *
from config import *

Now = PhotoImage(file='png/now.png')
wP = PhotoImage(file='png/wP.png')
bP = PhotoImage(file='png/bP.png')
wK = PhotoImage(file='png/wK.png')
bK = PhotoImage(file='png/bK.png')
wN = PhotoImage(file='png/wN.png')
bN = PhotoImage(file='png/bN.png')
wB = PhotoImage(file='png/wB.png')
bB = PhotoImage(file='png/bB.png')
wQ = PhotoImage(file='png/wQ.png')
bQ = PhotoImage(file='png/bQ.png')
wR = PhotoImage(file='png/wR.png')
bR = PhotoImage(file='png/bR.png')
BackGround = PhotoImage(file='png/main1.png')


def RenderMap(mp, canvas):
    canvas.delete('all')
    canvas.create_image(1, 1, anchor=NW, image=BackGround)
    for i in range(0, len(mp)):
        for j in range(0, len(mp[i])):
            if mp[i][j] == '1':
                canvas.create_image(2 + STEP * j, 2 + STEP * i, anchor=NW, image=wP)
            elif mp[i][j] == '2':
                canvas.create_image(2 + STEP * j, 2 + STEP * i, anchor=NW, image=wR)
            elif mp[i][j] == '3':
                canvas.create_image(2 + STEP * j, 2 + STEP * i, anchor=NW, image=wN)
            elif mp[i][j] == '4':
                canvas.create_image(2 + STEP * j, 2 + STEP * i, anchor=NW, image=wB)
            elif mp[i][j] == '5':
                canvas.create_image(2 + STEP * j, 2 + STEP * i, anchor=NW, image=wQ)
            elif mp[i][j] == '6':
                canvas.create_image(2 + STEP * j, 2 + STEP * i, anchor=NW, image=wK)
            elif mp[i][j] == 'p':
                canvas.create_image(2 + STEP * j, 2 + STEP * i, anchor=NW, image=bP)
            elif mp[i][j] == 'r':
                canvas.create_image(2 + STEP * j, 2 + STEP * i, anchor=NW, image=bR)
            elif mp[i][j] == 'n':
                canvas.create_image(2 + STEP * j, 2 + STEP * i, anchor=NW, image=bN)
            elif mp[i][j] == 'b':
                canvas.create_image(2 + STEP * j, 2 + STEP * i, anchor=NW, image=bB)
            elif mp[i][j] == 'q':
                canvas.create_image(2 + STEP * j, 2 + STEP * i, anchor=NW, image=bQ)
            elif mp[i][j] == 'k':
                canvas.create_image(2 + STEP * j, 2 + STEP * i, anchor=NW, image=bK)


def OpenMap():
    file = open('map.txt', 'r')
    s = file.read()
    tmp = []
    m = []
    for x in range(0, len(s)):
        if s[x] == '\n':
            m.append(tmp)
            tmp = []
        else:
            tmp.append(s[x])
    return m
