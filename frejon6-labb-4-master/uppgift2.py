from functions import *

LIST = text_to_word_list('ordlista.txt')


def main():
    """A program with a text based user interface that
      searches for an element in a list using the lin_search function"""
    while True:
        element = input("Ditt ord: ")
        if lin_search(LIST, element):
            print(element + " finns i listan")
        else:
            print(element + " finns inte i listan")


main()
