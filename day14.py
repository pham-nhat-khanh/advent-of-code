import re
from functools import reduce
with open('./day14-input.txt', 'r', encoding='utf-8') as file:
    input = [re.split('=>', line) for line in file.readlines()]
# print(input)

def structureize_reaction(reaction):
  [quantity, name] = reaction.strip().split()
  return (int(quantity), name)
reactions = { reaction[1] : reaction[0].split(',') for reaction in input}
reactions = { structureize_reaction(equate_right): [structureize_reaction(ingredient) for ingredient in equate_left] for equate_right, equate_left in reactions.items()}
# print(reactions)
def get_least_amount(ingredient):
  return least_common_divisor(ingredient, reaction)* reaction[ingredient]

ingredients = reactions[(1, 'FUEL')]
print(ingredients)


def get_baser_ingredients(ingredients):
  baser_ingredients = {}
  def add_ingredient(baser_ingredients, ingredient):
    if(ingredient is in baser_ingredients):
      return ...baser_ingredients, ingredient: 
    else:
      return ...baser_ingredients, ingredient
  reurn reduce( add_ingredient, ingredients, {})
  

while len(ingredients) > 1:
  ingredients = get_baser_ingredients(ingredients)
print(ingredients)
