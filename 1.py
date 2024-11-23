def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    arr = list(map(int, input("Введите 10 элементов списка через пробел: ").split()))
    if len(arr) != 10:
        print("Пожалуйста, введите ровно 10 элементов.")
        return
    
    print("Выберите метод сортировки:")
    print("1. Пузырьковая сортировка")
    print("2. Сортировка выбором")
    print("3. Сортировка вставками")
    
    choice = input("Введите номер метода сортировки (1/2/3): ")
    
    if choice == '1':
        sorted_arr = bubble_sort(arr)
    elif choice == '2':
        sorted_arr = selection_sort(arr)
    elif choice == '3':
        sorted_arr = insertion_sort(arr)
    else:
        print("Неверный выбор.")
        return
    
    print("Отсортированный список:", sorted_arr)

if __name__ == "__main__":
    main()