t= int(input())
while t:
    x,y = map(int,input().split())
    if x==y:
        print("ANY")
    elif x>y:
        print("SECOND")
    else:
        print("FRIST")
    t-=1