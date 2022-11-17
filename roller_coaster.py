# cook your dish here
t = int(input())
while t:
    x,h = map(int,input().split())
    if x>=h:
        print("YES")
    else:
        print("NO")
    t-=1