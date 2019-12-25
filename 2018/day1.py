with open('./day1.input', 'r', encoding='utf-8') as file:
    input = [int(line.strip()) for line in file.readlines()]
# print(input)

print('result:', sum(input))