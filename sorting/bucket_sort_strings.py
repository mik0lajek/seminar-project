from sorting.insertion_sort import insertion_sort

def bucket_sort_strings(data):
    """
    Bucket sort dla napisów znakowych.

    Bucketowanie:
    - po pierwszym znaku (alfabet łaciński)

    Zwraca:
    - posortowaną listę napisów
    - liczbę porównań
    """

    comparisons = 0
    ALPHABET_SIZE = 26

    # Inicjalizacja kubełków
    buckets = [[] for _ in range(ALPHABET_SIZE)]

    # Rozdział napisów do kubełków
    for s in data:
        index = ord(s[0]) - ord('a')
        buckets[index].append(s)

    # Sortowanie kubełków leksykograficznie
    result = []
    for bucket in buckets:
        comparisons += insertion_sort(bucket)
        result.extend(bucket)

    return result, comparisons
