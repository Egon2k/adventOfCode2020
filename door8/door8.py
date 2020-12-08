pc = 0
acc = 0

if __name__ == "__main__":
    data = []

    with open('data.txt','r') as f:
        data = f.read()[:-1].split('\n') # [:-1] to cut off the last \n

    alreadyExecuted = [0] * len(data)

    # part 1
    while(alreadyExecuted[pc] == 0):
        instr = data[pc].split()[0].replace(' ','')
        val   = int(data[pc].split()[1].replace(' ',''))

        if alreadyExecuted[pc] == 1:
            break;
        else:
            alreadyExecuted[pc] = 1

            if instr == 'nop':
                pc += 1
            elif instr == 'acc':
                pc += 1
                acc += val
            elif instr == 'jmp':
                pc += val

    print(acc)


