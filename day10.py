with open('./day10-input.txt', 'r', encoding='utf-8') as file:
  input = [ line.strip() for line in file.readlines()]
# print(input)
X = 'x'
Y = 'y'

def is_blocking(point_1,point_2, blocking_point):
  def is_on_line(): # there's no need to check for opposite signs
    slope_blocking_and_2 = (point_2[Y] - blocking_point[Y]) / (point_2[X] - blocking_point[X])
    slope_blocking_and_1 = (point_1[Y] - blocking_point[Y]) / (point_1[X] - blocking_point[X])
    if slope_blocking_and_2 == slope_blocking_and_1:
      return True
    return False 
  def is_coor_between():
    if (point_1[X] < blocking_point[X] < point_2[X] or point_1[X] > blocking_point[X] > point_2[X]) and (point_1[Y] > blocking_point[Y] > point_2[Y] or point_1[Y] < blocking_point[Y] < point_2[Y]):
      return True
    return False
  if not is_coor_between():
    return False
  if not is_on_line():
    return False
  return True

asteroid_coordinates = [ {X: r_index, Y: c_index} for r_index, row in enumerate(input) for c_index, ele in enumerate(row) if ele == '#']
print(asteroid_coordinates)