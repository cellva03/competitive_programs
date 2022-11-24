# cook your dish here
t = int(input())
while t:
    x, y = map(int,input().split())
    c=0
    if x == y:
        print(0)
    else:
        while(1):
            x+=8
            if x >= y:
                c+=1
                break
            else:
                c+=1
                continue
        print(c)
    t-=1