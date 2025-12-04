# Names Scores - https://projecteuler.net/problem=22

def compute():
    import string

    # Read names from the file
    with open('0022_names.txt', 'r') as f:
        names = f.read().replace('"', '').split(',')
    
    # Sort names alphabetically
    names.sort()

    # Create a dictionary to map letters to their alphabetical values
    letter_values = {letter: index for index, letter in enumerate(string.ascii_uppercase, start=1)}

    # Function to calculate the score of a name
    def name_score(name, position):
        score = sum(letter_values[char] for char in name)
        return score * position

    # Calculate the total score for all names
    total_score = sum(name_score(name, index + 1) for index, name in enumerate(names))

    return str(total_score)


if __name__ == "__main__":
    result = compute()
    print(f"The total of all the name scores in the file is: {result}")