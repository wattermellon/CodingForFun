sum = 0
cur = 1
while cur < 1000:
    if cur % 3 == 0 or cur % 5 == 0:
        sum += cur
    cur += 1

print(sum)