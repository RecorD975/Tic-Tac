from socket import *


def win(table):
    for i in range(len(table)):
        if table[i][0] == table[i][1] == table[i][2] != '*':
            return 1
    for i in range(len(table)):
        if table[0][i] == table[1][i] == table[2][i] != '*':
            return 1
    if table[0][0] == table[1][1] == table[2][2] != '*':
        return 1
    elif table[0][2] == table[1][1] == table[2][0] != '*':
        return 1
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == '*':
                break
            elif i == j == 2 and table[i][j] != '*':
                return -1
        break
    return 0

def print_table(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end=" ")
        print('\n', end='')

server = socket(AF_INET, SOCK_STREAM)
server.bind(("0.0.0.0", 7000))
server.listen(2)
user, address = server.accept()

table = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']
]

print("Привет, ты зашел в игру крестики-нолики, ты будешь играть крестиком 'x'\
\nПеред тобой игровое поле и его координаты\
 соответсвенно\n00 01 02\n10 11 12\n20 21 22")
user.send("Привет, ты зашел в игру крестики-нолики, ты будешь играть ноликом '0'\n\
Перед тобой игровое поле и его координаты соответсвенно\n\
00 01 02\n10 11 12\n20 21 22".encode('utf-8'))
while True:
    print_table(table)
    print("Введите координаты через пробел: ")
    user.send("Ваш соперник делает ход, ждем ...".encode('utf-8'))
    if win(table):
        print("Игра завершена победил '0'")
        user.send("Игра завершена победил '0'".encode('utf-8'))
        break
    while True:
        x, y = map(int, input().split())
        if 0 <= x <= 2 and 0 <= y <= 2:
            if table[x][y] == '*':
                break
            else:
                print("Эта клетка уже занята!")
                print("Введите координаты через пробел: ")
        else:
            print("Неверный формат координат!")
            print("Введите координаты через пробел: ")
    table[x][y] = 'x'
    print_table(table)
    user.send((str(x) + str(y)).encode('utf-8'))
    if win(table):
        print("Игра завершена победил 'x'")
        user.send("Игра завершена победил 'x'".encode('utf-8'))
        break
    elif win(table) == -1:
        print("Ничья")
        user.send("Ничья".encode('utf-8'))
        break
    print("Ваш соперник делает ход, ждем ...")
    user.send("Введите координаты через пробел: ".encode('utf-8'))
    data = user.recv(1024)
    msg = data.decode('utf-8')
    table[int(msg[0])][int(msg[1])] = '0'