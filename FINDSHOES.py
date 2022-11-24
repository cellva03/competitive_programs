# cook your dish here
t = int(input())
while t:
    x, y = map(int,input().split())
    tot = x*2
    if y>x:
        tot-=x
    else:
        tot=tot-y
    print(tot)
    t-=1