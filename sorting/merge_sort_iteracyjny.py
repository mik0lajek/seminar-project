import os
import time
import math
import random


def merge_sort_iterative(arr):
    #Sortowanie iteracyjne metodą merge sort. Działa na liście arr, modyfikuje ją bez zwracania nowej.

    n = len(arr)
    width = 1  # początkowa szerokość fragmentu do scalania
    while width < n:
        for i in range(0, n, 2*width):
            left = i
            mid = min(i + width, n)
            right = min(i + 2*width, n)
            merge(arr, left, mid, right)
        width *= 2  # zwiększamy szerokość fragmentu dwukrotnie
    return arr

def merge(arr, left, mid, right):
    #Funkcja pomocnicza do scalania dwóch posortowanych fragmentów tablicy arr: arr[left:mid] i arr[mid:right]

    L = arr[left:mid]
    R = arr[mid:right]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # kopiowanie pozostałych elementów z L
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    # kopiowanie pozostałych elementów z R
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


# Wczytywanie danych z pliku
def read_data(file_path):
    #Wczytuje wszystkie dane z pliku jako tekst. Każda linia pliku jest osobnym elementem listy.

    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(line.strip())
    return data

# Rozpoznanie typu danych
def detect_data_type(data):
    """
    Rozróżnia typ danych:
    1 - liczby całkowite (wszystkie cyfry)
    2 - teksty o stałej długości (różnica długości <= 2)
    3 - teksty o losowej długości (różnica długości > 2)
    0 - mieszane lub nieznany typ
    """
    if all(item.isdigit() for item in data):
        return 1  # liczby całkowite
    elif all(item.isalnum() for item in data):
        lengths = [len(s) for s in data]
        if max(lengths) - min(lengths) <= 2:
            return 2  # teksty o stałej długości
        else:
            return 3  # teksty o losowej długości
    else:
        return 0  # mieszane lub nieznany typ


# Przygotowanie wariantu danych
def prepare_data_variant(data, variant):
    """
    Tworzy kopię danych w określonym wariancie:
    - random: losowa kolejność
    - almost_sorted: prawie posortowane (kilka zamian)
    - almost_reverse: prawie odwrotnie posortowane
    - reverse: całkowicie odwrotnie posortowane
    """
    n = len(data)
    sorted_data = sorted(data)
    
    if variant == 'random':
        arr = data.copy()
        random.shuffle(arr)
        return arr
    
    elif variant == 'almost_sorted':
        arr = sorted_data.copy()
        swap_count = max(1, n // 20)  # 5% elementów zamieniamy
        for i in range(swap_count):
            arr[i], arr[-i-1] = arr[-i-1], arr[i]
        return arr
    
    elif variant == 'almost_reverse':
        arr = sorted_data[::-1]
        swap_count = max(1, n // 20)
        for i in range(swap_count):
            arr[i], arr[-i-1] = arr[-i-1], arr[i]
        return arr
    
    elif variant == 'reverse':
        return sorted_data[::-1]
    
    else:
        raise ValueError("Nieznana wariacja danych")


# Testowanie sortowania i generowanie raportu CSV
def test_sorting_lengths(data, data_type_name, lengths=[100, 500, 1000, 5000, 10000, 100000, 1000000, 10000000, 100000000]):
    #Testuje merge sort iteracyjny dla różnych długości danych i wariantów uporządkowania. Wyświetla szczegółowy raport CSV.

    variants = ['random', 'almost_sorted', 'almost_reverse', 'reverse']
    
    # Nagłówek CSV
    print(f"# Typ danych: {data_type_name}")
    print("Rozmiar;Wariant;Czas_s;O_n_log_n")
    
    for length in lengths:
        # Przycięcie lub powielanie danych do wymaganego rozmiaru
        if len(data) >= length:
            current_data = data[:length]
        else:
            current_data = data * (length // len(data) + 1)
            current_data = current_data[:length]
        
        # Teoretyczna złożoność O(n log n)
        theoretical = length * math.log2(length) if length > 0 else 0
        
        for variant in variants:
            arr = prepare_data_variant(current_data, variant)
            start_time = time.time()
            merge_sort_iterative(arr)
            end_time = time.time()
            elapsed = end_time - start_time
            
            # Wyświetlamy wynik w formacie CSV: Rozmiar;Wariant;Czas;Teoretyczne O(n log n)
            print(f"{length};{variant};{elapsed:.6f};{theoretical:.2f}")


# Główna część programu
if __name__ == "__main__":
    # Ścieżka do pliku Dane.txt na pulpicie
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop, "Dane.txt")

    # Wczytanie danych
    raw_data = read_data(file_path)

    # Rozpoznanie typu danych
    data_type = detect_data_type(raw_data)

    # Mapowanie typu na nazwę
    type_name = {1: "Liczby całkowite",
                 2: "Teksty o stałej długości",
                 3: "Teksty o losowej długości"}.get(data_type, "Nieznany typ")

    # Sprawdzenie poprawności danych
    if data_type == 0:
        print("Nieznany lub mieszany typ danych w pliku")
    else:
        # Generowanie szczegółowego raportu CSV
        test_sorting_lengths(raw_data, type_name)
