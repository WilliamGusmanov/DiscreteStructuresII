import sys
def EuclideanAlg(M,m,alist,t):
  if (m == 0):
    return alist
  else:
    q = M//m
    r = M%m
    if (t):
      a = q
    else:
      a = r
    alist.append(a)
    EuclideanAlg(m,r,alist, t)
    return alist
def ExEuclideanAlg(M,m):
  s0 = 1
  s1 = 0
  s2 = 1
  listofq = []
  listofq = EuclideanAlg(M,m,listofq,True)
  for i in range(len(listofq)-1):
    s2 = s0 - listofq[i]*s1
    s0 = s1
    s1 = s2
  return s2
def pairwiseprime(alist):
  negativevalue = True
  gcdtest = True
  for i in range(len(alist)):
    if (alist[i] < 1):
      negativevalue = False
    for j in range(i+1,len(alist)):
      if (alist[i] != alist[j]):
        L = EuclideanAlg(alist[i],alist[j],[],False)
        if (L[len(L)-2] != 1):
          gcdtest = False
  return negativevalue and gcdtest
def ChineseRemainderTheorem(alist):
  listofm = []
  listofa = []
  listofM = []
  listofy = []
  for i in alist:
    listofa.append(i[0])
    listofm.append(i[1])
  if pairwiseprime(listofm):
    M = 1
    for j in listofm:
      M = M * j
    for i in range(len(listofm)):
      listofM.append(M/listofm[i])
      listofy.append(ExEuclideanAlg(listofM[i],listofm[i]))
    x = 0
    for i in range(len(listofm)):
      x = x + listofa[i]*listofM[i]*listofy[i]
    return int(x%M)
  else:
   sys.exit("'Cannot proceed, the modulus values are not relatively prime'")
