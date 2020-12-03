arr = []
with open('door1.txt') as f:
    for line in f:
        arr.append(int(line.strip('\n')))

# part A
for i in range(len(arr)):
    for j in arr[i+1:]:
        if ((arr[i]+j) == 2020):
            print(f'Part A: {arr[i]*j}')

# part B
for i in range(len(arr)):
    for j in range(len(arr[i:])):
        for k in arr[j:]:
            if ((arr[i]+arr[j]+k) == 2020):
                print(f'Part B: {arr[i]*arr[j]*k}')
                
              
