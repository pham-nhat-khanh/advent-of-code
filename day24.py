from functools import reduce
def init():
  with open('./day24-input.txt', 'r', encoding='utf-8') as file:
    input = [line.strip() for line in file.readlines()]

  return input
tiles = init()

def print_prettily(tiles):
  for row in tiles:
    print(''.join(row))
# print_prettily(tiles)

def count_bugs(tile_position, tiles):
  bug_counter = 0
  
  positions_to_count = []
  if tile_position[0] > 0:
    positions_to_count.append([tile_position[0]-1, tile_position[1]])
  if tile_position[0] < len(tiles)-1:
    positions_to_count.append([tile_position[0]+1, tile_position[1]])
  if tile_position[1] > 0:
    positions_to_count.append([tile_position[0], tile_position[1]-1])
  if tile_position[1] < len(tiles[0])-1:
    positions_to_count.append([tile_position[0], tile_position[1]+1])
  # print(positions_to_count)

  for position_to_count in positions_to_count:
    if tiles[position_to_count[0]][position_to_count[1]] == '#':
      bug_counter += 1
  return bug_counter

def get_next_minute_tiles(tiles):
  new_tiles = [ [0]*5 for i in range(5)]
  for row_index, row in enumerate(tiles):
    for col_index, ele in enumerate(row):
      if ele == '#':
        new_tiles[row_index][col_index] = '#' if count_bugs([row_index, col_index], tiles) == 1 else '.'
      if ele == '.':
        new_tiles[row_index][col_index] = '#' if count_bugs([row_index, col_index], tiles) == 1 or count_bugs([row_index, col_index], tiles) == 2 else '.'
  return new_tiles
# print_prettily(get_next_minute_tiles(tiles))

def is_identical(tiles_1, tiles_2):
  for row_index, row in enumerate(tiles_1):
    for col_index, ele in enumerate(tiles_1):
      if tiles_1[row_index][col_index] != tiles_2[row_index][col_index]:
        return False
  return True

def get_identical_tiles():
  is_current_tile_identical = False
  tiles_versions = [tiles]
  while is_current_tile_identical == False:
    next_tiles = get_next_minute_tiles(tiles_versions[-1])
    tiles_versions.append(next_tiles)

    # print('next tiles:')
    # print_prettily(next_tiles)
    
    for old_tiles in tiles_versions[:-1]:
      if(is_identical(next_tiles, old_tiles)):
          is_current_tile_identical = True
  return tiles_versions[-1]
# print_prettily(get_identical_tiles())
def get_result_a():
  first_matching_tiles = get_identical_tiles()
  flattened_tiles = []
  for row in first_matching_tiles:
    for ele in row:
      flattened_tiles.append(ele)
  print(flattened_tiles)
  result = reduce(lambda total, index_tile: total + 2**(index_tile[0]) if index_tile[1] =='#' else total, enumerate(flattened_tiles), 0)
  return result
print('result:', get_result_a())