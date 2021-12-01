with open("pr1.dat") as f:
    nums = [int(line.rstrip()) for line in f]

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] == 2020:
            print(nums[i] * nums[j], nums[i], nums[j])
