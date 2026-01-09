# generators/sosinski/numeric.py
import random
import string
from utils import generate_all_variants, save_to_file, format_size

ALPHABET = string.digits + string.ascii_lowercase   # Alfabet służący do budowy stringów

# Generowanie stringów o stałej długości
def generate_fixed_strings(n, length=12):
    return [
        ''.join(random.choices(ALPHABET, k=length))
        for _ in range(n)
    ]

if __name__ == "__main__":
    SIZES = [100_000, 1_000_000, 10_000_000]    # Lista rozmiarów danych

    # Pętla generująca dane dla każdego rozmiaru
    for n in SIZES:
        print(f"Generating numeric data, n={n}")
        data = generate_fixed_strings(n)
        variants = generate_all_variants(data)

        size_str = format_size(n)

        # Zapis poszczególnych wariantów do osobnych plików
        for name, arr in variants.items():
            filename = f"input_data/string_fixed/{name}_{size_str}.txt"
            save_to_file(filename, arr)
