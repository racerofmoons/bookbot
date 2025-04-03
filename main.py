from stats import word_count, letter_count, sort_letters
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filepath>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(sys.argv[1])} total words")
    print("--------- Character Count -------")
    for key, value in sort_letters(sys.argv[1]).items():
        print(f"{key}: {value}")
    print("============= END ===============")

main()