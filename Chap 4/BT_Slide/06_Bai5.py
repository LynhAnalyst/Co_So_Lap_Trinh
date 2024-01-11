import random

def kiem_tra_nhap(n):
  if not 0<=n<=3:
    return False
  else:
    if n == 0:
      return "Stop"
    else:
      return True
  
def nguoi_nhap():
  return int(input('Human: '))

def may_nhap():
  m = random.randint(1,3)
  print(f"Computer: {m}")
  return m

def sosanh(n,m):
  if n==m: 
    print('Result:'+' Draw!')
  elif n==1 and m==2: 
    print('Result:'+' Human Win!')
  elif n==2 and m==3: 
    print('Result:'+' Human Win!')
  elif n==3 and m==1: 
    print('Result:'+' Human Win!')
  elif n==2 and m==1: 
    print('Result:'+' Human Lose!')
  elif n==3 and m==2: 
    print('Result:'+' Human Lose!')
  elif n==1 and m==3: 
    print('Result:'+' Human Lose!')
while True:
  n = nguoi_nhap()
  x = kiem_tra_nhap(n)
  if x == "Stop":
    break
  elif x==False:
    print('Nhap lai')
    continue
  m = may_nhap()
  sosanh(n,m)