roman_numbers = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
                 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}


def decimal_to_roman(num):
    if num == 0:
        return ""
    for number in reversed(list(roman_numbers.keys())):
        coefficient = int(num/number)
        if coefficient > 0:
            amount = coefficient*roman_numbers[number]
            return str(amount) + str(decimal_to_roman(num - coefficient*number))


def letters_in_roman(num_roman):
    general = []
    for character in num_roman:
        if character not in general:
            general.append(character)

    return list(reversed(sorted(general)))
