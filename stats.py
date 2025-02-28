def get_word_count(text):
    count = 0
    count = len(text.split())
    return count


def get_character_count(text):
    results = {}

    for c in text:
        char = c.lower()
        if char in results:
            results[char] = results[char] + 1
        else:
            results[char] = 1

    return results

def get_count(dictionary):
    """Helper function to extract the count from a dictionary."""
    return list(dictionary.values())[0]  # Extract the count value


def get_list_of_alpha_characters_and_counts(dictionary_of_characters_and_their_counts):
    dictionary_list = [] ##we are returning a list of dictionaries
    ##sort from greatest to least by the count, and skip any character that is not alpha

    for character, count in dictionary_of_characters_and_their_counts.items():
        # Skip non-alphabetic characters
        if not character.isalpha():
            continue
        # Append correctly structured dictionary
        dictionary_list.append({character: count})

    # Sort using the built-in sorted() function, NOT list.sorted()
    sorted_dictionary_list = sorted(dictionary_list, key=get_count, reverse=True)
    return sorted_dictionary_list