import random
import string
import time
import sys
import os
from pathlib import Path

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort_benchmark(arr):
    """
    Wersja algorytmu do testów wydajności.
    """
    n = len(arr)

    # Budowanie kopca
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Sortowanie właściwe
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

class DataGenerator:
    def __init__(self):
        self.chars = string.ascii_lowercase + string.digits

    def generate_integers(self, size):
        # Wartości mieszczące się w słowie komputera (np. 64-bit int)
        return [random.randint(-2**60, 2**60) for _ in range(size)]

    def generate_strings_fixed(self, size, length=15):
        data = []
        for _ in range(size):
            s = ''.join(random.choices(self.chars, k=length))
            data.append(s)
        return data

    def generate_strings_variable(self, size, min_len=5, max_len=15):
        data = []
        for _ in range(size):
            length = random.randint(min_len, max_len)
            s = ''.join(random.choices(self.chars, k=length))
            data.append(s)
        return data

    def apply_distribution(self, data, dist_type):
        """
        Modyfikuje dane zgodnie z zadaną charakterystyką.
        dist_type: 'random', 'sorted', 'reverse', 'nearly_sorted', 'nearly_reverse'
        """
        if dist_type == 'random':
            return data # Dane są już losowe z generatora
        
        elif dist_type == 'sorted':
            data.sort()
            return data
            
        elif dist_type == 'reverse':
            data.sort(reverse=True)
            return data
            
        elif dist_type == 'nearly_sorted':
            data.sort()
            self._swap_random(data, percentage=0.01) # Zamień 1% elementów
            return data
            
        elif dist_type == 'nearly_reverse':
            data.sort(reverse=True)
            self._swap_random(data, percentage=0.01)
            return data
            
        return data

    def _swap_random(self, data, percentage):
        n = len(data)
        swaps = int(n * percentage)
        for _ in range(swaps):
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            data[i], data[j] = data[j], data[i]

def save_to_file(data, filename, subfolder="generated_data"):
    """
    Zapisuje dane do katalogu input_data/{subfolder}/.
    """
    # Ustalanie ścieżki względem pliku skryptu: ../../input_data
    base_dir = Path(__file__).resolve().parents[2]
    target_dir = base_dir / "input_data" / subfolder
    
    # Tworzenie katalogu jeśli nie istnieje
    target_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = target_dir / filename
    
    print(f"Zapisywanie: {file_path}")
    with open(file_path, "w", encoding="utf-8") as f:
        for item in data:
            f.write(str(item) + "\n")

def run_generation():
    generator = DataGenerator()
    
    # Konfiguracja generowania (zmniejszona liczba dla testów plików, 
    # w produkcji można zwiększyć)
    SIZES = [10_000, 100_000] 
    
    # Mapowanie nazw typów do funkcji generatora
    data_types = [
        ('integers', lambda n: generator.generate_integers(n)),
        ('strings_fixed', lambda n: generator.generate_strings_fixed(n, 15)),
        ('strings_variable', lambda n: generator.generate_strings_variable(n, 5, 20))
    ]
    
    distributions = [
        'random', 
        'nearly_sorted', 
        'nearly_reverse', 
        'reverse'
    ]

    print("Rozpoczynam generowanie plików danych...")
    
    for n in SIZES:
        for dtype_name, gen_func in data_types:
            # Generujemy bazę
            base_data = gen_func(n)
            
            for dist in distributions:
                # Kopia i dystrybucja
                current_data = base_data[:]
                current_data = generator.apply_distribution(current_data, dist)
                
                # Nazwa pliku zgodna z konwencją: typ_dystrybucja_rozmiar.txt
                # np. integers_random_10000.txt
                filename = f"{dtype_name}_{dist}_{n}.txt"
                
                save_to_file(current_data, filename)

    print("Generowanie zakończone pomyślnie.")

if __name__ == "__main__":
    # Zwiększ limit rekurencji (pozostałość po HeapSort, nie zaszkodzi)
    sys.setrecursionlimit(2000000)
    
    print("Tryb pracy: Generator Danych Plikowych")
    run_generation()
