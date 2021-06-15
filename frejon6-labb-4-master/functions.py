"""for uppgift 1 """
def text_to_word_list(text_file):
    """Reads a text file and returns a list of all the words in the file"""
    with open(text_file, encoding='utf8') as a:
        text = a.read()
    return text.split()

"""The creation of the word list as per instruction"""
LIST = text_to_word_list('ordlista.txt')


"""for uppgift 2"""
def lin_search(list, element):
    """Linearly searches for a element in a list and
        returns True if that list contains that element and false otherwise"""
    for word in list:
        if word == element:
            return True
    return False


"""for uppgift 3"""
def lin_search_kup(list):
    """Linearly searches for pairs of "kuperade" words in a list
        and returns a list of those pairs"""
    words = list[:]
    pairs = []
    for word in words:
        is_pair = False
        match = [word]
        for i in range(1, 5):
            kup_word = word[i:] + word[:i]
            if lin_search(words, kup_word):
                match.append(kup_word)
                words.remove(kup_word)
                is_pair = True
        if is_pair:
            pairs.append(" och ".join(match))
    return pairs


"""for uppgift 4"""
def bin_search(list, element):
    """Returns True if the sorted list v contains an element and False otherwise.
        Undefined behaviour if v is not sorted"""
    lo = 0
    hi = len(list) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        #print(list[mid])
        if element < list[mid]:
            hi = mid - 1
        elif element > list[mid]:
            lo = mid + 1
        else:
            return True
    return False


"""for uppgift 5"""
def rec_bin_search(list, element):
    """Returns True if the sorted list v contains an element and False otherwise
        and does so recursively.
        Undefined behaviour if v is not sorted"""
    return helper(list, 0, len(list), element)


def helper(list, start, end, element):
    if start > end or start >= len(list):
        return False
    mid = (start + end) // 2
    if list[mid] == element:
        return True
    if list[mid] < element:
        return helper(list, mid + 1, end, element)
    else:
        return helper(list, start, mid - 1, element)


"""for uppgift 6"""
def bin_search_kup(list):
    """Binarily searches for pairs of "kuperade" words in a list
        and returns a list of those pairs"""
    words = list[:]
    pairs = []
    for word in words:
        is_pair = False
        match = [word]
        for i in range(1, 5):
            kup_word = word[i:] + word[:i]
            if bin_search(words, kup_word):
                match.append(kup_word)
                words.remove(kup_word)
                is_pair = True
        if is_pair:
            pairs.append(" och ".join(match))
    return pairs