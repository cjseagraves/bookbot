from stats import get_num_words
from stats import get_character_count
from stats import sort_the_list
import sys 

def get_book(sys_argv):
    if len(sys_argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys_argv[1]
    print(f"received book path: {book}")
    return book

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    print(f"analyzing contents from {book}...")
    return file_contents

def main():
    book = get_book(sys.argv)
    file_contents = get_book_text(book)
    num_words= get_num_words(file_contents)
    character_count = get_character_count(file_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sort_the_list(character_count):
        print(f"{i['char']}: {i['count']}")



main()