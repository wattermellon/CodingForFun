import math
numdigits = int(input())
arrstring = input()
arr = [int(element) for element in arrstring]
product = 1
factorialfactors = {2: 0, 3: 0, 5: 0, 7: 0}
divisors = [2, 3, 5, 7]

for digit in arr:
    toadd = math.factorial(digit)
    for divi in reversed(divisors):
        while toadd % math.factorial(divi) == 0:
            factorialfactors[divi] += 1
            toadd /= math.factorial(divi)




finalanswer = []

for x in divisors:
    for j in range(factorialfactors[x]):
        finalanswer.append(x)

finalanswer.reverse()
for x in range(len(finalanswer)):
    print(finalanswer[x], end='')

print()