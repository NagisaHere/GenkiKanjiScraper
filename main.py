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
import logging
import glob
import json

# own imports
from constants import NON_JAPANESE_CHARACTER, KANJI_FULL, DATA_SRC, OUTPUT

# ---------------------------------------
# Logging Setup
# ---------------------------------------
if not logging.getLogger().hasHandlers():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(message)s',
        handlers=[
            logging.FileHandler("KanjiScraper.log"),
            logging.StreamHandler()
        ]
    )

logger = logging.getLogger('KanjiScraper')
logger.setLevel(logging.DEBUG)



def ReadKanji(path: str, results: list) -> None:
    """Read the data file for kanji.
    
    Kanji is only stored in the first index (in a text file separated by spaces)
    Remove all special characters that isn't kanji, hiragana, or katakana.
    
    Parameters:
        path: path to kanji data
    """
    with open(path, 'r', encoding='utf-8') as the_file:
        for line in the_file:
            line = re.sub(r"\s+", " ", line)
            candidate = line.split(" ")[0]
            word = re.sub(NON_JAPANESE_CHARACTER, "", candidate)
            if re.findall(KANJI_FULL, word):
                results.append(word)
            else:
                logging.debug(f"Discarding {candidate}")

def initialiseOutput() -> dict:
    output = {}
    for i in range(15, 24):
        output[f"ch{i}"] = []
    
    return output

def main():
    output = initialiseOutput()
    
    FILE_PATH = glob.glob("./data/*.txt")
    
    for path in FILE_PATH:
        word_list = []
        ReadKanji(path, word_list)
        
        # append to chapter
        for chapter in output:
            if chapter in path:
                output[chapter] = word_list.copy()
                word_list = []
                break

    json_object = json.dumps(output, indent=2)
    
    with open("data.json", "w", encoding="utf-8") as the_file:
        the_file.write(json_object)

if __name__ == '__main__':
    # check that the console is in utf-8
    assert sys.getdefaultencoding() == 'utf-8'
    main()
