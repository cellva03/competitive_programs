# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int,input().split())
    if x == max(x,y,z):
        print("Setter")
    elif y == max(x,y,z):
        print("Tester")
    else:
        print("Editorialist")