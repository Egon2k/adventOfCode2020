part1 = 0
part2 = 0

with open('data.txt','r') as f:
    for line in f:
        # part A

        rule = line.split(':')[0]
        password = line.split(':')[1]
        letter = rule[-1]
        quantity = rule.split()[0]
        quantity_low = quantity.split('-')[0]
        quantity_high = quantity.split('-')[1]

        if (password.count(letter) >= int(quantity_low)) and (password.count(letter) <= int(quantity_high)):
            part1 += 1

        # part B

        first_pos = int(quantity_low)
        second_pos = int(quantity_high)

        if ((password[first_pos] == letter) and  (password[second_pos] != letter)) or ((password[first_pos] != letter) and  (password[second_pos] == letter)):
            part2 += 1


    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')