# cook your dish here
for _ in range(int(input())):
    a, b, c = map(int,input().split())
    if a == max(a,b,c):
        print("Alice")
    elif b == max(a,b,c):
        print("Bob")
    else:
        print("Charlie")