if __name__ == "__main__":
    data = []

    with open('data.txt','r') as f:
        data = f.read()[:-1].split('\n\n') # [:-1] to cut off the last \n

    # part 1
    part1 = 0
    for group in data:
        groupcount = 0
        for i in range(97, 123): # ascii for a-z
            if chr(i) in group:
                groupcount += 1
        part1 += groupcount

    print(f'Part 1: {part1}')


    # part 2
    part2 = 0
    for group in data:
        alphabet = [1] * 26

        for answer in group.split('\n'):
            for i in range(97, 123): # ascii for a-z
                if chr(i) in answer:
                    alphabet[i - 97] *= 1
                else:
                    alphabet[i - 97] *= 0

        # count the ones
        part2 += alphabet.count(1)


    print(f'Part 2: {part2}')
