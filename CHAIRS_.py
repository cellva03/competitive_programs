# cook your dish here
t = int(input())
while t:
    x,y = map(int,input().split())
    if(x>=y):
        print(x-y)
    else:
        print(0)
    t-=1