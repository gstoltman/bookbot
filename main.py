from stats import get_book_word_count, get_letter_count, sorted_letters
import sys

def print_report(book, path, word_count, sorted_letter_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_letter_dict:
        print(i["letter"]+':',i["count"])
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file = sys.argv[1]
    frankenstein_word_count = get_book_word_count(book_file)
    frankenstein_letter_count = get_letter_count(book_file)
    frankenstein_sorted_letters = sorted_letters(frankenstein_letter_count)

    print_report("frankenstein", book_file, frankenstein_word_count, frankenstein_sorted_letters)

main()
