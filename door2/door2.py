partA = 0
partB = 0

with open('door2.txt','r') as f:
    for line in f:
        # part A

        rule = line.split(':')[0]
        password = line.split(':')[1]
        letter = rule[-1]
        quantity = rule.split()[0]
        quantity_low = quantity.split('-')[0]
        quantity_high = quantity.split('-')[1]

        if (password.count(letter) >= int(quantity_low)) and (password.count(letter) <= int(quantity_high)):
            partA += 1

        # part B

        first_pos = int(quantity_low)
        second_pos = int(quantity_high)

        if ((password[first_pos] == letter) and  (password[second_pos] != letter)) or ((password[first_pos] != letter) and  (password[second_pos] == letter)):
            partB += 1


    print(f'Part A: {partA}')
    print(f'Part B: {partB}')