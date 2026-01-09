# generators/sosinski/utils.py
from pathlib import Path
import random

# katalog główny projektu: seminar-project/
BASE_DIR = Path(__file__).resolve().parents[2]

# Tworzenie prawie posortowanej listy
# Bierze posortowaną, zamienia losowo swaps elementów
# TODO
# swapowanie 10% pliku, nie stalej liczby
def nearly_sorted(arr, swaps=5):
    arr = arr.copy()    # Tworzy kopię listy
    n = len(arr)

    # Wykonuje swaps zamian miejscami
    for _ in range(swaps):
        i, j = random.sample(range(n), 2)   # Losowanie dwóch różnych indeksów
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# Tworzenie wszystkich wariantów danych
def generate_all_variants(data):
    sorted_data = sorted(data)  # Tworzenie nowej posortowanej rosnąco listy

    # Słownik wariantów
    return {
        "random": data,     # Oryginalne dane
        "nearly_sorted": nearly_sorted(sorted_data), # Prawie posortowane
        "nearly_reverse": nearly_sorted(sorted_data[::-1]), # Prawie posortowane odwrotnie
        "reverse": sorted_data[::-1]    # Posortowane malejąco
    }

# Zamienia liczbę na format z separatorami tysięcy (wykorzystanie przy generowaniu nazw plików)
def format_size(n):
    return f"{n:,}".replace(",", "-")

# Zapisywanie do pliku tekstowego; jedna wartość na jedną linię
def save_to_file(relative_path, data):
    """
    relative_path np. 'input_data/numeric/random.txt'
    """
    path = BASE_DIR / relative_path # Tworzenie pełnej ścieżki pliku

    # Tworzy katalog, jeśli nie istnieje
    path.parent.mkdir(parents=True, exist_ok=True)

    # Otwieranie pliku w trybie zapisu
    with open(path, "w", encoding="utf-8") as f:
        for x in data:
            f.write(str(x) + "\n")  # Każdy element listy zamieniany jest na string; jest zapisany w osobnej linii
