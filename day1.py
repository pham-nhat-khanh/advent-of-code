from functools import reduce
from math import floor

day1_input = []
with open('./day1-input.txt', 'r', encoding='utf-8') as file:
    day1_input = file.readlines()

print(reduce( lambda sum, current: sum + floor(int(current) / 3) - 2, day1_input, 0))