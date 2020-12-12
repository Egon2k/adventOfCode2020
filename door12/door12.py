if __name__ == "__main__":
    with open('data.txt','r') as f:
        data = f.read()[:-1].split('\n') # [:-1] to cut off the last \n

    # part 1
    coords = [0,0] # east(+)/west(-), north(+)/south(-)
    dir = 0        # 0 (east), 90 (south), 180 (west), 270 (north)

    for instr in data:

        l = instr[0]
        val = int(instr[1:])

        if  l == 'N':
            coords[1] += val
        elif  l == 'S':
            coords[1] -= val
        elif  l == 'E':
            coords[0] += val
        elif  l == 'W':
            coords[0] -= val
        elif  l == 'R':
            dir += val
            dir %= 360
        elif  l == 'L':
            dir -= val
            dir %= 360
        elif  l == 'F':
            if dir == 0:
                coords[0] += val
            elif dir == 180:
                coords[0] -= val
            elif dir == 90:
                coords[1] -= val
            elif dir == 270:
                coords[1] += val

    print(f'Part 1: {abs(coords[0]) + abs(coords[1])}')
