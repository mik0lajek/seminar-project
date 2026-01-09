import random
import string
import os

# USTAWIENIA PROGRAMU


# Liczba elementów w każdym zbiorze
LICZBA_LICZB = 20_000_000        # liczby całkowite
LICZBA_NAPISOW_STALYCH = 20_000_000  # napisy stałe
LICZBA_NAPISOW_LOSOWYCH = 20_000_000 # napisy losowe


# Długości napisów
DLUGOSC_STALA = 15
DLUGOSC_MIN = 1
DLUGOSC_MAX = 15

# Zbiór znaków: cyfry + małe litery łacińskie
ZNAKI = string.digits + string.ascii_lowercase

# ŚCIEŻKA DO PLIKU NA PULPICIE

# Pobranie ścieżki do pulpitu użytkownika
sciezka_pulpit = os.path.join(os.path.expanduser("~"), "Desktop")

# Pełna ścieżka do pliku wyjściowego
sciezka_pliku = os.path.join(sciezka_pulpit, "Dane.txt")

# FUNKCJE GENERUJĄCE DANE

def generuj_liczby(ile):
    """
    Generuje listę losowych liczb całkowitych.
    Zakładamy zakres 32-bitowy.
    """
    return [random.randint(0, 2**31 - 1) for _ in range(ile)]


def generuj_napisy_stale(ile, dlugosc):
    """
    Generuje listę napisów o stałej długości.
    """
    return [
        ''.join(random.choice(ZNAKI) for _ in range(dlugosc))
        for _ in range(ile)
    ]


def generuj_napisy_losowe(ile, min_dlugosc, max_dlugosc):
    """
    Generuje listę napisów o losowej długości.
    """
    return [
        ''.join(
            random.choice(ZNAKI)
            for _ in range(random.randint(min_dlugosc, max_dlugosc))
        )
        for _ in range(ile)
    ]

# GENEROWANIE DANYCH

print("Generowanie liczb...")
liczby = generuj_liczby(LICZBA_LICZB)

print("Generowanie napisów o stałej długości...")
napisy_stale = generuj_napisy_stale(
    LICZBA_NAPISOW_STALYCH,
    DLUGOSC_STALA
)

print("Generowanie napisów o losowej długości...")
napisy_losowe = generuj_napisy_losowe(
    LICZBA_NAPISOW_LOSOWYCH,
    DLUGOSC_MIN,
    DLUGOSC_MAX
)

# ZAPIS DO PLIKU

print("Zapisywanie danych do pliku...")

with open(sciezka_pliku, "w", encoding="utf-8") as plik:
    # Sekcja 1: liczby
    for x in liczby:
        plik.write(f"{x}\n")

    # Sekcja 2: napisy stałej długości
    for s in napisy_stale:
        plik.write(f"{s}\n")

    # Sekcja 3: napisy losowej długości
    for s in napisy_losowe:
        plik.write(f"{s}\n")

print(f"Gotowe! Dane zapisane w pliku:\n{sciezka_pliku}")
