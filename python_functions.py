# Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  sum = 0
  for num in range(n+1):
    sum += num
  return sum
  

print(sum_to(6))  # returns 21
print(sum_to(10)) # returns 55

# # --------------------

# # Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(numbers):
  lg = 0
  for n in numbers:
    if n > lg:
      lg = n
  return lg

print(largest([1, 2, 3, 4, 0]))  # returns 4
print(largest([10, 4, 2, 231, 91, 54]))  # returns 231

# # --------------------

# # Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurrences(str1, str2):
  return str1.count(str2)

print(occurrences('fleep floop', 'e'))   # returns 2
print(occurrences('fleep floop', 'p'))   # returns 2
print(occurrences('fleep floop', 'ee'))  # returns 1
print(occurrences('fleep floop', 'fe'))  # returns 0

# # --------------------

# # Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
  prod = 1
  for arg in args:
    prod *= arg
  return prod

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0