from socket import *
import function as func


def getmsg():
    data = client.recv(1024)
    msg = data.decode('utf-8')
    return msg


client = socket(AF_INET, SOCK_STREAM)
client.connect(("0.0.0.0", 7000))

table = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']
]

print(getmsg())
func.print_table(table)
while True:
    print(getmsg())
    msg = getmsg()
    table[int(msg[0])][int(msg[1])] = 'x'
    func.print_table(table)
    if func.win(table) != 0:
        print(getmsg())
        break
    print(getmsg())
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
    func.print_table(table)
    if func.win(table) != 0:
        print(getmsg())
        break
