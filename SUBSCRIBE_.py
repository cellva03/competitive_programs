for _ in range(int(input())):
    n, x = map(int,input().split())
    if n > 6:
        res = (n//6)+1
        print(res*x)

        
