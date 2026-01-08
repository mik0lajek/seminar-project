def insertion_sort(arr):
    """
    Algorytm insertion sort.
    Zwraca liczbę porównań wykonanych podczas sortowania.
    """
    comparisons = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Przesuwanie elementów większych od klucza
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        arr[j + 1] = key

    return comparisons
