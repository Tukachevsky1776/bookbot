import os
import sys
from stats import get_word_count
from stats import get_char_count
from stats import sort_char_count

if len(sys.argv)<2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as file:
        book_content = file.read()

    return book_content

def main():
    book_text = get_book_text(sys.argv[1])
    return book_text

main_var = main()
print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {len(get_word_count(main_var))} total words
--------- Character Count -------""")
for entry in sort_char_count(get_char_count(main_var)):
    print(f"{entry['char']}: {entry['num']}")
print("============= END ===============")