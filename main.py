def main():
    path = "books/frankenstein.txt"

    print(f"=== Begin report of {path} ===")

    contents = get_file_content(path)
    if len(contents) < 1:
        print("Document seems to be empty, end of report.")
        return

    print(f"{count_words(contents)} words found in the document\n")

    pretty_print_letter_counts(count_letters(contents))

    print("\n=== End report ===")

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

def sort_on(dict):
    return dict["count"]

def pretty_print_letter_counts(letter_counts):
    counts = []
    for letter, count in letter_counts.items():
        if letter.isalpha():
            counts.append({"letter": letter, "count": count})

    counts.sort(key=sort_on, reverse=True)
    
    for count in counts:
        print(f"Letter {count["letter"]} was found {count["count"]:5} times.")

main()