def checkDirectNeighbors(data, row, seat, lastRow, lastSeat):
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

def checkNeighbors(data, row, seat, lastRow, lastSeat):
    neighbors = 0

    directions = [(-1,-1), #up left
                  (-1, 0), #up
                  (-1, 1), #up right
                  ( 0, 1), #right
                  ( 1, 1), #down right
                  ( 1, 0), #down
                  ( 1,-1), #down left
                  ( 0,-1), #left
                  ]
    
    for direction in directions:
        for i in range(1,min(lastRow,lastSeat)):
            drow  = i * direction[0]
            dseat = i * direction[1]
            
            if (0 <= (row + drow) < lastRow) and (0 <= (seat + dseat) < lastSeat):
                if data[row + drow][seat + dseat] == 'L':
                    break
                elif data[row + drow][seat + dseat] == '#':
                    neighbors += 1
                    break
                elif data[row + drow][seat + dseat] == '.':
                    continue
            
    return neighbors

if __name__ == "__main__":
    with open('data.txt','r') as f:
        data = f.read()[:-1].split('\n') # [:-1] to cut off the last \n

    for i in range(len(data)):
        data[i] = list(data[i])
        
    
    rows = len(data)
    seats = len(data[0])

    # part 1

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
                if before[i][j] == 'L' and checkDirectNeighbors(before, i, j, rows, seats) == 0:
                    after[i][j] = '#'
                    changed = True
                if before[i][j] == '#' and checkDirectNeighbors(before, i, j, rows, seats) >= 4:
                    after[i][j] = 'L'
                    changed = True
        print('.', end='')
    
    part1 = 0
    for i in after:
        part1 += i.count('#')
    
    print(f'\nPart 1: {part1}')

    # part 2
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
                if before[i][j] == '#' and checkNeighbors(before, i, j, rows, seats) >= 5:
                    after[i][j] = 'L'
                    changed = True
    
    part2 = 0
    for i in after:
        part2 += i.count('#')
    
    print(f'\nPart 2: {part2}')