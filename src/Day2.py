import re

with open('../data/day2.txt', 'r') as f:
    file = f.read()

input_arr = file.splitlines()

rgb = [12, 13, 14]
output = []

for i, line in enumerate(input_arr):
    all_games = line.split(':')[1]
    games = all_games.split(';')
    passed = True
    for game in games:
        colors = game.split(',')
        temp = [0, 0, 0]

        for color in colors:
            color = color.strip()
            num = int(re.sub(r'[a-zA-Z]', '', color))
            if 'red' in color:
                temp[0] = num
            elif 'green' in color:
                temp[1] = num
            elif 'blue' in color:
                temp[2] = num

        for j in range(len(temp)):
            if temp[j] > rgb[j]:
                passed = False
    if passed:
        output.append(i+1)

print('Part 1 answer: ' + str(sum(output)))

output = []
for i, line in enumerate(input_arr):
    all_games = line.split(':')[1]
    games = all_games.split(';')
    temp = [1, 1, 1]
    for game in games:
        colors = game.split(',')
        for color in colors:
            color = color.strip()
            num = int(re.sub(r'[a-zA-Z]', '', color))
            if 'red' in color:
                if temp[0] < num:
                    temp[0] = num
            elif 'green' in color:
                if temp[1] < num:
                    temp[1] = num
            elif 'blue' in color:
                if temp[2] < num:
                    temp[2] = num
    output.append(temp[0] * temp[1] * temp[2])

print('Part 2 answer: ' + str(sum(output)))
