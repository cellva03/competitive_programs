for _ in range(int(input())):
    x, y, z = map(int,input().split())
    l =[x,y,z]
    maxi = max(l)
    l.remove(maxi)
    