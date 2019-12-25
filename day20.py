from typing import List
input: List[List[str]] = [[]]

input.append([1,2,3])
print(input)

def is_deadend(maze, position):
  pass
def is_next_to_portal(maze, position):
def is_at_the_end(maze, position):

def can_move_forward(maze, current_position, previous_position):
def get_next_possible_positions(maze, current_position, previous_position):

def possible_positions_at_turn(maze, original_position):

def get_portal_name(maze, position):
  height, width = len(maze), len(maze[0])
  position_y, position_x = position
  position_value = maze[position_y][position_x]

  for y in range(position_y-1, position_y+2):
    for x in range(position_x-1, position_x+2):
      try:
        neighbor_value = maze[y][x]
        if neighbor_value >= 'A' and neighbor_value <= 'Z': # is a character
          if x + y < position_x + position_y:
            return neighbor_value + position_value
          else:
            return position_value + neighbor_value
      except IndexError:
        pass
      
def get_original_position(maze);
def find_portal_postion_from_name(maze, portal_name, portal_position):


def walk_the_maze(maze, original_position):
  possible_positions = [original_position]
  while not is_at_the_end(maze, possible_positions)):
    possible_positions = get_next_possible_positions

walk_the_maze(input, get_original_position(input))