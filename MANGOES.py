for _ in range(int(input())):
    x, y, z = map(int,input().split())
    res = z-y
    print(x//res)
    