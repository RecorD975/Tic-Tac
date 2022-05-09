table = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
turner = True


def win(table):
    for i in [0, 3, 6]:
        if table[i] == table[i + 1] == table[i + 2] != '*':
            return 1
    for i in [0, 1, 2]:
        if table[i] == table[i + 3] == table[i + 6] != '*':
            return 1
    if table[0] == table[4] == table[8] != '*':
        return 1
    if table[2] == table[4] == table[6] != '*':
        return 1
    if '*' in table:
        return 0
    return -1
