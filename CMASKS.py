# cook your dish here
for _ in range(int(input())):
    x, y = map(int,input().split())
    print("Cloth") if (x*100)>=(y*10) else print("DISPOSABLE")