import sys
from stats import get_word_count, get_character_count, sort_char_count
def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    contents = get_book_text(path)
    num_words = get_word_count(contents)
    counts = get_character_count(contents)
    sorted_dictionary = sort_char_count(counts)
    print(f"Found {num_words} total words")
    print(sorted_dictionary)
    for item in sorted_dictionary:
        print(f"{item['char']}: {item['num']}")
    
main()


