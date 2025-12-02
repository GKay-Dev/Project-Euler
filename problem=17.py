# Number Letter Counts - https://projecteuler.net/problem=17

def number_to_words(n):
    if n == 0:
        return "zero"

    ones = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ]
    teens = [
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
    ]
    tys = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
    ]
    hundreds = "hundred"
    thousand = "thousand"
    words = ""
    if n >= 1000:
        words += ones[n // 1000] + thousand
        n %= 1000
    if n >= 100:
        words += ones[n // 100] + hundreds
        n %= 100
        if n > 0:
            words += "and"
    if n >= 20:
        words += tys[n // 10]
        n %= 10
    elif n >= 10:
        words += teens[n - 10]
        n = 0
    if n > 0:
        words += ones[n]
    return words

def count_letters_in_numbers(limit):
    total_letters = 0
    for i in range(1, limit + 1):
        words = number_to_words(i)
        total_letters += len(words)
    return total_letters

if __name__ == "__main__":
    limit = 1000
    result = count_letters_in_numbers(limit)
    print(f"The total number of letters used from 1 to {limit} is: {result}")