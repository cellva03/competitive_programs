# cook your dish here
for _ in range(int(input())):
    n, m, k = map(int,input().split())
    print("yes") if (k*m) >= n else print("no")