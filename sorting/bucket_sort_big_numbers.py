from sorting.insertion_sort import insertion_sort

def bucket_sort_big_numbers(data):
    """
    Bucket sort dla bardzo dużych liczb zapisanych jako listy cyfr.

    Przykład liczby:
    [9, 0, 4, 1, 7, 2]

    Bucketowanie:
    - po pierwszej cyfrze (1–9)

    Zwraca:
    - posortowaną listę liczb (list cyfr)
    - liczbę porównań
    """

    comparisons = 0

    # Kubełki dla cyfr 0–9
    buckets = [[] for _ in range(10)]

    # Rozdział do kubełków
    for number in data:
        first_digit = number[0]
        buckets[first_digit].append(number)

    # Sortowanie kubełków
    result = []
    for bucket in buckets:
        comparisons += insertion_sort(bucket)
        result.extend(bucket)

    return result, comparisons
