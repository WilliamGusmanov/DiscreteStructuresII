#William Gusmanov 

# Write a Python expression to find the number of seconds in a century. You can assume one year has 365 days. Save the value to a variable called seconds_in_decade.Then print it.
seconds_in_decade = 100 * 365 * 24 * 60 * 60;
print("Question 1: ")
print (seconds_in_decade , "seconds in 100 years.")

#Write a Python expression to find the remainder of 5789248divided by 6by using Python’s modulus operator. Save the value to a variable called remainder_with_mod.Then print it.
remainder_with_mod = 5789248 % 6;
print("Question 2: " )
print("remainder with mod:",remainder_with_mod)

#Write a Python expression to find the remainder of 5789248 divided by 6without using Python’s modulus operator. Instead, you must use thefloor division(//)operator. Save the value to a variable called remainder_without_mod
#Num - (divisor * (number / divisor [floored])) = remainder
remainder_without_mod = 5789248 - (6 * (5789248 // 6))
print("Question 3: ")
print ("remainder no mod:", remainder_without_mod)

#Write a comprehension over {1, 3, 5, 7, 11} whose value is the set consisting of theirfourth power minus 2.Print the result
print("Question 4: ")
print({x * x * x * x - 2 for x in {1,3,5,7,11}})

#Write a comprehension over [11, -2, 8, 15, 22]whose value is the listconsisting of the cubeminus the value’s index.Assume that the indexstarts at zero and assignvariable M to be the list[11, -2, 8, 15, 22]. Print the result.
print("Question 5:")
array = [11, -2, 8, 15, 22]
print([x * x * x - array.index(x) for x in array])

# Write a Python expression that will give the union of the following two sets: the square of numbers from 1 to 30 the cube of numbers from 1 to 30 And the result of that unioned set intersected with the following set: four times each number from 1 to 30 Then print the final resulting set. You cannot manually write out the numbers from 1 to 30, you must use a built-in Python function that will do that for you
print("Question 6") 
set1 = set()
set2 = set()
set3 = set()
for i in range(1,31):
  set1.add(i*i)
#print("set 1: ",set1,"\n")
for i in range(1,31):
  set2.add(i*i*i)
#print("set 2: ", set2,"\n")  
for i in range(1,31):
  set3.add(4*i)
#print("set 3: ", set3,"\n")  
set1 = set1.union(set2)
#print(set1,"\n")
set1 = set1.intersection(set3)
print(set1,"\n") 