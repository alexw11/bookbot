def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    result = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in result.keys():
            result[char_lower] += 1
        else:
            result[char_lower] = 1
    return result

def get_character_dict(dicto):
    def sort_on(items):
        return items["num"]
    result = []
    for char in dicto:
        if not char.isalpha():
            continue
        little_dict = {}
        little_dict["char"] = char
        little_dict["num"] = dicto[char]
        result.append(little_dict)
    result.sort(reverse = True, key = sort_on)
    return result
