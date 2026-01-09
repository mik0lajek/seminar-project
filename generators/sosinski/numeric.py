# generators/sosinski/numeric.py
import random
from utils import generate_all_variants, save_to_file, format_size

# Generowanie listy n liczb całkowitych (wartosci od 0 do 2^31 - 1 (miesci sie w slowie maszynowym))
def generate_numeric(n, min_val=0, max_val=2**31 - 1):
    return [random.randint(min_val, max_val) for _ in range(n)]

if __name__ == "__main__":
    SIZES = [100_000, 1_000_000, 10_000_000]    # Lista rozmiarów danych

    # Pętla generująca dane dla każdego rozmiaru
    for n in SIZES:
        print(f"Generating numeric data, n={n}")
        data = generate_numeric(n)
        variants = generate_all_variants(data)

        size_str = format_size(n)

        # Zapis poszczególnych wariantów do osobnych plików
        for name, arr in variants.items():
            filename = f"input_data/numeric/{name}_{size_str}.txt"
            save_to_file(filename, arr)
