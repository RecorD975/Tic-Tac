import function as func
from socket import *
import time


server = socket(AF_INET, SOCK_STREAM)
server.bind(("0.0.0.0", 7000))
server.listen(2)
user1, address = server.accept()
user2, address = server.accept()

table = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']
]

user2.send("Привет, ты зашел в игру крестики-нолики, ты будешь играть крестиком 'x'\
\nПеред тобой игровое поле и его координаты\
 соответсвенно\n00 01 02\n10 11 12\n20 21 22".encode('utf-8'))
user1.send("Привет, ты зашел в игру крестики-нолики, ты будешь играть ноликом '0'\
\nПеред тобой игровое поле и его координаты\
 соответсвенно\n00 01 02\n10 11 12\n20 21 22".encode('utf-8'))
time.sleep(0.5)
while True:
    if func.win(table):
        time.sleep(0.5)
        user2.send("Игра завершена победил '0'".encode('utf-8'))
        user1.send("Игра завершена победил '0'".encode('utf-8'))
        time.sleep(0.5)
        break
    user2.send("Введите координаты через пробел: ".encode('utf-8'))
    user1.send("Ваш соперник делает ход, ждем ...".encode('utf-8'))
    data = user2.recv(1024)
    user1.send(data)
    msg = data.decode('utf-8')
    table[int(msg[0])][int(msg[1])] = 'x'
    print(func.win(table))
    if func.win(table) == 1:
        time.sleep(0.5)
        user2.send("Игра завершена победил 'x'".encode('utf-8'))
        user1.send("Игра завершена победил 'x'".encode('utf-8'))
        time.sleep(0.5)
        break
    elif func.win(table) == -1:
        time.sleep(0.5)
        user2.send("Ничья".encode('utf-8'))
        user1.send("Ничья".encode('utf-8'))
        time.sleep(0.5)
        break
    user2.send("Ваш соперник делает ход, ждем ...".encode('utf-8'))
    user1.send("Введите координаты через пробел: ".encode('utf-8'))
    data = user1.recv(1024)
    user2.send(data)
    msg = data.decode('utf-8')
    table[int(msg[0])][int(msg[1])] = '0'
