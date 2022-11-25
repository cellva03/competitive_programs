# cook your dish here
t = int(input())
while t:
    n, m = map(int,input().split())
    if n%m == 0 and (n//m)%2 == 0:
        print("yes")
    else:
        print("no")
    t-=1