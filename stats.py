def sort_on(dict):
    return dict["num"]


def sort_dict(dict):
    char_list = []
    for key in dict:
        dict_entry = {"char": key, "num": dict[key]}
        char_list.append(dict_entry)

    char_list.sort(reverse=True, key=sort_on)
    
    return char_list



def get_character_count(filepath):
    with open(filepath) as f:
        text = f.read().lower()
        chars = {}
        for char in text:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
        return chars



def get_num_words(filepath):
    with open(filepath) as f:
        word_list = f.read().split()
        return len(word_list)

