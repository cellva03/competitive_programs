for _ in range(int(input())):
  n, x, y = map(int,input().split())
  res = x + (y*2)
  if res > n:
    print("No")
