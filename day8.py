from math import ceil
from functools import reduce

with open('./day8-input.txt', 'r', encoding='utf-8') as file:
    input = file.read()
digits = [int(char) for char in input.strip()]
# print(digits)
print(len(digits))

number_of_digits_in_layer = 25 * 6
number_of_layers = ceil(len(digits)/number_of_digits_in_layer)
print(number_of_layers)
print(len(digits)/number_of_digits_in_layer)

layers = [digits[(number_of_digits_in_layer*i):((number_of_digits_in_layer)*(i+1))] for i in range(number_of_layers)]
# print(layers)
# print(layers[2])
# print(len(layers[2]))

# first half
# def number_of_digit(layer, digit):
#   return reduce( lambda counter, current_digit: counter + 1 if digit == current_digit else counter, layer, 0)

# fewest_0_digits_layer = layers[0]
# for i, v in enumerate(layers):
#   if number_of_digit(v, 0) < number_of_digit(fewest_0_digits_layer, 0):
#     fewest_0_digits_layer = v
# print(fewest_0_digits_layer)

# print(number_of_digit(fewest_0_digits_layer, 1)*number_of_digit(fewest_0_digits_layer, 2))

# second half
overlapped_layers = list(zip( *layers))
# print(overlapped_layers)

def get_pixel_value(pixels):
  for pixel in pixels:
    if pixel != 2:
      return pixel
merged = [get_pixel_value(pixels) for pixels in overlapped_layers]
merged_as_string = ''.join(['#' if pixel==1 else ' ' for pixel in merged])
for i in range(0, int(len(merged_as_string)/25)):
  print(merged_as_string[i*25:(i+1)*25])
