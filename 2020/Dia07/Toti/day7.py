l = [line.split("\n")[0] for line in open("day7input.txt", "r")]

rules = {}
for i in l:
    rules[i.split(" contain ")[0]] = i.split(" contain ")[1].split(", ")


def ReturnNumberAndCleanString(str):
    num = ""
    x = ""
    for i in str:
        if i in "abcdefghijklmnopqrstuvwxyz ":
            x += i
        if i in "0123456789":
            num += i
    if x[:2] == "no":
        return(x, 0)
    if x[-1] == "g":
        x += "s"
    return(x[1:], int(num))

def ContainsShinyGold(bag):
    # print("IN " + str(bag))
    # print("----------")
    for i in rules[bag]:
        # print(RemoveNumberAndDotFromString(i))
        if ReturnNumberAndCleanString(i)[0] == "shiny gold bags":
            # print("FOUND! +1")
            return True
        elif ReturnNumberAndCleanString(i)[0] == "no other bags":
            return False
        else:
            # print("---------->")
            if ContainsShinyGold(ReturnNumberAndCleanString(i)[0]):
                return True
            else:
                continue
    return False

def IndividualBagsInsideBag(bag):
    c = 0
    for i in rules[bag]:
        if ReturnNumberAndCleanString(i)[0] != "no other bags":
            c += ReturnNumberAndCleanString(i)[1] + ReturnNumberAndCleanString(i)[1] * (IndividualBagsInsideBag(ReturnNumberAndCleanString(i)[0]))
    
    return(c)



c = 0
for i in rules:
    if i == "shiny gold bags":
        continue
    else:
        # print("SUPER IN "+ i)
        if ContainsShinyGold(i):
            c += 1
            # print("count: "+ str(c))

print(c)

print(IndividualBagsInsideBag("shiny gold bags"))
