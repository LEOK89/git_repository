# -*- coding: iso-8859-15 -*-

# Scrivere un algoritmo che, dato un numero,
# ne mostri la sua rappresentazione a lettere in italiano
# Esempio:
#   input: 1234 -> output: milleduecentotrentaquattro
#
# Come funziona?
# Per i primi venti numeri, non c'è altra strada che quella
# di prevedere una traduzione semplice attraverso una tabella:
# 0 -> zero, 1 -> uno, 2 -> due, ..., 19 -> diciannove

def __translate_to_20(n): 
    # le funzioni il cui nome inizia con due underscore (__)
    # non sono accessibili al di fuori del file nel quale sono inserite
    if n > 19:
        return "Out of range"

    NUMBERS = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette",
               "otto", "nove", "dieci", "undici", "dodici", "tredici",
               "quattordici", "quindici", "sedici", "diciassette",
               "diciotto", "diciannove"]
    return NUMBERS[n]

# dal 20, fino al 100 (escluso), ho la possibilità di prevedere
# una "traduzione" della decina e demandare la "traduzione"
# dell'unità alla funzione che traduce fino a 20
# 25 -> decina = 2, unità = 5


def __translate_to_100(n):
    if n < 20:
        return __translate_to_20(n)
    if n > 99:
        return "Out of range"
    DECADES = ["venti", "trenta", "quaranta", "cinquanta", "sessanta",
               "settanta", "ottanta", "novanta"]
    decade = n // 10  # la decina da n
    unit = n % 10  # l'unità di n
    return DECADES[decade-2] + __translate_to_20(unit)


def __translate_to_1000(n):
    if n < 100:
        return __translate_to_100(n)
    if n > 999:
        return "Out of range"
    hundreds = n // 100
    decades = n % 100
    if hundreds > 1:  # se le centinaia sono più di 1 traduci pure le centinaia
        return __translate_to_20(hundreds) + "cento" + __translate_to_100(decades)
    # altrimenti scrivi solo cento

    return "cento" + __translate_to_100(decades)


def __translate_others(n):
    if n < 100:
        return __translate_to_1000(n)
    thousands = n // 1000
    remaining = n % 1000
    if thousands > 1:
        return __translate_to_1000(thousands) + "mila" + __translate_to_1000(remaining)
    return "mille" + __translate_to_1000(remaining)


def translate_number(n):
    if (n == 0):
        return "zero"
    if (n < 0):
        return "meno " + translate_number(-n)
    result = __translate_others(n).replace('iu', 'u').replace(
        'io', 'o').replace('au', 'u').replace('ao', 'o')
    return result


# for x in range(1, 1000000):
#     print(translate_number(x))