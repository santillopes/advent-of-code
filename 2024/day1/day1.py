
list1 = []
list2 = []
with open ("input.tsv", "r") as file:
    for line in file:
        row = line.split()
        list1.append(row[0])
        list2.append(row[1])

print(list1)
print(list2)
