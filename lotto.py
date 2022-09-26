import random
import time
import sys

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
  """
  gernerates Lotto pool
  
  parameters: integer 
  
  return: array of length of n
  """
  
  arr=[]
  for i in range (1,n+1) :
    arr.append(i)
  return arr

def lotto_pull(total, n):
  """
  parametners:
      total (integer): total number of balls
      n (integer): how many balls will be pulled
  returns:
      the array of pulled balls and number of balls
  """
  
  pulled_balls=[]
  pool=lotto_pool(total)
  
  for mal in range(0,n):
    i=random.randint(1,len(pool))
    pulled_ball=pool.pop(i-1)
    pulled_balls.append(pulled_ball)
  print(pool, pulled_balls, len(pool))
  
  return pulled_balls, len(pulled_balls)

"""
def lotto_play():
  return
"""

if __name__ == "__main__":
  if len(sys.argv) != 3 or int(sys.argv[1]) < int(sys.argv[2]):
    print("enter two numbers.")
  else:
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    result = lotto_pull(arg1, arg2)
    print("{} ball(s) of {} balls will be pulled.".format(arg2, arg1))
    print(result)
    

