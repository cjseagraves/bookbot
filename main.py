from stats import get_num_words
from stats import get_character_count
from stats import sort_the_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text("")
    num_words= get_num_words(file_contents)
    character_count = get_character_count(file_contents)
    print("============ BOOKBOT ============")
    print("Analyzing book found at ")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sort_the_list(character_count):
        print(f"{i['char']}: {i['count']}")



main()