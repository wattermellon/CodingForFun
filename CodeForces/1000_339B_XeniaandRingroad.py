values = input().split(" ")
nhomes = int(values[0])
mtasks = int(values[1])
position = 1
movement = 0
tasks = input().split(" ")
int_task_list = [int(x) for x in tasks]
for i in int_task_list:
    if position < i:
        movement += i - position
    elif position > i:
        movement += i + nhomes - position
    position = i
print(movement)