for _ in range(int(input())):
    x, y = map(int,input().split())
    res = x*(1.07)
    if y <= res :
        print("Yes")
    else:
        print("no")