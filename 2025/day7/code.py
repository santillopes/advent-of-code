lines = []
with open ("input.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

beamsloc = []
for n in range(len(lines[0])):
    if lines[0][n] == 'S':
        beamsloc.append([n])

splitcount = 0
for linecount, line in enumerate(lines):
    if linecount != 0:
        beamsloc.append([])
        for beamloc in beamsloc[linecount - 1]:
            if line[beamloc] != '^':
                beamsloc[linecount].append(beamloc)
                line_list = list(line) # string to list
                line_list[beamloc] = '|' # change char
                line = ''.join(line_list) # list to char
            else: # it is a ^
                splited = False
                if line[beamloc - 1] != '|' and line[beamloc - 1] != '^': # right side
                    line_list = list(line) # string to list
                    line_list[beamloc - 1] = '|' # change char
                    line = ''.join(line_list) # list to char
                    beamsloc[linecount].append(beamloc - 1)
                    splited = True
                if line[beamloc + 1] != '|' and line[beamloc + 1] != '^': # left side
                    line_list = list(line) # string to list
                    line_list[beamloc + 1] = '|' # change char
                    line = ''.join(line_list) # list to char
                    beamsloc[linecount].append(beamloc + 1)
                    splited = True
                if splited == True:
                    splitcount += 1
    print(line)

print(splitcount)