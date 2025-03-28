from stats import get_book_words, get_character_count

def main():
    
    words, num_words = get_book_words(r"books/frankenstein.txt")

    print(f"{num_words} words found in the document")

    char_count = get_character_count(words)

    print(char_count)

main()
