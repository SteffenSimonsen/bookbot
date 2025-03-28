def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def get_book_words(filepath):

    text = get_book_text(filepath)

    wordcount = 0

    words = text.split()

    return words, len(words)

def get_character_count(text):

    char_count = {}

    for word in text:
        
        chars = list(word)

        for c in chars:
            if c.lower() in char_count:
                char_count[c.lower()] += 1
            else:
                char_count[c.lower()] = 1
    return char_count
    
 
        

