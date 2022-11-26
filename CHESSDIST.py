# cook your dish here
t = int(input())
while t:
    a, b, c, d = map(int,input().split())
    print(max(abs(a,c),abs(b,d)))
    t-=1