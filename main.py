def main(txt_file):
    booktext = read_book(f"./books/{txt_file}")
    total_words = count_words(booktext)
    number_of_characters = count_characters(booktext)
    print(f'---Report for {txt_file} ---')
    print('')

    print(f'This text contains {total_words} total words.')
    print('')

    for char in number_of_characters:
        print(f'Character: {char} occurs {number_of_characters[char]} times')

    print('')
    print('---End Report---')

    

def read_book(book_path):
    with open(book_path) as book:
        text = book.read()
        return text

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_set = set()

    for letter in letters:
        letters_set.add(letter)

    letters_count = {}

    for l in letters:
        count = 0        
        for i in text:
            if i.lower() == l:
                count += 1

        letters_count.update({l: count})

    return letters_count 

main('frankenstein.txt')



    

    
    
