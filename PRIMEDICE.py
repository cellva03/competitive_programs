t = int(input())
while t:
    a, b = map(int,input().split())
    flag = True
    if (a+b)>2:
        for i in range(2,(a+b)):
            if (a+b)%i == 0:
                flag = False
                break
    if flag:
        print("Alice")
    else:
        print("Bob")
    t-=1
        