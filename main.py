import sys
from stats import count_words, count_chars, sort_by_count

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        contents = f.read()
    return contents

def main(book_path: str):
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_dict = count_chars(book_text)
    sorted_by_count = sort_by_count(char_dict)

    print("="*12, " BOOKBOT ", "="*12)
    print(f"Analyzing book found at {book_path}...")
    print("-"*11, " Word Count ", "-"*10)
    print(f"Found {num_words} total words")
    print("-"*9, " Character Count ", "-"*7)
    for dct in sorted_by_count:
        if dct['char'].isalpha(): # type: ignore
            print(f"{dct['char']}: {dct['num']}")
    print("="*14, " END ", "="*14)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    main(book_path)
