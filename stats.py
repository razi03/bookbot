# stats.py

def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_repeated_characters(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def convert_to_list(characters):
    converted_list = []
    for char in characters:
        converted_list.append({"char": char, "num": characters[char]})
    
    converted_list.sort(key=sort_num, reverse=True)
    return converted_list

def sort_num(item):
    return item["num"]
