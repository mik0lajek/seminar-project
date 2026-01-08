import random

output_folder = "./output_data/sorted/"
characters_path = "./generators/ryba/znaki.txt"
characters_file = open(characters_path, 'r')

characters = list(characters_file.read().strip());

def generate_numbers(n, min_length=1, max_length=9): # generowanie tablicy n liczb losowych o długości od min_length do max_length
    return [(random.randint(10 ** (min_length-1), 10 ** max_length - 1) * (-1 * random.choice([-1, 1]))) for _ in range(n)]


def generate_strings(n, min_length=1, max_length=9): # generowanie tablicy n losowych stringów o długości od min_length do max_length
    strings = []

    for _ in range(n):
        length = random.randint(min_length, max_length)
        s = ''.join(random.choices(characters, k=length))
        strings.append(s)

    return strings


def sort(numbers, reverse = False): # sortowanie liczb
    return sorted(numbers, reverse=reverse)


def semi_sort(numbers, percent_sorted = 90, reverse = False): # częściowe sortowanie tablicy liczb
    n = len(numbers)

    sorted_count = int(n * percent_sorted / 100)

    sorted_part = sort(numbers[:sorted_count], reverse=reverse)
    unsorted_part = numbers[sorted_count:]

    if reverse:
        return unsorted_part + sorted_part
    
    return sorted_part + unsorted_part


def save_numbers_to_file(numbers, filename): #zapis do pliku
    with open(output_folder + filename, 'w') as f:
        for number in numbers:
            f.write(str(number) + '\n')


numbers = generate_numbers(1000000, 20, 20)
save_numbers_to_file(numbers, "big_numbers_unsorted.txt")

numbers2 = generate_numbers(1000000, 20, 20)
numbers2 = semi_sort(numbers2, 90)
save_numbers_to_file(numbers2, "big_numbers_semi_sorted.txt")

numbers3 = generate_numbers(1000000, 20, 20)
numbers3 = semi_sort(numbers3, 90, True)
save_numbers_to_file(numbers3, "big_numbers_semi_sorted_desc.txt")

numbers4 = generate_numbers(1000000, 1, 9)
save_numbers_to_file(numbers4, "small_numbers_unsorted.txt")

numbers5 = generate_numbers(1000000, 1, 9)
numbers5 = semi_sort(numbers5, 90)
save_numbers_to_file(numbers5, "small_numbers_semi_sorted.txt")

numbers6 = generate_numbers(1000000, 1, 9)
numbers6 = semi_sort(numbers6, 90, True)
save_numbers_to_file(numbers6, "small_numbers_semi_sorted_desc.txt")

strings = generate_strings(1000000, 5, 20)
save_numbers_to_file(strings, "strings_unsorted.txt")

strings2 = generate_strings(1000000, 5, 20)
strings2 = semi_sort(strings2, 90)
save_numbers_to_file(strings2, "strings_semi_sorted.txt")

strings3 = generate_strings(1000000, 5, 20)
strings3 = semi_sort(strings3, 90, True)
save_numbers_to_file(strings3, "strings_semi_sorted_desc.txt")