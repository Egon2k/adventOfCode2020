from sympy.ntheory.modular import solve_congruence

def check(lines, val):
    for i in range(1,len(lines)):
        if lines[i] != 'x':
            if (val+i) % lines[i] != 0:
                return False
    return True       

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

    # part 2
    ai = []
    mi = []
    
    # https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.modular.solve_congruence
    for i in range(len(lines)):
        if lines[i] != 'x':
            ai.append(int(lines[i]))
            mi.append(-i)
    
    part2 = solve_congruence(*zip(mi, ai))
    
    print(f'Part 2: {part2[0]}')
    