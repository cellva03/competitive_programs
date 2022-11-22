# cook your dish here
t = int(input())
while t:
    x,y,z = map(int,input().split())
    res = (x*5)+(y*10)
    print(res//z)
    t-=1