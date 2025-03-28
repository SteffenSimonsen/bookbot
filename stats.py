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
    
 
def sort_dictionary(dictionary):

    def sort_on(dict):
        return dict['count']
    
    dict_list = []

    for key, value in dictionary.items():
        dict_list.append({'char': key, 'count': value})


    dict_list.sort(reverse=True, key=sort_on)

    return dict_list


