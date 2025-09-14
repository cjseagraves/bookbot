def get_num_words(file_contents):
    num_words = len(file_contents.split())
    return num_words
def get_character_count(file_contents):
    character_count = {}
    for character in file_contents.lower():
        if character.isalpha() and character in character_count:
            character_count[character] += 1
        elif character.isalpha():
            character_count[character] = 1
    return character_count

def get_char_list(character_count):
    char_list = []
    for k in character_count:
        char_list.append({"char": k, "count": character_count[k]})
    return char_list

def get_count(item):
        return item["count"]
def sort_the_list(character_count):
    sorted_list = get_char_list(character_count)
    sorted_list.sort(key=get_count, reverse=True)
    return sorted_list