def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def main():
    input_sequence = input("Введите последовательность чисел через пробел : ")
    input_sequence = list(map(int, input_sequence.split()))

    try:
        user_number = int(input("Введите любое число: "))
    except ValueError:
        print("Ошибка: Введено некорректное число!")
        return

    sorted_sequence = sorted(input_sequence)
    position = binary_search(sorted_sequence, user_number)

    if position == len(sorted_sequence):
        print("Введенное число больше всех чисел в последовательности.")
    else:
        print(f"Найдено место вставки числа: {position}")
        print(f"Число, меньшее: {sorted_sequence[position - 1]}, число, большее или равное: {sorted_sequence[position]}")

if __name__ == "__main__":
    main()
