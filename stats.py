def get_word_count(book_string):
    words = book_string.split()
    return words

def get_char_count(book_string):
    chars_table = {}
    for char in book_string:
        char = char.lower()
        if char in chars_table:
                    chars_table[char] += 1
        else:
            chars_table[char] = 1
    return chars_table

def sort_on(dict):
    return dict["num"]

def sort_char_count(dict):
    dict_list = []
    for entry in dict:
        if entry.isalpha():
            char = {"char": entry}
            num = {"num": dict[entry]}
            dict_list.append({**char, **num})
        else:
            pass
    dict_list.sort(reverse = True, key = sort_on)
    return dict_list
