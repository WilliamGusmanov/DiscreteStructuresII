#William Gusmanov
#RSA encryption
import math

#converts message to number made up of character alphabetical values [00 - 25]
def convertMessage(message):
  message = message.upper()
  number = ""
  for letter in message:
    if (letter.isalpha()):
      order = ord(letter) - 65
      if (order < 10):
        number = number + "0" + str(order)
      else:
        number = number + str(order)
  return number

#finds block size given n = p * q
def findBlockSize(n):
  twentyfive = "25"
  blockSize = 0
  while(int(twentyfive) < n):
    blockSize = blockSize + 1
    twentyfive = twentyfive + "25"
  return blockSize * 2

#takes number as a string and the block size and returns the blocks as a list of strings
def convertToBlocks(number,blocksize):
  iterations = math.ceil(len(number)/blocksize)
  blocklist = []
  k = 0
  for i in range(iterations):
    j = 0
    temp = ""
    while j < blocksize:
      if k < len(number):
        temp = temp + number[k]
      else:
        temp = temp + "2"
        j = j + 1
        if j < len(number):
          temp = temp + "3"
      j = j + 1
      k = k + 1
    blocklist.append(temp)
  return blocklist

#used to check if a number is prime
#true if prime, else false
def prime(n):
  if (n > 1):
    for i in range(2,math.floor(math.sqrt(n))+1):
      if (n%i == 0):
        return False
  else:
    return False
  return True

#converts the string number and converts it into a int value
def convertToNumber(strNumber):
  i = 0
  while (strNumber[i] == '0'):
    i = i + 1
  number = strNumber[i:len(strNumber)]
  return int(number)

def RSAencrypt(p, q, e, message):
  if (len(message) < 1):
    print("'Message length needs to be greater than 0.'")
  elif not(prime(p) and prime(q)):
    print("'p and q need to be prime.'")
  elif (math.gcd(e, (p-1)*(q-1)) == 1): 
    n = p * q
    blocksize = findBlockSize(n)
    number = convertMessage(message)
    blocks = convertToBlocks(number, blocksize)
    cipher = []
    for block in blocks:
      value = convertToNumber(block)
      remainder = str(value**e%n)
      while (len(remainder) < blocksize):
        remainder = "0" + remainder
      cipher.append(remainder)
    return cipher
  else:
    print("'e needs to be relatively prime to (p-1)(q-1).'")
