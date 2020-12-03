arr = []
with open('data.txt') as f:
    for line in f:
        arr.append(int(line.strip('\n')))

# part 1
for i in range(len(arr)):
    for j in arr[i+1:]:
        if ((arr[i]+j) == 2020):
            print(f'Part 1: {arr[i]*j}')

# part 2
for i in range(len(arr)):
    for j in range(len(arr[i:])):
        for k in arr[j:]:
            if ((arr[i]+arr[j]+k) == 2020):
                print(f'Part 2: {arr[i]*arr[j]*k}')
                
              
