import pprint

pc = 0
acc = 0

def replaceInstr(mem,n):
    count = 0
    for line in mem:
        #if 'nop' in line:
        if 'jmp' in line:
            if count == n:
                #line.replace('nop','jmp')
                line.replace('jmp','nop')
            count += 1
    return mem

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

    print(f'Part1 {acc}')

    # part 2
    for i in range(len(data)):
        mem = data[:]
        pc = 0
        acc = 0
        alreadyExecuted = [0] * len(mem)

        if "jmp" in mem[i]:
            mem[i] = mem[i].replace("jmp", "nop")
        elif "nop" in mem[i]:
            mem[i] = mem[i].replace("nop", "jmp")
        else:
            continue

        try:
            while(0 <= pc <= len(mem) and alreadyExecuted[pc] == 0):
                instr = mem[pc].split()[0].replace(' ','')
                val   = int(mem[pc].split()[1].replace(' ',''))

                if alreadyExecuted[pc] == 1 :
                    break
                else:
                    alreadyExecuted[pc] = 1

                    if instr == 'nop':
                        pc += 1
                    elif instr == 'acc':
                        pc += 1
                        acc += val
                    elif instr == 'jmp':
                        pc += val

            if pc >= len(mem):
                break
        except:
            break

    print(f'Part2 {acc}')


