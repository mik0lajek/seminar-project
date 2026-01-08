import random
import string

# Dozwolone cyfry (0–9)
DIGITS = string.digits

# Warianty generowania danych
VARIANTS = ["random", "almost_sorted", "almost_sorted_reverse"]


def _partial_sort_safe(seq, variant):
    """
    Wykonuje częściowe sortowanie fragmentu sekwencji cyfr.

    UWAGA:
    - Nigdy nie modyfikuje pierwszej cyfry (indeks 0),
      aby nie zmieniać rzędu wielkości liczby.
    - Dzięki temu zachowany jest jednorodny rozkład wartości,
      korzystny dla algorytmu bucket sort.
    """
    if variant == "random":
        return seq

    n = len(seq)

    # Losujemy fragment WYŁĄCZNIE od indeksu >= 1
    start = random.randint(1, n // 2)
    end = random.randint(start + 2, n)

    fragment = seq[start:end]

    if variant == "almost_sorted":
        fragment.sort()
    elif variant == "almost_sorted_reverse":
        fragment.sort(reverse=True)

    seq[start:end] = fragment
    return seq


def generate_number_uniform_almost_sorted(
    length: int,
    random_length: bool = False,
    min_len: int | None = None,
    max_len: int | None = None
) -> str:
    """
    Generuje liczbę jako napis znaków.

    DOMYŚLNIE:
    - zachowuje dotychczasowe zachowanie (stała długość)

    OPCJONALNIE:
    - random_length=True → losowa długość z przedziału [min_len, max_len]
    """

    # 🔹 NOWA FUNKCJONALNOŚĆ (opcjonalna)
    if random_length:
        if min_len is None or max_len is None:
            raise ValueError(
                "Dla random_length=True należy podać min_len oraz max_len"
            )
        length = random.randint(min_len, max_len)

    # 🔹 DOTYCHCZASOWA LOGIKA (BEZ ZMIAN)
    first_digit = random.choice("123456789")
    remaining_digits = [random.choice(DIGITS) for _ in range(length - 1)]

    digits = [first_digit] + remaining_digits
    variant = random.choice(VARIANTS)
    digits = _partial_sort_safe(digits, variant)

    return "".join(digits)
