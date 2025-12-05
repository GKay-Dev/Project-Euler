# Coded Triangle Numbers - https://projecteuler.net/problem=42

def is_triangle_number(n):
    """Check if n is a triangle number."""
    # A number n is a triangle number if 8n + 1 is a perfect square
    x = 8 * n + 1
    s = int(x**0.5)
    return s * s == x

def word_value(word):
    """Calculate the alphabetical value of a word."""
    return sum(ord(char) - ord('A') + 1 for char in word)

def count_triangle_words(filename):
    """Count how many words in the file are triangle words."""
    with open(filename, 'r') as f:
        words = f.read().replace('"', '').split(',')
    
    triangle_word_count = sum(1 for word in words if is_triangle_number(word_value(word)))
    return triangle_word_count


if __name__ == "__main__":
    filename = '0042_words.txt'
    result = count_triangle_words(filename)
    print(f"The number of triangle words in the file is: {result}")