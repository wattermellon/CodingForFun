ncases = int(input())
for i in range(ncases):
    values = input().split(" ")
    arrlength = int(values[0])
    sublength = int(values[1])
    arrstring = input().split(" ")
    arr = [int(element) for element in arrstring]
    myset = set(arr)
    maxsubsum = sum(myset)  

    if(len(myset) > sublength):
        print("-1")
        continue

    if arrlength == sublength:
        print(arrlength)
        for i in range(len(arr)):
            if i == len(arr) - 1:
                print(arr[i], end='')
            else:
                print(arr[i], end=' ')
        print()
        continue

    printable = sorted(list(myset))
    if len(myset) < sublength:
        for j in range(sublength - len(myset)):
            printable.append(min(myset))

    print(arrlength*sublength)
    for x in range(arrlength):
        for i in range(len(printable)):
            if x == arrlength - 1 and i == len(printable) - 1:
                print(printable[i], end='')
            else:
                print(printable[i], end=' ')
    print()
        




