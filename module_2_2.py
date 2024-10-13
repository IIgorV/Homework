first = input('Введите любое произвольное число: ')
second = input('Введите любое произвольное число: ')
third = input('Введите любое произвлоьное число: ')
if first == second and second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')
