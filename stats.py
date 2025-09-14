def get_num_words(file_contents):
    num_words = len(file_contents.split())
    return num_words
def get_character_count(file_contents):
    character_count = {}
    for character in file_contents.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count