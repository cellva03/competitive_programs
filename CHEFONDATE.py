# cook your dish here
t = int(input())
while t:
    x,y = map(int,input().split())
    if y>x:
        print("NO")
    else:
        print("YES")
    t-=1