def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        print(len(contents.split()))

main()