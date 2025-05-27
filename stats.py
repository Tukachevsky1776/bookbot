def get_word_count(book_string):
    words = book_string.split()
    print (f"{len(words)} words found in the document")

def get_char_count(book_string):
    chars_table = {}
    for char in book_string:
        char = char.lower()
        if char in chars_table:
                    chars_table[char] += 1
        else:
            chars_table[char] = 1
    print(chars_table)
    return chars_table