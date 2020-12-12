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


    #part 2

    coords = [0,0]      # east(+)/west(-), north(+)/south(-)
    waypoint = [10,1]   # east(+)/west(-), north(+)/south(-)   

    for instr in data:

        l = instr[0]
        val = int(instr[1:])

        if  l == 'N':
            waypoint[1] += val
        elif  l == 'S':
            waypoint[1] -= val
        elif  l == 'E':
            waypoint[0] += val
        elif  l == 'W':
            waypoint[0] -= val
        elif  l == 'R':
            temp = waypoint[0]
            if val == 90:
                waypoint[0] = waypoint[1]
                waypoint[1] = -temp
            elif val == 180:
                waypoint[0] = -waypoint[0]
                waypoint[1] = -waypoint[1]
            elif val == 270:
                waypoint[0] = -waypoint[1]
                waypoint[1] = temp
        elif  l == 'L':
            temp = waypoint[0]
            if val == 90:
                waypoint[0] = -waypoint[1]
                waypoint[1] = temp
            elif val == 180:
                waypoint[0] = -waypoint[0]
                waypoint[1] = -waypoint[1]
            elif val == 270:
                waypoint[0] = waypoint[1]
                waypoint[1] = -temp
        elif  l == 'F':
            coords[0] += val * waypoint[0]
            coords[1] += val * waypoint[1]

    print(f'Part 2: {abs(coords[0]) + abs(coords[1])}')
