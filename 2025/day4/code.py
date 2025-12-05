lines = []
with open ("input.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

rolls = 0
for linenum, line in enumerate(lines):
    rows = len(line)
    for row in range(rows):
        if lines[linenum][row] == '@':
            near = 0
            # top
            if linenum > 0:
                if row > 0 and lines[linenum - 1][row - 1] == '@':
                    near += 1
                if lines[linenum - 1][row] == '@':
                    near += 1
                if row < rows - 1 and lines[linenum - 1][row + 1] == '@':
                    near += 1
            # next
            if row > 0 and lines[linenum][row - 1] == '@':
                    near += 1
            if row < rows - 1 and lines[linenum][row + 1] == '@':
                    near += 1
            # bottom
            if linenum < len(lines) - 1:
                if row > 0 and lines[linenum + 1][row - 1] == '@':
                    near += 1
                if lines[linenum + 1][row] == '@':
                    near += 1
                if row < rows - 1 and lines[linenum + 1][row + 1] == '@':
                    near += 1
            # sum
            if near < 4:
                rolls += 1

print(rolls)