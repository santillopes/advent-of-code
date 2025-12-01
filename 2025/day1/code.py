rotations = []
with open("input.csv", "r") as file:
    for line in file:
        rotations.append(line.strip()) # strip() removes any leading, and trailing whitespaces

position = 50
zerocounter = 0
for rotation in rotations:
    if rotation[0] == 'L':
        value = -int(rotation[1:]) # all digits from the second one
    else: # 'R'
        value = int(rotation[1:])

    position = (position + value) % 100
    if position == 0:
        zerocounter += 1

print(f"zeros: {zerocounter} after {len(rotations)} spins")