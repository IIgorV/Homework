# Дан список
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# 1 Создаем пустые списки для простых и не простых чисел
primes = []
not_primes = []

for num in numbers:
    # Проверяем на простоту
    is_prime = True
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

print("Простые числа:")
print(primes)
print()
print("Не простые числа:")
print(not_primes)