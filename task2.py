import time

def factorial(n): 
 if n == 0: 
  return 1
 else:
  return n * factorial(n-1)
  
start = time.time()

for i in range(1,1001):
 print (factorial(0),factorial(1),factorial(2),factorial(3),factorial(4),factorial(5),
 factorial(6),factorial(7),factorial(8),factorial(9),factorial(10))
 
 #the following block comment is the "other way to do it"
 #interestingly, to me at least, it is actually slightly slower than the non-commented method
 '''currFact = 1
 print('0!=' + str(currFact), end=" ")

 for n in range(1,11):
  currFact *= n
  print(str(n) + '!=' + str(currFact), end=" ")

 print()'''

print (time.time() - start)