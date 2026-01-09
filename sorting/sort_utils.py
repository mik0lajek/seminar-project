# generators/sosinski/utils.py
from pathlib import Path
import random

# katalog główny projektu: seminar-project/
BASE_DIR = Path(__file__).resolve().parents[1]

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
