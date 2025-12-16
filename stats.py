def get_word_count(text):
    words = text.split()
    count = len(words)
    return count
def get_character_count(text):
    char_count={}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
def sort_char_count(char_count):
    sorted_count = []
    for char, num in char_count.items():
        if char.isalpha():
            sorted_count.append({"char":char, "num":num})
    def sort_on(item):
        return item["num"]
    
    sorted_count.sort(reverse=True, key=sort_on)
    return sorted_count
                                 
