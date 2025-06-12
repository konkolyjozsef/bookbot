from stats import get_num_words, get_text_string, sorted_text
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1] ##['main.py', 'books/frankenstein.txt']
    book_text = get_book_text(filepath)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_count = get_num_words(book_text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    char_counts = get_text_string(book_text)

    sorted_chars = sorted_text(char_counts)

    for entry in sorted_chars:
        char_display = entry['char']
        if not char_display.isalpha():
            continue
        print(f"{char_display}: {entry['num']}")

    print("============= END ===============")

main()
