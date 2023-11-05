ncases = int(input())

for x in range(ncases):
    tocheck = int(input())
    yesorno = False
    for i in range(11):
        checking = tocheck - 111*i
        if checking % 11 == 0 and checking >= 0:
            yesorno = True
            break
    if yesorno:
        print("YES")
    else:
        print("NO")
