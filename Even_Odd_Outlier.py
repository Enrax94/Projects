def find_outlier(integers):
    even_count = 0
    even_num = []
    odd_count = 0
    odd_num = []
    for i in integers:
        if i % 2 == 0:
            even_count += 1
            even_num.append(i)
        else:
            odd_count += 1
            odd_num.append(i)
    if len(even_num) > len(odd_num):
        return odd_num, "odd numbers:"
    else:
        return even_num, "even numbers:"


user_list = []
n = int(input("Enter number of elements : "))
for x in range(0, n):
    ele = int(input())
    user_list.append(ele)
print("You have entered:", user_list)
outlier, num_type = find_outlier(user_list)
print("The outliers are", num_type, outlier)
