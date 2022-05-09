import function as func
from socket import *
from tkinter import *
from threading import *
from PIL import Image, ImageTk
from functools import partial
import time

def table_clear():
    for i in range(9):
        func.table[i] = '*'


def endgame():
    user2.send("Хотите начать новую игру?".encode('utf-8'))
    user1.send("Хотите начать новую игру?".encode('utf-8'))
    data2 = user2.recv(1024)
    data1 = user1.recv(1024)
    msg2 = data2.decode('utf-8')
    msg1 = data1.decode('utf-8')
    if msg1 == msg2 == 'Да':
        user2.send("Оба игрока согласились, рестарт ...".encode('utf-8'))
        user1.send("Оба игрока согласились, рестарт ...".encode('utf-8'))
        table_clear()
        time.sleep(3)
        return 1
    else:
        user2.send("Нет согласия от обоих игроков".encode('utf-8'))
        user1.send("Нет согласия от обоих игроков".encode('utf-8'))
        table_clear()
        time.sleep(3)
        return 0


server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 7000))
server.listen(2)
user1, address = server.accept()
user1.send('1'.encode('utf-8'))
user2, address = server.accept()
user2.send('2'.encode('utf-8'))
user2.send("Привет, ты зашел в игру крестики-нолики,\nты будешь играть крестиком 'x'\n".encode('utf-8'))
user1.send("Привет, ты зашел в игру крестики-нолики,\nты будешь играть ноликом '0'\n".encode('utf-8'))
time.sleep(5)
while True:
    user2.send("Ваш ход".encode('utf-8'))
    user1.send("Ваш соперник делает ход, ждем ...".encode('utf-8'))
    data = user2.recv(1024)
    user1.send(data)
    msg = data.decode('utf-8')
    func.table[int(msg)] = 'x'
    if func.win(func.table) == 1:
        time.sleep(0.5)
        user2.send("Игра завершена победил 'x'".encode('utf-8'))
        user1.send("Игра завершена победил 'x'".encode('utf-8'))
        time.sleep(2)
        if endgame() == 1:
            continue
        else:
            break
    elif func.win(func.table) == -1:
        time.sleep(0.5)
        user2.send("Ничья".encode('utf-8'))
        user1.send("Ничья".encode('utf-8'))
        time.sleep(2)
        if endgame() == 1:
            continue
        else:
            break
    user2.send("Ваш соперник делает ход, ждем ...".encode('utf-8'))
    user1.send("Ваш ход".encode('utf-8'))
    data = user1.recv(1024)
    user2.send(data)
    msg = data.decode('utf-8')
    func.table[int(msg)] = '0'
    if func.win(func.table):
        time.sleep(0.5)
        user2.send("Игра завершена победил '0'".encode('utf-8'))
        user1.send("Игра завершена победил '0'".encode('utf-8'))
        time.sleep(2)
        if endgame() == 1:
            continue
        else:
            break
