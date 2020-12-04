def byr(x):
    return(int(x) in range(1920, 2021))

def iyr(x):
    return(int(x) in range(2010, 2021))

def eyr(x):
    return(int(x) in range(2020, 2031))

def hgt(x):
    if x[-2:] == "in":
        return int(x[:-2]) in range(59,77)
    elif x[-2:] == "cm":
        return int(x[:-2]) in range(150,194)
    else:
        return False

def hcl(x):
    if x[0] == "#" and len(x) == 7:
        for i in x[1:]:
            if i not in "0123456789abcdef":
                return False
        return True
    return False

def ecl(x):
    return(x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

def pid(x):
    try:
        int(x)
        return len(x) == 9
    except:
        return False

def PassDic(p):
    passdic = {}
    l = p.split(" ")
    for i in l:
        key = i.split(":")[0]
        value = i.split(":")[1]
        passdic[key] = value
    return passdic
    

def IsPassportValid(dic):
    MandatoryKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    KeysInDic = list(dic.keys())
    return (sorted(MandatoryKeys) == sorted(KeysInDic)) or (sorted(MandatoryKeys + ["cid"]) == sorted(KeysInDic))

def IsPassportValid2(dic):
    try:
        return( IsPassportValid(dic) and byr(dic["byr"]) and iyr(dic["iyr"]) and eyr(dic["eyr"]) and hgt(dic["hgt"])
                and hcl(dic["hcl"]) and ecl(dic["ecl"]) and pid(dic["pid"]))
    except:
        return False
    

f = open("day4input.txt", "r")
data = f.read()
PassportsRaw = data.split("\n\n")

passports = []
for passport in PassportsRaw:
    x = ""
    for char in passport:
        if char != "\n":
            x += char
        else:
            x += " "
    passports.append(x)

count = 0
for i in passports:
    if IsPassportValid2(PassDic(i)):
        count += 1
print(count)







