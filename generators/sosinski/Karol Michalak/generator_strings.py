import random
import string

# Alfabet – tylko małe litery (jednorodny rozkład)
ALPHABET = string.ascii_lowercase

# Warianty danych
VARIANTS = ["random", "almost_sorted", "almost_sorted_reverse"]


def _partial_sort_safe(seq, variant):
    """
    Wykonuje częściowe sortowanie fragmentu napisu.

    Zasady:
    - pierwszy znak (indeks 0) NIE jest modyfikowany,
    - zachowany zostaje rozkład kubełków,
    - modyfikujemy tylko środkową część napisu.
    """
    if variant == "random":
        return seq

    n = len(seq)

    # Nie dotykamy pierwszego znaku
    start = random.randint(1, n // 2)
    end = random.randint(start + 2, n)

    fragment = seq[start:end]

    if variant == "almost_sorted":
        fragment.sort()
    elif variant == "almost_sorted_reverse":
        fragment.sort(reverse=True)

    seq[start:end] = fragment
    return seq


def generate_string_uniform_almost_sorted(
    length: int,
    random_length: bool = False,
    min_len: int | None = None,
    max_len: int | None = None
) -> str:
    """
    Generuje napis znakowy.

    DOMYŚLNIE:
    - stała długość (jak dotychczas)

    OPCJONALNIE:
    - random_length=True → losowa długość z [min_len, max_len]
    """

    # 🔹 NOWA FUNKCJONALNOŚĆ (opcjonalna)
    if random_length:
        if min_len is None or max_len is None:
            raise ValueError(
                "Dla random_length=True należy podać min_len oraz max_len"
            )
        length = random.randint(min_len, max_len)

    # 🔹 DOTYCHCZASOWA LOGIKA (BEZ ZMIAN)
    chars = [random.choice(ALPHABET) for _ in range(length)]

    variant = random.choice(VARIANTS)
    chars = _partial_sort_safe(chars, variant)

    return "".join(chars)
