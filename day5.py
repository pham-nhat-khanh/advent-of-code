from functools import reduce
from math import floor

def init():
  day2_input = ''
  with open('./day5-input.txt', 'r', encoding='utf-8') as file:
      day2_input = file.read()

  instructions = [int(piece) for piece in day2_input.split(',')]


  return instructions

def fill_to_len_3_with_zeros(arr):
  new_arr = arr[:]
  for i in range(len(new_arr), 3):
    new_arr.append(0)
  return new_arr
def separate_instruction(instruction):
  instruction = str(instruction)
  opcode = int(instruction[-2:])
  parameter_modes = [int(parameter_mode) for parameter_mode in instruction[-3::-1]]
  parameter_modes = parameter_modes if len(parameter_modes) >= 3 else fill_to_len_3_with_zeros(parameter_modes)

  return [opcode, *parameter_modes]
# print(separate_instruction('1003'))

def compile(program):
  index = 0

  def get_value(parameter_mode, index):
    
    return program[index] if parameter_mode == 1 else program[program[index]]
  while index < len(program):
    instruction = separate_instruction(program[index])
    # print('where:', index, 'program:', program, 'instruction', instruction)
    if instruction[0] == 1:
      program[program[index + 3]] = get_value(instruction[1], index+1) + get_value(instruction[2], index + 2)
      index += 4
    elif instruction[0] == 2:
      program[program[index + 3]] = get_value(instruction[1], index+1) * get_value(instruction[2], index + 2)
      index += 4
    elif instruction[0] == 3:
      # inp = input('got instruction 3, please type 1 for a, type 5 for b:')
      # program[int(program[index+1])] = int(inp)
      
      
      index +=2
    elif instruction[0] == 4:
      print(get_value(instruction[1], index + 1))
      index +=2

    # uncomment for b
    elif instruction[0] == 5:
      if get_value(instruction[1], index+1) != 0:
        index = get_value(instruction[2], index+2)
      else:
        index += 3
    elif instruction[0] == 6:
      if get_value(instruction[1], index+1) == 0:
        index = get_value(instruction[2], index+2)
      else:
        index += 3
    elif instruction[0] == 7:
      program[program[index+3]] = 1 if get_value(instruction[1], index+1) < get_value(instruction[2], index + 2) else 0
      index += 4
    elif instruction[0] == 8:
      program[program[index+3]] = 1 if get_value(instruction[1], index+1) == get_value(instruction[2], index + 2) else 0
      index += 4

    elif instruction[0] == 99:
      break
    else:
      raise Exception('error at index {} and value {}'.format(index, program[index]))

if __name__ =='__main__':
  program = init()
  # print([ (index, opcode) for index, opcode in enumerate(program) if opcode == 3])

  compile(program)

