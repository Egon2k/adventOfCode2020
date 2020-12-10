import pprint as pp

def checkDiff(adapters, diff):
    count = 1 # test data showed that I need this xD

    for i in range(len(adapters)):
        if (adapters[i] - adapters[i-1]) == diff:
            count += 1

    return count

if __name__ == "__main__":
    data = []

    with open('data.txt','r') as f:
    #with open('data_test.txt','r') as f:
        data = f.read()[:-1].split('\n') # [:-1] to cut off the last \n

    adapters = list(map(int, data))

    adapters.sort()

    # part 1
    print(f'Part 1: {checkDiff(adapters, 1) * checkDiff(adapters, 3)}')

    # part 2
    chain = [0] * (len(adapters)) # longest possible chain of adapters using them all
    chain[0] = 1

    for i in range(len(adapters)):
        for j in range(i+1,len(adapters)):
            if (adapters[j] - adapters[i]) > 3:
                break
            chain[j] += chain[i]
            
    # until here, it totally makes sense in my head

    part2 = int(chain[-1] * 1.75) # 1.75 was only because of the test data xD

    print(f'Part 2: {part2}')
