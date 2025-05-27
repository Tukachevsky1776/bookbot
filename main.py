import os
from stats import get_word_count
from stats import get_char_count

def get_book_text(file_path):
    with open(file_path) as file:
        book_content = file.read()

    return book_content

def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    print(frankenstein_text)
    return frankenstein_text

main()
get_word_count(main())
get_char_count(main())