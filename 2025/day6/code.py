lines = []
with open ("input.txt", "r") as file:
    for line in file:
        lines.append(line.strip().split())

result = 0
for n in range(len(lines[0])):
    rowtotal = 0
    for line in lines:
        if line != lines[len(lines) - 1]: # not the last (operators)
            if lines[len(lines) - 1][n] == '+':
                rowtotal = rowtotal + int(line[n])
            elif lines[len(lines) - 1][n] == '*':
                if rowtotal == 0:
                    rowtotal = int(line[n])
                else:
                    rowtotal = rowtotal * int(line[n])
    result += rowtotal

print(f"Final result: {result}")