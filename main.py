from stats import word_count
from stats import char_count
from stats import sort_char_count
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    num_words = word_count(get_book_text(book_path))
    num_chars = char_count(get_book_text(book_path))
    sorted_chars = sort_char_count(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()


