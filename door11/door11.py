def checkNeighbors(data, row, seat, lastRow, lastSeat):
    neighbors = 0
    fromRow = 0
    toRow = 0
    fromSeat = 0
    toSeat = 0

    if row == 0:
        fromRow = 0
        toRow = row + 2
    elif row == lastRow:
        fromRow = row - 1
        toRow = lastRow
    else:
        fromRow = row - 1
        toRow = row + 2

    if seat == 0:
        fromSeat = 0
        toSeat = seat + 2
    elif seat == lastSeat:
        fromSeat = seat - 1
        toseat = lastSeat
    else:
        fromSeat = seat - 1
        toSeat = seat + 2

    temp = data[fromRow:toRow]


    for line in range(len(temp)):
        neighbors += temp[line][fromSeat:toSeat].count('#')

    if data[row][seat] == '#':
        neighbors -= 1

    return neighbors


if __name__ == "__main__":
    with open('data.txt','r') as f:
        data = f.read()[:-1].split('\n') # [:-1] to cut off the last \n

    for i in range(len(data)):
        data[i] = list(data[i])

    rows = len(data)
    seats = len(data[0])

    # https://stackoverflow.com/a/28684323
    before = [x[:] for x in data]
    after  = [x[:] for x in data]

    changed = True

    while changed:
        changed = False

        before = [x[:] for x in after]

        for i in range(rows):
            for j in range(seats):
                if before[i][j] == '.':
                    continue
                if before[i][j] == 'L' and checkNeighbors(before, i, j, rows, seats) == 0:
                    after[i][j] = '#'
                    changed = True
                if before[i][j] == '#' and checkNeighbors(before, i, j, rows, seats) >= 4:
                    after[i][j] = 'L'
                    changed = True
        print('.', end='')

    part1 = 0
    for i in after:
        part1 += i.count('#')

    print(f'\nPart 1: {part1}')
