def get_matrix(n, m, value):
    # Создаем пустую матрицу внутри ger_matrix
    matrix = []
    # Внешний цикл для строк
    for i in range(n):
        row = []
        # Внутренний цикл для столбцов
        for i in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

# Пример использования функции
n = get_matrix(2,2,10)
m = get_matrix(3,5,42)
value = get_matrix(4,2,13)
print(n)
print(m)
print(value)
