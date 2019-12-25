from functools import reduce
from math import floor

wire_1_movements, wire_2_movements = ['R8','U5','L5','D3'], ['U7','R6','D4','L4']
# with open('./day3-input.txt', 'r', encoding='utf-8') as file:
#     wire_1_movements, wire_2_movements = [line.split(',') for line in file.readlines()]
# print(wire_1_movements)

X = 'x'
Y = 'y'
def get_positions(wire_movements):
  wire_positions = [{X: 0,Y: 0}]
  def get_position(previous, wire_movement):
    wire_direction = wire_movement[0]
    wire_length = int(wire_movement[1:])
    if(wire_direction == 'R'):
      return {X: previous[X], Y: previous[Y] + wire_length}
    elif(wire_direction == 'L'):
      return {X: previous[X], Y: previous[Y] - wire_length}
    elif(wire_direction == 'U'):
      return {X: previous[X] + wire_length, Y: previous[Y]}
    elif(wire_direction == 'D'):
      return {X: previous[X] - wire_length, Y: previous[Y]}
    else:
      raise Exception('no movement')
  for wire_movement in wire_movements:
    wire_positions.append(get_position(wire_positions[-1], wire_movement))
  return wire_positions
wire_1_positions = get_positions(wire_1_movements)
wire_2_positions = get_positions(wire_2_movements)
# print(wire_1_positions)
# print(wire_2_positions)

def get_collision(wire_1, wire_2):
  x1, y1 = wire_1[0][X], wire_1[0][Y]
  x2, y2 = wire_1[1][X], wire_1[1][Y]
  x3, y3 = wire_2[0][X], wire_2[0][Y]
  x4, y4 = wire_2[1][X], wire_2[1][Y]
  try:
    return {X: ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - x4*y3) ) / ( (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4) ), Y: ( (x1*y2 -y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / ( (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4) )}
  except ZeroDivisionError:
    # print('error at ', wire_1, wire_2)
    return None
def get_collisions(wire_1_positions, wire_2_positions):
  
  collisions = []
  for i in range(len(wire_1_positions)-1):
    for j in range(len(wire_2_positions)-1):
      collisions.append(get_collision([wire_1_positions[i], wire_1_positions[i+1]], [wire_2_positions[j], wire_2_positions[j+1]]))
  return collisions
print(get_collision([wire_1_positions[0], wire_1_positions[1]], [wire_2_positions[0], wire_2_positions[1]]))
collisions = get_collisions(wire_1_positions, wire_2_positions)

def get_min(collisions):
  min = float("inf")
  for i, collision in enumerate(collisions):
    if collision == None or min <= abs(collision[X]) + abs(collision[Y]):
      pass
    else:
      min = abs(collision[X]) + abs(collision[Y])
      print(min, collision, i)
  return min
print(collisions)
print('result:', get_min(collisions))
