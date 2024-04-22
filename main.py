def main():
    contents = get_file_content("books/frankenstein.txt")
    if len(contents) < 1:
        return
    
    print(count_words(contents))

def get_file_content(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception as e:
        print(f"Error opening file: {path}\n")
        print(e)
        return ""

def count_words(text):
    if type(text) == str:
        return len(text.split())
    return 0

main()