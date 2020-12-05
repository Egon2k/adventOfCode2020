def translateToBinary(string):
    string = string.replace('F', '0')
    string = string.replace('B', '1')
    string = string.replace('L', '0')
    string = string.replace('R', '1')

    return int(string, 2)

if __name__ == "__main__":
    data = []

    with open('data.txt') as f:
        for line in f:
            data.append(line.strip())

    # part 1
    binData = []
    for seat in data:
        # seat code is actually a binary number, so convert into bin
        binData.append(translateToBinary(seat))

    # just max for highest seat ID
    print(f'Part 1: {max(binData)}')

    # part 2
    for i in range(1024):
        # find seat not taken
        if i not in binData:
            # find seat that meets the requirement
            if i + 1 in binData and i - 1 in binData:
                print(f'Part 2: {i}')
