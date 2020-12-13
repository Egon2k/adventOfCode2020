if __name__ == "__main__":
    with open('data.txt','r') as f:
        data = f.read()[:-1].split('\n') # [:-1] to cut off the last \n

    timestamp = int(data[0])
    lines = data[1].split(',')
    activeLines = []
    notFound = True
    i = timestamp

    for line in lines:
        if line != 'x':
            activeLines.append(int(line))

    # part 1
    while notFound:
        for activeLine in activeLines:
            if i % activeLine == 0:
                notFound = False
                break
            else:
                i += 1
                
    print(f'Part 1: {activeLine * (i - timestamp)}')

