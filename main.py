import sys

from stats import get_wordcount, sort_countcharfunc

if len(sys.argv) == 2:
    book=sys.argv[1]
else: 
    print("Usage: python3 main.py <path_to_book>") 
    sys.exit(1)
 


def main():
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(get_wordcount(book))
    print("--------- Character Count -------")
    sort_countcharfunc(book)
    print("============= END ===============")
    
    




    return




main()

