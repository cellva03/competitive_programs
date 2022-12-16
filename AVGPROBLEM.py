for _ in range(int(input())):
    x, y, z = map(int,input().split())
    res = float(x+y)
    if res > z:
        print("Yes")
    else:
        print("No")