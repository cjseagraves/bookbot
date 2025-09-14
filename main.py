def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
def get_num_words(file_contents):
    num_words = len(file_contents.split())
    return num_words

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    num_words= get_num_words(file_contents)
    print(f"{num_words} words found in the document")
    

main()