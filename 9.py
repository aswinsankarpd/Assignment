def checkr(lst):
  nlst = sorted(lst)

  last_np = nlst[-1]

  clst = list(range(1,last_np+1))

  if(nlst == clst):
      print("True")
  else:
      print("False")

lst =  list(map(int,input().split()))
checkr(lst)