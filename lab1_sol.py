# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
# B. avg
# Given a list of numbers, return the average of the list.
# If numbers equal [10, 10, 15, 7], the return value should be 10.5
def avg(numbers):
  # +++your code here+++
  sum=0
  for i in  numbers:
      ##print (i)
      sum +=i
  avr= sum / len(numbers)
  print(avr)
  return sum

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
  # +++your code here+++
  if len(s) <=2:
      return ""
  else:
       return s[0]+s[1]+s[-2]+s[-1]
  return


# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
  # +++your code here+++
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b

  return

# B. uniq
# Given a list of objects (numbers, strings, booleans), return the same list without duplicates.
# If a = [1, True, "otter", "platypus", 1, 2, False, "otter"]
# the return value should be [1, True, "otter", "platypus", 2, False]
# Note that the order does not matter
def uniq(a):
  list2 = list(set(a))
  return list2

# B. merge
# Given two sorted list of numbers, return a sorted list with the elements of both lists.
# If a = [1, 5, 13, 14] and b = [2, 7, 8, 42]
# the return value should be [1, 2, 5, 7, 8, 13, 14, 42]
def merge(a, b):
  # +++your code here+++
  c = a+b
  c.sort()
  print(c)
  return c



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    numbers = [1, 2, 3, 4, 6]
    avergae = avg(numbers)
    doubleend=both_ends("qw")
    print(doubleend)
    doubleend = both_ends("spring")
    print(doubleend)
    result=mix_up("dog", "dinner")
    print(result)
    a = [1, True, "otter", "platypus", 1, 2, False, "otter"]
    newList=uniq(a)
    print(newList)

    a = [1, 5, 13, 14]
    b = [2, 7, 8, 42]
    c=merge(a, b)
    print(c)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
