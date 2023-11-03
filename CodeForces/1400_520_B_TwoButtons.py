import sys
values = input().split(" ")
start = int(values[0])
goal = int(values[1])
moves = 0

if start >= goal:
    print(int (start-goal))
else:
    while True:
        if goal % 2 == 0:
            goal = goal/2
        else:
            goal += 1
        moves += 1
        if start >= goal:
            print(int (moves + start-goal))
            break
