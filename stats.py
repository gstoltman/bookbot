def get_book_text(book):
    with open(book) as f:
        book_text = f.read()
        return book_text

def get_book_word_count(book):
    book_text = get_book_text(book)
    word_list = book_text.split()
    return len(word_list)

def get_letter_count(book):
    book_text = get_book_text(book).lower()
    letter_dict = {}
    for i in book_text:
        letter_dict[i] = letter_dict.get(i, 0) +1
    return letter_dict

def sort_on(dict):
    return dict["count"]

def sorted_letters(letter_dict):
    pair_list = []
    for key, value in letter_dict.items():
        if key.isalpha():
            pairs = {"letter":key, "count":value}
            pair_list.append(pairs)
    pair_list.sort(reverse=True, key=sort_on)
    return pair_list
