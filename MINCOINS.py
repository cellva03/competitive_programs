t = int(input())
while t:
    x = int(input())
    if x%5 == 0:
        if x%10 == 0:
            print(x//10)
        else:
            print((x//10)+1)
    else:
        print(-1)
    t-=1