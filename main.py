from stats import get_num_words
from stats import get_character_count
from stats import sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        word_count = get_num_words(path)
        char_count = get_character_count(path)
        sorted_chars = sort_dict(char_count)
        print("=========== BOOKBOT ===========\n" +
            f"Analyzing book found at {path}...\n" +
            "--------- Word Count ----------\n" +
            f"Found {word_count} total words\n" +
            "------- Character Count -------\n")
        for key in sorted_chars:
            if key["char"].isalpha():
                print(f"{key["char"]}: {key["num"]}\n")
        print("============ END =============")


main()
