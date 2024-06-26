def main():
    file_path = "books/frankenstein.txt"
    text = read_book(file_path)
    word_count = word_counter(text)
    alpha = "abcdefghijklmnopqrstuvwxyz"
    letters = letter_counter(checker(list(text), alpha), build_dictionary(alpha))
    converted = converter(letters)
    print_me(file_path,word_count,converted)

def print_me(path, count, characters):
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document")
    print("") # Adds a blank line for formatting
    for c in characters:
        letter = c["letter"]
        count = c["count"]
        print(f"The '{letter}' character was found {count} times")

def read_book(book):
    with open(book) as f:
        return f.read()

def word_counter(text):
    words = text.split()
    return len(words)

def build_dictionary(alpha):
    return {i: 0 for i in alpha}

def checker(letter_list, alpha):
    return [i for i in letter_list if i in alpha]

def letter_counter(letters, dictionary):
    for l in letters:
        dictionary[l] += 1
    return dictionary

def count_sort(dictionary):
    return dictionary["count"]

def converter(letters):
    new_list = []
    for letter, count in letters.items():
        new_list.append({"letter": letter,"count": count})
    new_list.sort(key=count_sort, reverse=True)
    return new_list

if __name__ == "__main__":
    main()