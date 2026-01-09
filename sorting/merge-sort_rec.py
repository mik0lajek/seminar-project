# Source: https://www.geeksforgeeks.org/dsa/merge-sort/
import time
from pathlib import Path

# Załadowanie danych z plików
def load_data(path, data_type):
    with open(path, "r", encoding="utf-8") as f:
        if data_type == "numeric":
            return [int(line.strip()) for line in f]
        else:
            return [line.strip() for line in f]

# Zapis posortowanej tablicy do pliku tekstowego
def save_sorted_array(path, arr):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for x in arr:
            f.write(str(x) + "\n")

# =========================
# Merge sort rekurencyjny
# =========================

# Zcalanie dwóch posortowanych części tablicy
def merge(arr, left, mid, right):

    # Ustawianie rozmiarów lewej i prawej części
    n1 = mid - left + 1
    n2 = right - mid

    # Tworzenie tablic pomocniczych
    L = [0] * n1
    R = [0] * n2

    # Kopiowanie danych z oryginalnej tablicy arr do L[] i R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    # Mergowanie tablic pomocniczych do oryginalnej tablicy
    while i < n1 and j < n2:    # dopóki oba podzbiory mają jeszcze elementy
        if L[i] <= R[j]:        # Porównywanie aktualnych elementów lewej i prawej tablicy
            arr[k] = L[i]       # Jeśli element z lewej tablicy jest mniejszy (lub równy), wstawiamy go do tablicy wynikowej
            i += 1
        else:
            arr[k] = R[j]       # W przeciwnym wypadku wstawiamy element z prawej tablicy
            j += 1

        # Przechodzimy do kolejnej pozycji w tablicy wynikowej
        k += 1

    # Jeśli w lewej tablicy zostały jeszcze elementy,
    # to są one już posortowane – przepisujemy je bez porównań
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Jeśli w prawej tablicy zostały jeszcze elementy,
    # również przepisujemy je bez porównań
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:    # Warunek stopu; jeśli są min. 2 elementy to dzieli dalej
        mid = (left + right) // 2   # Środek zakresu

        merge_sort(arr, left, mid)      # Rekurencyjnie wywołuje merge_sort() dla lewej części tablicy; left jest początkiem, mid końcem
        merge_sort(arr, mid + 1, right) # Rekurencyjnie wywołuje merge_sort() dla prawej części tablicy; mid+1 jest początkiem, right końcem
        merge(arr, left, mid, right)    # Scalanie


# Main
if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parents[1] # Katalog główny
    input_root = BASE_DIR / "input_data"           # Ścieżka wejściowa
    output_root = BASE_DIR / "output_data"         # Ścieżka wyjściowa

    # Iterowanie po podkatalogach
    for data_dir in sorted(input_root.iterdir()):
        if not data_dir.is_dir():
            continue

        txt_files = list(data_dir.glob("*.txt"))
        if not txt_files:
            continue  # pomijamy puste foldery

        data_type = data_dir.name   # Identyfikacja typu danych
        print(f"\n=== Processing data type: {data_type} ===")

        # Pliki wynikowe dla danego typu danych
        results_csv = output_root / f"results-{data_type}.csv"
        sorted_dir = output_root / f"sorted_{data_type}"

        # Zapisanie wyniku w postaci:
        # data_type_100-000; 2.0000
        with open(results_csv, "w", encoding="utf-8") as out:
            out.write("file_name;time\n")   # Nagłówek pliku CSV

            # Iteracja po pliku z danymi; wczytywanie danych
            for file_path in sorted(txt_files):
                print(f"  Sorting {file_path.name}")

                arr = load_data(file_path, data_type)   # Wczytywanie danych z pliku do tablicy

                start = time.perf_counter()             # Pomiar czasu przed rozpoczęciem sortowania
                merge_sort(arr, 0, len(arr) - 1)
                end = time.perf_counter()               # Pomiar czasu po zakończeniu sortowania

                elapsed = end - start   # Czas sortowania w sekundach
                out.write(f"{file_path.name};{elapsed:.6f}\n")  # Zapis wyniku do pliku

                # zapis posortowanej tablicy
                sorted_path = sorted_dir / f"sorted_{file_path.name}"
                save_sorted_array(sorted_path, arr)