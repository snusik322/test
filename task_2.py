def transpose_matrix(matrix):
    return [
        [matrix[0][0], matrix[1][0]],
        [matrix[0][1], matrix[1][1]]
    ]

def input_matrix_two_lists():
    print("Введите первую строку матрицы:")
    row1 = list(map(int, input().split()))
    print("Введите вторую строку матрицы:")
    row2 = list(map(int, input().split()))
    return [row1, row2]

def input_matrix_one_list():
    print("Введите 4 числа матрицы через пробел:")
    elements = list(map(int, input().split()))
    return [elements[:2], elements[2:]]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


print("Выберите способ задания матрицы:")
print("1. Двумя списками ")
print("2. Одним списком ")
choice = input("Ваш выбор: ")

if choice == '1':
    matrix = input_matrix_two_lists()
elif choice == '2':
    matrix = input_matrix_one_list()
else:
    print("Неверный выбор. Завершение программы.")
    exit()

print("\nИсходная матрица:")
print_matrix(matrix)

transposed = transpose_matrix(matrix)
print("\nТранспонированная матрица:")
print_matrix(transposed)