# -*- coding: utf-8 -*-
# one time
# scrape all the kanji from the folder with yaml files
# and then append it all to one big list

# go through the list and pick a random kanji
# if the kanji is "" then choose another one
# the format of the yaml file is kanji: yes
# so it should be fine to just split the line on the space

"""
Problems:
    Can't convert japanese characters because of some unicode error (this
    doesnt seem to be an issue anymore)
    https://docs.python.org/3.12/howto/unicode.html
    https://stackoverflow.com/questions/14682933/chinese-and-japanese-character-support-in-python
"""
import platform
import sys
import re

os = platform.system()  # Linux or Windows

DATA_SRC = "./data/JAPN3020_DATA.txt"

chapter_one = [f"L{i}" for i in range(15, 20)]
chapter_two = [f"L{i}" for i in range(20, 24)]

hiragana_full = r'[ぁ-ゟ]'
katakana_full = r'[゠-ヿ]'

word_list = []

# check that the console is in utf-8
print(sys.getdefaultencoding())

# me when i realise I left my text file in downloads :skull:


# adds kanji to the wordlist array
def ReadKanji(line: str) -> None:
    """Reads the current line and appends to the word list if kanji is valid.

    A Kanji is valid given that there is no hiragana or english in the line.
    """
    hiragana = re.findall(hiragana_full, line)
    katakana = re.findall(katakana_full, line)

    if (not katakana and not hiragana):
        elem = "\""
        elem += line.strip()
        elem += "\","
        word_list.append(elem)


def read(path: str, arr: list[str]) -> None:
    """Read the file given a file path.

    Appends the line to a given list 'arr'.
    """
    with open(path, 'r', encoding='utf-8') as the_file:
        for line in the_file:
            ReadKanji(line)


if os == 'Linux':
    path = DATA_SRC
    read(path, word_list)

with open("data.txt", "w", encoding='utf-8') as the_file:
    for word in word_list:
        the_file.write(word + "\n")

# clean word list
word_list = []
