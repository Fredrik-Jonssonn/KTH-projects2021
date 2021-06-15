#!/usr/bin/env python3
import sys

VOWELS = "aouåeiyäöAOUÅEIYÄÖ"
CONSONANTS = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"


def visk(text):
    output = ""
    for char in text:
        if char in VOWELS:
            pass
        else:
            output += char
    return output


def rovar(text):
    output = ""
    for char in text:
        if char in CONSONANTS:
            output += char + "o" + char.lower()
        else:
            output += char
    return output


def reverse_rovar(text):
    output = ""
    counter = 0
    for char in text:
        if counter > 0:
            counter -= 1
        elif char in CONSONANTS:
            output += char
            counter = 2
        else:
            output += char
    return output


def bebis(text):
    output = []
    words = text.split()
    for word in words:
        current_word = ""
        counter = 0
        for char in word:
            if char in VOWELS:
                current_word += word[:counter + 1]
                for i in range(0, 2):
                    current_word += word[:counter + 1].lower()
                break
            else:
                counter += 1
        output.append(current_word)
    return " ".join(output)


def all(text):
    for char in text:
        if char in ".,:;!?'¨":
            text = text.replace(char, "")
    output = []
    words = text.split()
    for word in words:
        current_word = ""
        consonants = ""
        counter = 0
        for char in word:
            if char in VOWELS:
                current_word += word[counter:] + word[:counter] + "all"
                break
            elif counter == len(word) - 1:
                current_word += consonants + char + "all"
            else:
                counter += 1
                consonants += char
        output.append(current_word)
    return " ".join(output)


def fikon(text):
    for char in text:
        if char in ".,:;!?'¨":
            text = text.replace(char, "")
    output = []
    words = text.split()
    for word in words:
        current_word = ""
        counter = 0
        consonants = ""
        for char in word:
            if char in VOWELS:
                current_word += "fi" + word[counter + 1:] + word[:counter + 1] + "kon"
                break
            elif counter == len(word) - 1:
                current_word += "fi" + consonants + char + "kon"
            else:
                counter += 1
                consonants += char
        output.append(current_word)
    return " ".join(output)


def main():
    menu = {"-v": lambda text: visk(text),
            "-r": lambda text: rovar(text),
            "-b": lambda text: bebis(text),
            "-a": lambda text: all(text),
            "-f": lambda text: fikon(text)}
    text = sys.stdin.read()
    a = sys.argv[1]
    print(menu[a](text))


if __name__ == '__main__':
    main()
