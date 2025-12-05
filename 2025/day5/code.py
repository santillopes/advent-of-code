intervals = []
ids = []
with open ("input.txt", "r") as file:
    type = "interval"
    for line in file:
        if line.strip():
            if type == "interval":
                intervals.append(line.strip())
            elif type == "id":
                ids.append(line.strip())
        else:
            type = "id"

avaliableids = 0
for id in ids:
    for interval in intervals:
        first, last = interval.split("-")
        if int(id) >= int(first) and int(id) <= int(last):
            avaliableids += 1
            break
print(avaliableids)