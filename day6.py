import re
from functools import reduce

with open('./day6-input.txt', 'r', encoding='utf-8') as file:
    input = [re.split(r'\)', line.strip()) for line in file.readlines()]
# print(input)

all_orbitting = {'COM': set()}
def add_path(all_orbitting, path):
  [orbitted, orbitting] = path
  if orbitting in all_orbitting:
    all_orbitting[orbitting].add(orbitted)
  else:
    all_orbitting[orbitting] = set([orbitted])

for path in input:
  add_path(all_orbitting, path)
# print(all_orbitting)

def traverse_objs(objs): #from orbitting to orbitted only
  new_objs = set()
  for obj in objs:
    for orbitted in all_orbitting[obj]:
      new_objs.add(orbitted)
  return new_objs
# print(traverse_objs(set(['YOU', 'COM'])))

def get_total_orbits_of_object(obj):
  total = 0
  orbittings = set([obj])

  while len(orbittings) > 0:
    orbittings = traverse_objs(orbittings)
    total += len(orbittings)
  return total
# print(get_total_orbits_of_object('MV6'))

#a
total_orbits = 0
for orbit in all_orbitting:
  total_orbits += get_total_orbits_of_object(orbit)
# print('result a:', total_orbits)

#b
def find_orbittings(orbitted):
  orbittings = set()
  for orbitting, orbitteds in all_orbitting.items():
    if orbitted in orbitteds:
      orbittings.add(orbitting)
  return orbittings
def traverse_all_objs(objs): # no discrimination between orbittings and orbitteds
  new_objs = set()
  for obj in objs:
    for orbitted in all_orbitting[obj]:
      new_objs.add(orbitted)
    for orbitting in find_orbittings(obj):
      new_objs.add(orbitting)
  return new_objs
# print(traverse_objs(set(['YOU', 'COM'])))

count = 500
least_moves_to_SAN = 0
traversing = set(['YOU'])
traversing = traverse_objs(traversing)
destination = iter(all_orbitting['SAN']).__next__()
# print(traversing)
# print(destination)


while not destination in traversing and count > 0:
  # print('traversing:', traversing, least_moves_to_SAN)
  traversing = traverse_all_objs(traversing)
  least_moves_to_SAN +=1
  count -=1
print('result b', least_moves_to_SAN)