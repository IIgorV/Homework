my_string = input("Я сегодня смогу сделать домашнюю работу? ")
if my_string == 'Да' or my_string == 'да' or my_string == 'yes':
    print('Молодец')
elif my_string == 'Нет' or my_string == 'нет' or my_string == 'no':
    print('Ты все сможешь тигр =)')
else:
    print('Ответ должен быть "да" или "нет"')

my_string = ("учить новое в кайф")
print(my_string.upper())
my_string = ("УЧИТЬ НОВОЕ В КАЙФ")
print(my_string.lower())
my_string = ("учить новое в кайф")
print(my_string.replace(' ', ''))
my_string = ("учить новое в кайф")
print(my_string.replace('у', 'У'))
my_string = ("учить новое в кайф")
print(my_string.replace('ф', 'Ф'))