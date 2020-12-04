def createDictFromEntry(entry):
    result = dict()

    entry = entry.replace(' ', '\n')
    entry = entry.split('\n')

    for info in entry:
        result[info[0:3]] = info[4:]

    return result

if __name__ == "__main__":
    data = []
    
    with open('data.txt','r') as f:
        data = f.read().split('\n\n')

    # part 1
    part1 = 0

    reqFields = ['byr','iyr', 'eyr','hgt','hcl','ecl','pid']

    for entry in data:
        required = 0
        for field in reqFields:
            if field in entry:
                required += 1
        if required >= len(reqFields):
            part1 += 1

    print(f'Part 1: {part1}')

    # part 2
    part2 = 0

    for entry in data:
        entryDict = createDictFromEntry(entry)

        valid = 0

        try:
            # byr
            byr = int(entryDict['byr'])
            if byr >= 1920 and byr <= 2002:
                valid += 1

            # iyr
            iyr = int(entryDict['iyr'])
            if iyr >= 2010 and iyr <= 2020:
                valid += 1

            # eyr
            eyr = int(entryDict['eyr'])
            if eyr >= 2020 and eyr <= 2030:
                valid += 1

            # hgt
            hgt = entryDict['hgt']

            if hgt.endswith('cm'):
                if int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193:
                    valid += 1
            elif hgt.endswith('in'):
                if int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76:
                    valid += 1
            else:
                pass

            # hcl
            hcl = entryDict['hcl']
            if hcl.startswith('#') and len(hcl) == 7:
                valid += 1
            #leads to exception when not a valid hex (thx Maik ;) )
            int(hcl[1:], 16)

            #ecl
            ecl = entryDict['ecl']
            if ecl == 'amb' or \
               ecl == 'blu' or \
               ecl == 'brn' or \
               ecl == 'gry' or \
               ecl == 'grn' or \
               ecl == 'hzl' or \
               ecl == 'oth':
                valid += 1

            # pid
            pid = entryDict['pid']
            if pid.isdigit() and len(pid) == 9:
                valid += 1
        except:
            valid = 0


        if valid >= 7:
            part2 += 1

    print(f'Part 2: {part2}')