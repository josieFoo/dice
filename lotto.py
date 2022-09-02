import random
import time

def dice(count):
  dic={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
  c=0
  while (True):
     i=random.randint(1,6)
     c+=1
     dic[i]=dic[i]+1
     print(dic)
     if dic[i]==count:
       dicprobablity=dic
       for p in range(1,7):
         dicprobablity[p]=dicprobablity[p]/c*100
       print (dicprobablity)
       return (c, 'mal geworfen')
     elif not count:
       break
      

def lotto_pool(n):
  arr=[]
  for i in range (1,n+1) :
    arr.append(i)
  return arr

def lotto_pull(total, n):
  pulled_balls=[]
  pool=lotto_pool(total)
  for mal in range(0,n):
    i=random.randint(1,len(pool))
    pulled_ball=pool.pop(i-1)
    pulled_balls.append(pulled_ball)
  print(pool, len(pool))
  return pulled_balls, len(pulled_balls)

def lotto_play():
  return


