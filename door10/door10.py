def checkDiff(adapters, diff):
    count = 1 # test data showed that I need this xD

    for i in range(len(adapters)):
        if (adapters[i] - adapters[i-1]) == diff:
            count += 1

    return count

if __name__ == "__main__":
    data = []

    with open('data.txt','r') as f:
        data = f.read()[:-1].split('\n') # [:-1] to cut off the last \n

    adapters = list(map(int, data))
    
    adapters.sort()

    # part 1
    print(f'Part 1: {checkDiff(adapters, 1) * checkDiff(adapters, 3)}')

    # part 2
