for _ in range(int(input())):
    x, y, z = map(int,input().split())
    l =[x,y,z]
    maxi = max(l)
    l.remove(maxi)
    if l[0]+l[1] < maxi:
        