# cook your dish here
t = int(input())
while t:
    x,y = map(int,input().split())
    if y>=x and y<=(x+200):
        print("yes")
    else:
        print("no")
    t-=1