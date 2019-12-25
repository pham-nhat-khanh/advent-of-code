
# with open('./day12-input.txt', 'r', encoding='utf-8') as file:
#     input = file.readlines()
# print(input)
# position = [ for position_string in input]
def init():
  position_matrix = [
    [-8, -18, 6],
    [-11, -14, 4],
    [8, -3, -10],
    [-2, -16, 1]
  ]
  velocity_matrix = [ [0]*3 for i in range(4)]
  return position_matrix, velocity_matrix
position_matrix, velocity_matrix = init()
# print(position_matrix, velocity_matrix)

def add_two_matrix(matrix_1,matrix_2):
  return [ [matrix_1[row][column] + matrix_2[row][column] for column in range(len(matrix_1[0]))] for row in range(len(matrix_1))]

def get_velocity_difference_matrix(position_matrix):
  def get_velocity_difference_row(row):
    inverted_velocity_matrix = list(zip(position_matrix))
    def get_velocity_difference_element(column):
      element = position_matrix[row][column]
      return sum([1 if element>other_element else 0 if element==other_element else -1 for other_element in inverted_velocity_matrix[column]])
    return [get_velocity_difference_element(column) for column in range(len(position_matrix[0]))]
  return [get_velocity_difference_row(row) for row in range(len(position_matrix))]

def compute_next_velocity_matrix(velocity_matrix, position_matrix):
  velocity_difference_matrix = get_velocity_difference_matrix(position_matrix)
  return [velocity_matrix[i][j] + velocity_difference_matrix[i][j] for row in position_matrix]
  
  return add_two_matrix(velocity_matrix, velocity_difference_matrix)

def compute_next_position_matrix(computed_velocity_matrix, current_position_matrix):
  return add_two_matrix(current_position_matrix, computed_velocity_matrix)

# for i in range(1000):
#   velocity_matrix = compute_next_velocity_matrix(velocity_matrix, position_matrix)
#   position_matrix = compute_next_position_matrix(velocity_matrix, position_matrix)

# print(velocity_matrix)
# print(position_matrix)
# total_energy = [sum(position)*sum(velocity) for 