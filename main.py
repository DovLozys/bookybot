def main():
    contents = get_file_content("books/frankenstein.txt")
    if len(contents) < 1:
        return
    
    print(count_words(contents))
    print(count_letters(contents))

def get_file_content(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception as e:
        print(f"Error opening file: {path}\n")
        print(e)
        return ""

def count_words(text):
    if type(text) != str:
        return 0
    return len(text.split())

def count_letters(text):
    if type(text) != str:
        return 0

    counts = {}

    for l in text:
        if l.lower() not in counts:
            counts[l.lower()] = 1
        else:
            counts[l.lower()] += 1
    
    return counts


main()