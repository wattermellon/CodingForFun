import sys
values = input().split(' ')
strength = int(values[0])
ndrags = int(values[1])
i = 0
arrayarray = []
for number in range(0, ndrags):
    int1, int2 = map(int, input().split())
    arrayarray.append([int1, int2])
sorted_2darray = sorted(arrayarray, key=lambda x: x[0])

for number in range(0, ndrags):
    tobeat = sorted_2darray[number][0]
    reward = sorted_2darray[number][1]
    if tobeat >= strength:
        print("NO")
        sys.exit()
    else:
        strength += reward

print("YES")