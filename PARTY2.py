# cook your dish here
for _ in range(int(input())):
    n, x, k = map(int,input().split())
    print("yes") if (x*n) <= k else print("no")