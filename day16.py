from functools import reduce
from math import ceil

input = ''
with open('./day16-input.txt', 'r', encoding='utf-8') as file:
  input = file.read()
  input = [int(digit) for digit in input]
# print(input)
# print(type(input))



base_pattern = [0, 1, 0, -1]
def get_pattern(index, input_len):
  pattern =[repeated_digit for digit in base_pattern for repeated_digit in [digit]*(index+1)][1:]
  if len(pattern) < input_len:
    return (pattern * ceil(input_len / len(pattern)))[:input_len]
  else:
    return pattern[:input_len]

def compute_output(input):
  return [compute_output_digit(digit, input) for digit in range(len(input))]
def compute_output_digit(digit_index, input): #index is 0-based
  pattern = get_pattern(digit_index, len(input))
  computation_result = reduce( lambda accumulator, index_and_value: accumulator + index_and_value[1]*pattern[index_and_value[0]], list(enumerate(input)), 0)
  return computation_result % 10

output = input
for i in range(100):
  output = compute_output(output)
print(output)