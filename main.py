from stats import word_count, sort_letters
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path or url>")
        sys.exit(1)
    try:
        count = word_count(sys.argv[1])
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for key, value in sort_letters(sys.argv[1]).items():
        print(f"{key}: {value}")
    print("============= END ===============")

main()