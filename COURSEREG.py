# cook your dish here
for _ in range(int(input())):
    n, m, k = map(int,input().split())
    print("yes") if (m-k)>=n else print("no")