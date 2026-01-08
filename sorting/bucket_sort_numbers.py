from sorting.insertion_sort import insertion_sort

def bucket_sort_numbers(data, k):
    """
    Bucket sort dla liczb zapisanych jako napisy znaków.

    Parametry:
    - data: lista napisów reprezentujących liczby
    - k: liczba kubełków

    Zwraca:
    - posortowaną listę napisów
    - liczbę porównań
    """

    comparisons = 0

    # Konwersja na liczby całkowite (tylko do obliczeń)
    values = [int(x) for x in data]

    min_val = min(values)
    max_val = max(values)

    # Inicjalizacja kubełków
    buckets = [[] for _ in range(k)]

    if min_val == max_val:
        return data[:], comparisons

    # Rozdział elementów do kubełków (O(n))
    for x, v in zip(data, values):
        index = (v - min_val) * k // (max_val - min_val + 1)
        buckets[index].append(v)

    # Sortowanie kubełków
    result = []
    for bucket in buckets:
        comparisons += insertion_sort(bucket)
        result.extend(bucket)

    # Konwersja z powrotem na napisy
    result_str = [str(v) for v in result]

    return result_str, comparisons
