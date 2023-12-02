import re

with open('../data/day1.txt', 'r') as f:
    file = f.read()

input_arr = file.splitlines()

# Set False for part one answer.
part_two = True

str_to_int = [['one', 'o1e'], ['two', 't2o'], ['three', 't3e'], ['four', 'f4r'], ['five', 'f5e'],
              ['six', 's6x'], ['seven', 's7n'], ['eight', 'e8t'], ['nine', 'n9e']]

output = []
for line in input_arr:
    temp = line

    if part_two:
        for pair in str_to_int:
            temp = temp.replace(pair[0], pair[1])

    temp = re.sub(r'[a-zA-Z]', '', temp)
    output.append(int(temp[0] + temp[-1]))

print(sum(output))



