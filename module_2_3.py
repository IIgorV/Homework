my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive = []
index = 0
while index < len(my_list):
    number = (input('Введите число: '))
    if my_list[index] < 0:
        print('not positive numbers')
        break
    positive.append(my_list[index])
    index += 1
