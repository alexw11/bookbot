import sys
from stats import get_num_words, get_character_count, get_character_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = get_num_words(book)
    character_count = get_character_count(book)
    character_dict = get_character_dict(character_count)
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for entry in character_dict:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if len(sys.argv)==2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)