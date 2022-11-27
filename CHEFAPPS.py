t = int(input())
while t:
    s, x, y, z = map(int,input().split())
    tot = x+y+z
    if s >= tot:
        print(0)
    else:
        if (tot-max(x,y)) <= s:
            print(1)
        else:
            print(2)
    t