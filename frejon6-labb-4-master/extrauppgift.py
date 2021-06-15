from functions import *

LIST = text_to_word_list('ordlista.txt')


def kup_search(list, method):
    """Searches for pairs of "kuperade" words in a list using
        the chosen method and returns a list of those pairs"""
    words = list[:]
    pairs = []
    for word in words:
        is_pair = False
        match = [word]
        for i in range(1, 5):
            kup_word = word[i:] + word[:i]
            if method(words, kup_word):
                match.append(kup_word)
                words.remove(kup_word)
                is_pair = True
        if is_pair:
            pairs.append(" och ".join(match))
    return pairs


def riffle_shuffle(list):
    """Returns a perfect riffle shuffled version of a list"""
    first_half = 0
    second_half = len(list)//2
    shuffled_deck = []
    for i in range(len(list)//2):
        shuffled_deck.append(list[first_half])
        shuffled_deck.append(list[second_half])
        first_half += 1
        second_half += 1
    return shuffled_deck


def riffle_counter(amount_of_cards):
    """Counts the amount of riffle shuffles required to
        restore a deck of cards with the chosen amount (even) of cards
        to its original state"""
    if amount_of_cards % 2 != 0:
        print("Invalid number of cards (it should be an even number)")
        return
    deck = list(range(amount_of_cards))
    counter = 0
    while True:
        counter += 1
        shuffled_deck = riffle_shuffle(deck)
        if sorted(shuffled_deck) == shuffled_deck:
            print(counter, "riffle shuffles were required")
            break
        else:
            deck = shuffled_deck

riffle_counter(52)

