import os
from stats import get_word_count
from stats import get_char_count
from stats import sort_char_count

def get_book_text(file_path):
    with open(file_path) as file:
        book_content = file.read()

    return book_content

def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    print(frankenstein_text)
    return frankenstein_text

main()
main_var = main()
print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {len(get_word_count(main_var))} total words
--------- Character Count -------""")
for entry in sort_char_count(get_char_count(main_var)):
    print(f"{entry['char']}: {entry['num']}")
print("============= END ===============")