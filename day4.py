from math import floor
from functools import reduce 

def dissect(number):
  return [int(digit) for digit in str(number)] 
def has_same_adjacent_digits(digits):
  return reduce(lambda logic_aggregate, digit_index : logic_aggregate or (digits[digit_index] == digits[digit_index + 1]), range(len(digits) - 1), False)
def digits_only_increase(digits):
  return reduce(lambda logic_aggregate, digit_index : logic_aggregate and (digits[digit_index] <= digits[digit_index + 1]), range(len(digits) - 1), True)

def times_repeated(digits, index):
  result = 1

  if index == len(digits) - 1:
    return 1
  while digits[index + result] == digits[index]:
    result += 1
  return result
def has_same_two_adjacent_digits(digits):
  i = 0
  while i < len(digits):
    if times_repeated(digits, i) == 2:
      return True
    else:
      i += times_repeated(digits, i)
  return False

# count = 0
# for i in range(372037, 905157):
#   digits = dissect(i)
#   if has_same_adjacent_digits(digits) and digits_only_increase(digits):
#     count += 1
# print(count)

count = 0
for i in range(372037, 905157):
  digits = dissect(i)
  digits.append(11)
  if has_same_two_adjacent_digits(digits) and digits_only_increase(digits):
    count += 1
print(count)

# print(dissect(123456))
# print(digits_only_increase(dissect(120456)))

# print(has_same_adjacent_digits(dissect(123356)))
# print(times_repeated([1,2,2,2,3,3,3,3,4], 4))
# print(has_same_two_adjacent_digits(dissect(1112223)))
