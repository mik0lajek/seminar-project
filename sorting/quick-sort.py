def quickSort(tab, poczatek, koniec):
    if poczatek < koniec: # sprawdzenie czy tablica ma więcej niż jeden element
        pivot = podzial(tab, poczatek, koniec) # podział tablicy i uzyskanie indeksu pivotu
        # elementy zostają podzielone na dwie części: mniejsze i większe od pivotu

        quickSort(tab, poczatek, pivot - 1) # rekurencyjne wywołanie quickSort dla lewej części tablicy
        quickSort(tab, pivot + 1, koniec) # rekurencyjne wywołanie quickSort dla prawej części tablicy

def podzial(tab, poczatek, koniec): # funkcja pomocnicza do podziału tablicy
    pivot = tab[koniec] # ustawienie pivotu na ostatni element

    i = poczatek - 1 # ustawienie indeksu i na początek - 1, będzie używany przy zamianie elementów

    for j in range(poczatek, koniec): # iteracja przez tablicę od poczatku do konca - 1
        if tab[j] < pivot:
            # jeśli element jest mniejszy niż pivot, zwiększ indeks i oraz zamień elementy na indeksach i oraz j
            i += 1

            tab[i], tab[j] = tab[j], tab[i] # zamiana miejscami elementów i oraz j

    tab[i + 1], tab[koniec] = tab[koniec], tab[i + 1] # zamiana pivotu z elementem na indeksie i + 1 (pomiędzy mniejszymi i większymi elementami)

    return i + 1 # zwrócenie nowego indeksu pivotu