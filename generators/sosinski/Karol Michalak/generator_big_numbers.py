import random
from typing import List, Optional

# Warianty danych
VARIANTS = ["random", "almost_sorted", "almost_sorted_reverse"]


def _partial_sort_safe(seq: List[int], variant: str) -> List[int]:
    """
    Częściowo sortuje fragment listy cyfr.

    Zasady:
    - pierwsza cyfra (indeks 0) NIE jest modyfikowana,
    - nie zmienia się rząd wielkości liczby,
    - zachowany zostaje rozkład kubełków.
    """
    if variant == "random" or len(seq) < 3:
        return seq

    n = len(seq)

    # Modyfikujemy tylko fragment od indeksu >= 1
    start = random.randint(1, n // 2)
    end = random.randint(start + 1, n)

    fragment = seq[start:end]

    if variant == "almost_sorted":
        fragment.sort()
    elif variant == "almost_sorted_reverse":
        fragment.sort(reverse=True)

    seq[start:end] = fragment
    return seq


def generate_big_number_uniform_almost_sorted(
    length: int,
    random_length: bool = False,
    min_len: Optional[int] = None,
    max_len: Optional[int] = None
) -> List[int]:
    """
    Generuje bardzo dużą liczbę jako listę cyfr (list[int]).

    DOMYŚLNIE:
    - stała długość `length`

    OPCJONALNIE:
    - random_length=True → losowa długość z zakresu [min_len, max_len]

    UWAGI:
    - brak wiodącego zera,
    - cyfry 0–9,
    - lokalne uporządkowanie (almost sorted),
    - przeznaczone do sortowania jako struktury danych.
    """

    # 🔹 Opcjonalna losowa długość
    if random_length:
        if min_len is None or max_len is None:
            raise ValueError(
                "Dla random_length=True należy podać min_len oraz max_len"
            )
        length = random.randint(min_len, max_len)

    if length < 1:
        raise ValueError("Długość liczby musi być >= 1")

    # 🔹 Pierwsza cyfra: 1–9 (brak wiodącego zera)
    first_digit = random.randint(1, 9)

    # 🔹 Pozostałe cyfry: 0–9
    remaining_digits = [random.randint(0, 9) for _ in range(length - 1)]

    digits = [first_digit] + remaining_digits

    # 🔹 Lokalny wariant uporządkowania
    variant = random.choice(VARIANTS)
    digits = _partial_sort_safe(digits, variant)

    return digits
