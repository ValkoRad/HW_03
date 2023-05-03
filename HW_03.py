def sort(array): # Сортировка по возрастанию
    for i in range(len(array) - 1):
        idx_max = i
        for j in range(i, len(array)):
            if array[j] < array[idx_max]:
                idx_max = j
        if i != idx_max:
            array[i], array[idx_max] = array[idx_max], array[i]
    return array


def binary_search(array, element, left, right): # Двоичный поиск
    if element < array[0]:
        return False
    if left > right:
        return right

    middle = (right + left) // 2
    if (array[middle] == element) or (array[middle-1] < element <= array[middle]):
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

try: # Отлов ошибки при вводе
    array = list(map(int, input('Введите целые числа через пробел:\n').split()))
except ValueError:
    print("Нужно вводить только целые числа, перезапустите программу")
else:
    print('Отсортированный список:  ', sort(array))
    print('Индексы элементов:       ', [i for i in range(len(array))])
    element = int(input('Введите любое целое число: '))
    result = binary_search(array, element, 0, len(array) - 1)


    if not result and isinstance(result, bool):
        print("Введенное число меньше нулевого элемента списка")
    elif result == -1:
        print("Введенное число совпадает с нулевым элементом списка")
    elif result == len(array) - 1:
        print("Введенное число больше последнего (%d - го) элемента списка" % (len(array) - 1))
    else:
        print("Индекс элемента, который меньше введенного числа:", result)
