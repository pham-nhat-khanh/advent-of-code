from functools import reduce
from math import floor

def init():
  day2_input = ''
  with open('./day2-input.txt', 'r', encoding='utf-8') as file:
      day2_input = file.read()

  storage = list( map( lambda x: int(x), day2_input.split(',')))


  return storage

def compile(number_list):
  for index, value in enumerate(number_list):
    if index % 4 == 0:
      if number_list[index] == 1:
        number_list[number_list[index + 3]] = number_list[number_list[index+1]] + number_list[number_list[index+2]]
      elif number_list[index] == 2:
        number_list[number_list[index + 3]] = number_list[number_list[index+1]] * number_list[number_list[index+2]]
      elif number_list[index] == 99:
        break
      else:
        raise Exception('error at index {} and value {}'.format(index, value))

def print_2a():
  number_list = init()
  number_list[1] = 12
  number_list[2] = 2
  # print('before: ', number_list)

  compile(number_list)
  # print('after: ', number_list)
  print('result', number_list[0])

def print_2b():
  for noun in range(0, 100, 1):
    for verb in range(0, 100, 1):
      number_list = init()
      # print("before: ", number_list)

      number_list[1] = noun
      number_list[2] = verb
      compile(number_list)
      if number_list[0] == 19690720:
        print('noun: ', noun, ', verb: ', verb, ', result: ', 100 * noun + verb)

print_2a()
print_2b()