for _ in range(int(input())):
  x, y = map(int,input().split())
  if y == x:
    print("NEUTRAL")
  elif x > y:
    print("LOSS")
  else:
    print("PROFIT")
    
    
