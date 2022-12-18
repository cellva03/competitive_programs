for _ in range(int(input())):
    x, y, m = map(int,input().split())
    res = x*m
    if res >= y:
        print("No")
    else:
        print("Yes")