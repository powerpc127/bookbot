def main():
    # Opens a .txt file and provides a word count and a character count
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"--- Begin report of {f.name} ---")
    print(f"This book contains {word_count(file_contents)} words.")
    print("Here are all the character counts in this book: ")
    character_count(file_contents)
    print("--- End report ---")

def word_count(text):
    # Returns the length of a list created by seperating all the words in a text
    return len(text.split())

def character_count(text):
    # Creates a dictionary that contains a count of all instances of a character
    # Spaces have been removed and capital letters count as lowercase
    chars = {}
    text = text.replace(" ", "")
    for i in text.lower():
        if not i.isalpha(): # Remove this condition to make it count EVERY character
            pass
        elif i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    # 1/8 Update: Sort the dict by value and print the character count one line at a time
    # Use sorted() to put the dict in numerical order for values
    chars_sorted = {}
    for key in sorted(chars, key=chars.get, reverse=True):
        chars_sorted[key] = chars[key]
    for key in chars_sorted:
        print(f"The '{key}' character was found {chars_sorted[key]} times")
    

if __name__ == "__main__":
    main()