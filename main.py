from stats import get_book_words, get_character_count, sort_dictionary
import sys

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
    
    words, num_words = get_book_words(book)

    char_count = get_character_count(words)

    sorted = sort_dictionary(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted:

        char = item['char']
        if char.isalpha():
            print(f"{item['char']}: {item['count']}")

main()
