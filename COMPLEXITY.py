# cook your dish here
t = int(input())
while t:
    a,b = map(int,input().split())
    if a>b:
        print("yes")
    else:
        print("no")
    t-=1