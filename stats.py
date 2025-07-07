def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    result = {}
    text = text.lower()

    for char in text:
        result[char] = result.get(char, 0) + 1

    return result

def sort_on(item):
    return item["num"]

def sort_char_count(char_count_dict):
    result = []

    for item in char_count_dict:
        result.append({"char": item, "num": char_count_dict[item]})
    
    result.sort(reverse=True, key=sort_on)

    return result
