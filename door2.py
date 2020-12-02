count = 0

with open('door2.txt','r') as f:
    for line in f:
        rule = line.split(':')[0]
        password = line.split(':')[1]
        letter = rule[-1]
        quantity = rule.split()[0]
        quantity_low = quantity.split('-')[0]
        quantity_high = quantity.split('-')[1]
        
        if (password.count(letter) >= int(quantity_low)) and (password.count(letter) <= int(quantity_high)):
            count += 1
            
    print(count)