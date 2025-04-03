def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read() 

def word_count(filepath):
    text = get_book_text(filepath)
    words = text.split()
    return len(words)

def letter_count(filepath):
    text = get_book_text(filepath).lower()
    counts = {}
    for char in text:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

def sort_letters(filepath):
    count = letter_count(filepath)
    sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    return sorted_count
    
