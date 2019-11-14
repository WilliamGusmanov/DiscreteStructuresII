'''
William Gusmanov
'''
import math
#QUESTION 1
def modulus_product(base, exponent, divisor):
  bin_exponent = bin(exponent) # ex.) 0b1111,  /3^344 mod 645
  size = len(bin_exponent) - 2
  i = 1 #increment loop
  List = []
  tempMod = base%divisor 
  List.append(tempMod)
  while(i < size):
    tempMod = (tempMod*tempMod)%divisor
    List.append(tempMod)
    i = i+1
  i = len(bin_exponent) - 1 #accces end of string
  j = 0
  Answer = 1
  while (i > 1):
    if (bin_exponent[i] == "1"):
      print(List[j])
      Answer = Answer * List[j]
    j = j + 1
    i = i - 1
  return Answer
