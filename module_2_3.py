my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_numbers = []
index = 0
while index < len(my_list):
    number = my_list[index]
    if number > 0:
        positive_numbers.append(number)
        index += 1
    else:
        index += 1
        continue
    if number < 0 or index == len(my_list):
        break
print("Положительные числа:", positive_numbers)