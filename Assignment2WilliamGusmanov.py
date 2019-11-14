'''
William Gusmanov
'''
import math
  # QUESTION 2
def isPrime(L):
  Primes = L.copy()
  for number in L:
    if (number > 0):
      for i in range (2,(int(math.sqrt(number)) + 1)):
        if ((number % i) == 0):
          Primes.remove(number)
          break
  return Primes
'''
input: takes in list L of non-negative integers and an int num
output:a list of Lists, for every element x in L, create  
'''
#QUESTION 3
def my_lists(L,num):
    BigList = []
    for x in L:
        i = 1
        aList = []
        while (i <= x):
            aList.append(i - num)
            i = i + 1
        BigList.append(aList)
    return BigList
def main():
   print("Answer: ", modulus_product(3,644,645))
   print(isPrime([2,5,8,10,13]))
   print(my_lists([1,2,4],5))
   print(my_lists([0],5))

if __name__=="__main__":
   main()

