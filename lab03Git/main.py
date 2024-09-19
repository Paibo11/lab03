# Функция для реализации сортировки пузырьком
def bubble_sort(arr, ascending=True):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n-i-1):
            # Меняем элементы местами в зависимости от направления сортировки
            if ascending:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

# Ввод чисел с клавиатуры
n = int(input("Введите количество чисел: "))
arr = []

for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    arr.append(num)
bubble_sort(arr)
print("Отсортированные числа: ", arr)
