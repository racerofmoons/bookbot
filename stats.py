import requests
import os

def cull_text(text, start_sequence="*** START OF THE PROJECT GUTENBERG EBOOK", end_sequence="*** END OF THE PROJECT GUTENBERG EBOOK"):
    start_index = text.find(start_sequence)
    end_index = text.find(end_sequence)
    if start_index != -1 and end_index != -1:
        return text[start_index + len(start_sequence):end_index]
    else:
        return text

def get_book_text(filepath):
    if filepath.startswith('http'):
        response = requests.get(filepath)
        if response.status_code == 200:
            return cull_text(response.text)
        else:
            raise Exception(f"Failed to fetch the book from URL: {filepath}")
    elif os.path.isfile(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        raise Exception(f"Invalid path to file: {filepath}. Must be a valid URL or local file path.")

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
    
