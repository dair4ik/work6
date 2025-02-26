from functools import reduce
import time
import math
#task1
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)
numbers = [2, 3, 4]
print("Product of list:", multiply_list(numbers))
#task2
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower
s = "HelloWorld"
upper, lower = count_case(s)
print("Upper case letters:", upper, "Lower case letters:", lower)
#task3
def is_palindrome(s):
    return s == s[::-1]
s = "madam"
print("Is palindrome:", is_palindrome(s))
#task4
def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)
number, delay = 25100, 2123
print(f"Square root of {number} after {delay} milliseconds is {delayed_sqrt(number, delay)}")
#task5
def all_true(t):
    return all(t)
t = (True, True, False)
print("All elements true:", all_true(t))
