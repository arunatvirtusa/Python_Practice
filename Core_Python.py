# 1> Data of XYZ company is stored in sorted list. Write a program for searching specific data 
# from that list.
# Hint: Use if/elif to deal with conditions.

def binary_search(list1, low, high, n):   
  
   if low <= high:  
  
      mid = (low + high) // 2  
  
      # If element is available at the middle itself then return the its index  
      if list1[mid] == n:   
         return mid   
  
      # If the element is smaller than mid value, then search moves  
      # left sublist1  
      elif list1[mid] > n:   
         return binary_search(list1, low, mid - 1, n)   
  
      # Else the search moves to the right sublist1  
      else:   
         return binary_search(list1, mid + 1, high, n)   
  
   else:   
      # Element is not available in the list1  
      return -1  
  
# Test list1ay   
list1 = [12, 24, 32, 39, 45, 50, 54]  
n = 3232
  
# Function call   
res = binary_search(list1, 0, len(list1)-1, n)   
  
if res != -1:   
   print("Element is present at index", str(res))  
else:   
   print("Element is not present in list1")  


# 2> Write a program which will find all such numbers which are divisible by 7 but are not 
# a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed 
# in a comma-separated sequence on a single line.

nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))



# 3>Write a program which can compute the factorial of a given numbers. Use recursion to find it.
# Example: Input supplied to the program:
# 8
# Output:
# 120


# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# 4>. Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30. D  is  the  variable  whose  values  
# should  be  input  to  your  program  in  a  comma-separated sequence.

import math

numbers = raw_input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)


# 5. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 


user_input = raw_input("Enter values for row and column number: ")
rows, cols = user_input.split(",")
rows = int(rows)
cols = int(cols)
grid = []
def array_td(rows, cols):
    for x in range(rows):
        row = []
        for y in range(cols):
            row.append(x * y)
        grid.append(row)
        print(row)
array_td(rows,cols)
print()
print(grid)


# 6> Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. 
# Example: Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world


items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))



# 7. Write  a  program  which  accepts  a  sequence  of  comma  separated  4  digit  binary numbers  as 
#  its  input  and  then  check  whether  they  are  divisible  by  5  or  not.  The numbers that are 
# divisible by 5 are to be printed in a comma separated sequence. 
# Example: Input given: 0100,0011,1010,1001 
# Then the output should be: 1010

items = []
num = [x for x in raw_input().split(',')]
for p in num:
    x = int(p, 2)
    if not x%5:
        items.append(p)
print('sequence items',items)



# 8. Write  a  program  that  accepts  a  sentence  and  calculate  the  number  of  upper  case letters 
# and lower case letters.


def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')

# 9. Given a dictionary in Python, write a Python program to check whether a given key already 


def checkKey(dict, key):
	
	if key in dict.keys():
		print("Present, ", end =' ')
		print("value =", dict[key])
	else:
		print("Not present")

# Driver Code
dict = {'a': 100, 'b':200, 'c':300}

key = 'b'
checkKey(dict, key)

key = 'w'
checkKey(dict, key)



# 10>. Program to prompt whether we need to add or modify the key/value inside the dictionary.

dictionary = {}
input_string = str(input("Do you want to Add / Modify dictionary or Exit?"))

if input_string in ['Add', 'Modify']:
    user_input = [input('key and value') for i in range(2)]
    dictionary[user_input[0]] = user_input[1]
    print("updated dict", dictionary)
else:
    print("undefined option")



