index = 0
lst = []
nums = [4, 3, 2, 3, 4]
answer = 6
same_result = 0
for index in range(0, len(nums)):
    print("Element:", index)
    for i in nums:
        if i == nums[index] and same_result == 1:
            continue
        elif i == nums[index]:
            same_result = 1
        res = i + nums[index]
        print("Result:", nums[index], "+", i, "=", res)
        if res == answer:
            ind = nums.index(nums[index])
            ind2 = nums.index(i)
            print("1st Index:", ind, "2nd Index:", ind2)

