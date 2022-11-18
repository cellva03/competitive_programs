# cook your dish here
t = int(input())
while t:
    l = list(map(int,input().split()))
    x =max(l)
    l.remove(x)
    print(max(l))
    t-=1