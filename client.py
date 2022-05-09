import function as func
from socket import *
from tkinter import *
from threading import *
from PIL import Image, ImageTk
from functools import partial
import time


def button(j, players_num):
    players_num = int(players_num)
    if players_num == 1:
        btn[j]['image'] = img_o_tk
        func.table[j] = '0'
    else:
        btn[j]['image'] = img_x_tk
        func.table[j] = 'x'
    for k in range(9):
        btn[k]['state'] = 'disabled'
    if players_num == num_of_player:
        client.send(str(j).encode('utf-8'))
        func.turner = False


def answer(str):
    client.send(str.encode('utf-8'))
    yes_button.place_forget()
    no_button.place_forget()


def getmsg():
    msg = client.recv(1024).decode('utf-8')
    title['text'] = msg


def getcoord():
    func.turner = False
    msg = client.recv(1024).decode('utf-8')
    if num_of_player == 1:
        button(int(msg), num_of_player + 1)
    else:
        button(int(msg), num_of_player - 1)


def endgame_check():
    getmsg()
    for i in range(9):
        btn[i]['state'] = 'disabled'
    getmsg()
    yes_button.place(x = 200, y = 100)
    no_button.place(x = 320, y = 100)
    getmsg()


def table_unlock():
    for i in range(9):
        if func.table[i] == '*':
            btn[i]['state'] = 'normal'


def table_clear():
    for i in range(9):
        func.table[i] = '*'
        btn[i]['image'] = pixelVirtual


def gameloop(number):
    getmsg()
    time.sleep(5)
    while True:
        getmsg()
        if number == 1:
            getcoord()
        else:
            table_unlock()
        while func.turner:
            continue 
        func.turner = True
        if func.win(func.table):
            endgame_check()
            if 'Оба' in title['text']:
                table_clear()
                continue
            else:
                table_clear()
                time.sleep(2)
                root.quit()
        getmsg()
        if number == 1:
            table_unlock()
        else:
            getcoord()
        while func.turner:
            continue
        func.turner = True
        if func.win(func.table):
            endgame_check()
            if 'Оба' in title['text']:
                table_clear()
                continue
            else:
                table_clear()
                time.sleep(2)
                root.quit()


root = Tk()
root['bg'] = 'white'
root.title("Tic-Tac")
root.geometry('700x700')
root.resizable(width = False, height = False)

frame = Frame(root, bg = 'white')
frame.place(relx = 0.05, rely = 0.05, relheight = 0.9, relwidth = 0.9)

title = Label(frame, font = 100)
title.pack()

img_x = Image.open('x_blue.jpg')
img_x = img_x.resize((85, 85), Image.ANTIALIAS)
img_x_tk = ImageTk.PhotoImage(img_x)
img_o = Image.open('o_blue.jpg')
img_o = img_o.resize((85, 85), Image.ANTIALIAS)
img_o_tk = ImageTk.PhotoImage(img_o)

img_field = Image.open('game.jpg')
img_field_tk = ImageTk.PhotoImage(img_field)
label_field = Label(frame, image = img_field_tk)
label_field.pack(side = BOTTOM)
pixelVirtual = PhotoImage(width=1, height=1)
yes_button = Button(frame,
                    bg = '#d7d7d7',
                    text = "Да",
                    font = 100,
                    width = 10,
                    height = 1,
                    activebackground = 'gray',
                    command = partial(answer, 'Да'))
no_button = Button(frame,
                    bg = '#d7d7d7',
                    text = "Нет",
                    font = 100,
                    width = 10,
                    height = 1,
                    activebackground = 'gray',
                    command = partial(answer, 'Нет'))


client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 7000))
num_of_player = client.recv(1024).decode('utf-8')
num_of_player = int(num_of_player)
btn = []
for i in range(9):
    btn.append(Button(frame,
                        bg = '#14bdac',
                        image = pixelVirtual,
                        width = 95,
                        height = 95,
                        activebackground = '#116062',
                        relief = 'flat'))
    btn[i]['command'] = partial(button, i, num_of_player)
    if i < 3:
        btn[i].place(x = 153 + i * 110, y = 235)
    elif 3 <= i < 6:
        btn[i].place(x = 153 + (i - 3) * 110, y = 345)
    else:
        btn[i].place(x = 153 + (i - 6) * 110, y = 455)
for i in range(9):
    btn[i]['state'] = 'disabled'
t1 = Thread(target = gameloop, args = (num_of_player,), daemon = True)
t1.start()
root.mainloop()