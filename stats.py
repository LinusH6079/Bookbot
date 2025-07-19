
#Function to read "frankenstein.txt" and return it as a string.
def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

#Function to get num of words "frankenstein.txt"
def get_wordcount():
    word_list = get_book_text().split()
    word_count = len(word_list)
    num_words_string = f"{word_count} words found in the document"
    
    return num_words_string

#Function to counting every different character in "frankenstein.txt"
def count_characters():
    
    book_string = get_book_text()
    

    #a string of the book in lowercase
    lower_case_book_string = book_string.lower()

    #a list of words (only lowercase)
    wordlist_lower_case = lower_case_book_string.split()

    #Creating char dictionary
    char_dict = {}
    
    #For every char in every word in the wordlist_lower_case, adding it in as a key with value = 0, then adding 1 each time.
    for words in wordlist_lower_case:
        for char in words:
            if char not in char_dict:
                char_dict[char] = 0
            char_dict[char] += 1
            

    return char_dict

def sort_on(items):
    return items["num"]


def sort_countcharfunc():

    this_func_dict = count_characters()
    
    unsorted_list = []

    for char in this_func_dict:
        value = this_func_dict[char]
        
        
        new_dict = {}
        if char not in new_dict:
            new_dict["char"] = char
            new_dict["num"] = value
        unsorted_list.append(new_dict)

    unsorted_list.sort(reverse = True, key = sort_on)
    for dict in unsorted_list:
        return dict
    
    #nested_dict = {}
    #Vad jag vill: nested_dict = {"char": "b" , "num": 4868}

    


