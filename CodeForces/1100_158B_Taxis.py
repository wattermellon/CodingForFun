import math

ngroups = int(input())
friends = input().split(" ")
int_friends_list = [int(x) for x in friends]
counts = [0] * 5
ntaxis = 0
for x in int_friends_list:
    counts[x] += 1
ntaxis += counts[4]
ntaxis += counts[3]
if counts[1] >= counts[3]:
    counts[1] -= counts[3]
else:
    counts[1] = 0
ntaxis += counts[2]//2
if counts[2] % 2 == 1:
    counts[1] += 2
ntaxis += math.ceil(counts[1]/4)
print(ntaxis)