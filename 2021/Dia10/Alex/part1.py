values = {")": 3, "]": 57, "}": 1197, ">": 25137}
counts = {")": 0, "]": 0, "}": 0, ">": 0}

translation = {")": "(", "]": "[", "}": "{", ">": "<"}
opening_chars = "([{<"

with open("input.dat") as f:
    data = [l.replace("\n", "") for l in f.readlines()]

for line in data:
    to_close = []

    for char in line:
        if char in opening_chars:
            to_close.append(char)
        else:
            if to_close.pop() != translation[char]:
                counts[char] += 1
                break

score = 0
for k, v in counts.items():
    score += v * values[k]

print(score)
