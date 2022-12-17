for _ in range(int(input())):
    n, x = map(int,input().split())
    if n > 6:
        if n%6==0:
            res = (n//6)
        else:
            res = (n//6)+1
        print(res*x)
    else:
        print(x)

        
