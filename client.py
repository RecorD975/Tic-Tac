from socket import *


def getmsg():
    data = client.recv(1024)
    msg = data.decode('utf-8')
    print(msg)

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

client = socket(AF_INET, SOCK_STREAM)
client.connect(("0.0.0.0", 7000))

table = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']
]

getmsg()
print_table(table)
while True:
    getmsg()
    data = client.recv(1024)
    msg = data.decode('utf-8')
    table[int(msg[0])][int(msg[1])] = 'x'
    print_table(table)
    getmsg()
    if win(table):
        getmsg()
        break
    elif win(table) == -1:
        getmsg()
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
    table[x][y] = '0'
    client.send((str(x) + str(y)).encode('utf-8'))
    print_table(table)
    if win(table):
        getmsg()
        break