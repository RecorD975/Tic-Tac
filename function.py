def win(table):
    for i in range(len(table)):
        if table[i][0] == table[i][1] == table[i][2] != '*':
            return 1
        elif table[0][i] == table[1][i] == table[2][i] != '*':
            return 1
    if table[0][0] == table[1][1] == table[2][2] != '*':
        return 1
    elif table[0][2] == table[1][1] == table[2][0] != '*':
        return 1
    for i in range(len(table)):
        if '*' in table[i]:
            return 0
    return -1


def print_table(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end=" ")
        print('\n', end='')
