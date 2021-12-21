values = {"(": 1, "[": 2, "{": 3, "<": 4}

translation = {")": "(", "]": "[", "}": "{", ">": "<"}
opening_chars = "([{<"

with open("input.dat") as f:
    data = [l.replace("\n", "") for l in f.readlines()]

autocomplete_scores = []
for line in data:
    to_close = []
    valid = True

    for char in line:
        if char in opening_chars:
            to_close.append(char)
        else:
            if to_close.pop() != translation[char]:
                valid = False

    if valid:
        score = 0
        while len(to_close) > 0:
            score *= 5
            char = to_close.pop()
            score += values[char]
        autocomplete_scores.append(score)

autocomplete_scores.sort()
print(autocomplete_scores[len(autocomplete_scores) // 2])
