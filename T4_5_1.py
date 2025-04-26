import random
import timeit

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    # Пример использования:
print('Фибоначи:', fibonacci(6))  # Вывод: 8

# Напишите рекурсивную функцию для нахождения максимального
# элемента в списке, используя подход "Разделяй и властвуй"

from random import randint

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

arr = []
for i in range(10):
    arr.append(randint(0, 10))
a = len(arr)

print('Исходный список ', arr)
print('Отсортированный список ', merge_sort(arr))
print('Максимальное число списка:',arr[a-1])

# Напишите функцию для реализации быстрой сортировки
# (QuickSort) с примером использования
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2] # список делится на 3 части правая часть, левая часть и pivot
        left = []
        right = []
        middle = []
        for i in arr:
            if i > pivot: # сравниваем значение из списка с pivot
                right.append(i) # если значение больше, то помещаем его в правую часть
            elif i < pivot:
                left.append(i) # если значение меньше, то помещаем его в левую часть
            else:
                middle.append(i)
        # left=[0,3,2] right=[55, 44] middle=88
        return quick_sort(left)+ middle+ quick_sort(right)

print('Отсортированный список с помощью QuickSort ', quick_sort([0, 3, 2, 88, 55, 44]))
print()

# Проанализируйте время выполнения быстрой сортировки на списках различной длины (например, 10, 100, 1000 элементов)
# и сравните её с другими сортировками, такими как сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


list_sizes = [10, 100, 1000, 5000]  # Добавим размер для лучшего сравнения

def quick_sort_time(arr):
    quick_sort(arr.copy())  # Сортирую копию, чтобы не изменять исходный список

def insertion_sort_time(arr):
    insertion_sort(arr.copy())  # Сортирую копию, чтобы не изменять исходный список


print("__________________________________________________")
print("List Size | Quicksort Time | Insertion Sort Time |")
print("----------|----------------|---------------------|")

for size in list_sizes:
    arr = [random.randint(0, 1000) for _ in range(size)]  # создаю список случайных чисел
    # print(arr)  #  Убрали вывод, т.к. он не нужен для больших списков

    quick_sort_time_take = timeit.timeit(stmt = lambda: quick_sort_time(arr), number=100) # Измеряем время выполнения Quicksort
    insertion_sort_take = timeit.timeit(stmt = lambda: insertion_sort_time(arr), number=100) # Измеряем время выполнения Insertion Sort

    print(f"{size:10}| {quick_sort_time_take:15f}| {insertion_sort_take:20f}|")