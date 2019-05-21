from tkinter import *
STEP = 65
def quit(event):
    menu.quit()

menu = Tk()
menu.maxsize(524,524)
menu.minsize(524,524)
canvas = Canvas(menu, width = 524, height = 524)
canvas.pack()

BackGround = PhotoImage(file='png/main1.png')
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

canvas.create_image(1, 1, anchor=NW, image=BackGround)

canvas.create_image(2, 2, anchor=NW, image=wR)
canvas.create_image(2+STEP, 2, anchor=NW, image=wN)
canvas.create_image(2+2*STEP, 2, anchor=NW, image=wB)
canvas.create_image(2+3*STEP, 2, anchor=NW, image=wQ)
canvas.create_image(2+4*STEP, 2, anchor=NW, image=wK)
canvas.create_image(2+5*STEP, 2, anchor=NW, image=wB)
canvas.create_image(2+6*STEP, 2, anchor=NW, image=wN)
canvas.create_image(2+7*STEP, 2, anchor=NW, image=wR)
canvas.create_image(2, STEP*7, anchor=NW, image=bR)
canvas.create_image(2+STEP, 2+STEP*7, anchor=NW, image=bN)
canvas.create_image(2+STEP*2, 2+STEP*7, anchor=NW, image=bB)
canvas.create_image(2+STEP*3, 2+STEP*7, anchor=NW, image=bQ)
canvas.create_image(2+STEP*4, 2+STEP*7, anchor=NW, image=bK)
canvas.create_image(2+STEP*5, 2+STEP*7, anchor=NW, image=bB)
canvas.create_image(2+STEP*6, 2+STEP*7, anchor=NW, image=bN)
canvas.create_image(2+STEP*7, 2+STEP*7, anchor=NW, image=bR)


for i in range(0, 8):
    canvas.create_image(2+STEP*i, STEP, anchor=NW, image=wP)

for i in range(0, 8):
    canvas.create_image(2+STEP*i, STEP*6, anchor=NW, image=bP)
menu.bind("<Escape>", quit)

# photo = PhotoImage(file='main.png')
# BackGround = Label(menu, image = photo)
# BackGround.pack()
#
# Peshka = PhotoImage(file = 'wP.png', width = 60, height =60)
# PS = Label(menu, image = Peshka)
# PS.place(x = 3, y = 3)
menu.mainloop()
