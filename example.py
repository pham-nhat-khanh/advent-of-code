import pipes

def get_input():
  numb = input()
  print(numb)
  return int(numb)
def get_total_from_input():
  total = 0
  for i in range(5):
    total +=get_input()
  return total
# print('total:', get_total_from_input())

