arr = []
with open('door1.txt') as f:
    for line in f:
        arr.append(int(line.strip('\n')))
    
for i in range(len(arr)):
    for j in arr[i:]:
        if ((arr[i]+j) == 2020):
            print(arr[i]*j)
