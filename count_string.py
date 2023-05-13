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
    max_count = max(char_counts.values())

    max_chars = {char: count for char, count in char_counts.items() if count == max_count}

    return max_chars


text = "hello world and uniwersum"
max_char = count_char(text)
print(max_char)
