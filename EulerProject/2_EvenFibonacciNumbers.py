num1 = 1
num2 = 2
evensum = 2
cur = 0
while cur < 4000000:
    cur = num1 + num2
    num1 = num2
    num2 = cur
    if cur%2 == 0:
        evensum += cur
print(evensum)
