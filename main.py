def main():
    # Opens a .txt file and provides a word count and a character count
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"This book contains {word_count(file_contents)} words.")
    print("Here are all the character counts in this book: ")
    print(character_count(file_contents))

def word_count(text):
    # Returns the length of a list created by seperating all the words in a text
    return len(text.split())

def character_count(text):
    # Creates a dictionary that contains a count of all instances of a character
    # Spaces have been removed and capital letters count as lowercase
    chars = {}
    text = text.replace(" ", "")
    for i in text.lower():
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars

if __name__ == "__main__":
    main()