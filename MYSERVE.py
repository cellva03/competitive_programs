# cook your dish here
t = int(input())
while t:
    a, b = map(int,input().split())
    if (a+b)%4 == 0 or (a+b)%4 == 1:
        print("Alice")
    else:
        print("Bob")
    t-=1