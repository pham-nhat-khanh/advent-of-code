from day5 import compile
def init():
  input = ''
  with open('./day7-input.txt', 'r', encoding='utf-8') as file:
      input = file.read()
  instructions = [int(piece) for piece in input.split(',')]
  return instructions
program = init()
print(program)

compile(program)