def count_char(text):
    """
    This function takes a string as input and returns a dictionary
    containing the count of each character in the string.
    """

    char_counts = {}

    for char in text:

        if char not in char_counts:
            char_counts[char] = 0

        char_counts[char] += 1

    return char_counts


text = "hello world and uniwersum"
char_counts = count_char(text)
print(char_counts)
