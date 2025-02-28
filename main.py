import sys
from stats import get_word_count, get_character_count,get_list_of_alpha_characters_and_counts

# Check if the number of arguments is correct (script name + 1 argument)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  # Exit with status code 1 indicating an error

def get_book_text(filepath):
    text = ""
    try:
        with open(filepath) as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' does not exist.")
    return text
def generate_report(filepath,word_count, list_counts_per_character):
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {filepath}\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {word_count} total words\n"
    report += "--------- Character Count -------\n"

     # Iterate through the list of dictionaries
    for dictionary in list_counts_per_character:
        for character, count in dictionary.items():  # Extract key-value pairs
            report += f"{character}: {count}\n"  # Append to the report

    report += "============= END ==============="
    return report

def main():
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    list_counts_per_character = get_list_of_alpha_characters_and_counts(character_count)
    
    generated_report = generate_report(file_path,word_count,list_counts_per_character)

    print(generated_report)




if __name__ == "__main__":
    main()