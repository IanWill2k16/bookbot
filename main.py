
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    letter_count_list = dict_to_list(letter_count)
    print_report(book_path, word_count, letter_count_list)

def print_report(book_path, word_count, letter_count_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for letter in letter_count_list:
        name = letter["name"]
        num = letter["num"]
        print(f"The {name} character was found {num} times")
    print(f"--- End report ---")

def sort_on(dict):
    return dict["num"]

def dict_to_list(dict):
    dict_list = []
    for pair in dict:
        if pair.isalpha():
            dict_list.append({"name": pair, "num": dict[pair]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

main()