def countTrees(map, right, down):
    count = 0
    for i, row in enumerate(map):
        if i == 0:
            # ignore first row
            pass
        else:
            # only consider 'down' row (dont forget to ignore first row)
            if ((1 + i) % down) == 0:
                # check every 'right' element if its a tree (1) and count
                if row[(i * right) % len(row)] == 1:
                    count += 1
    return count

if __name__ == "__main__":
    map = []

    with open('data.txt','r') as f:
        for line in f:
            row = []
            for element in line:
                if element == '.': #no tree
                    row.append(0)
                elif element == '#': #tree
                    row.append(1)
                else:
                    pass
            map.append(row)

    # part 1
    print(f'Part 1: {countTrees(map, 3, 1)}')

    # part 2
    res = 1
    res *= countTrees(map, 1, 1)
    res *= countTrees(map, 3, 1)
    res *= countTrees(map, 5, 1)
    res *= countTrees(map, 7, 1)
    res *= countTrees(map, 1, 2)
    print(f'Part 2: {res}')
