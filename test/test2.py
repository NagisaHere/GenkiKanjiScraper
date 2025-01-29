# -*- coding: utf-8 -*-
import re
import sys

# god my workflow is so screwed
# credit to https://github.com/olsgaard/Japanese_nlp_scripts/blob/master/jp_regex.py
# thank you for saving my ass
kanji_full = r'[㐀-䶵一-鿋豈-頻]'

def ReadKanji(line: str) -> None:
    """Reads the current line and appends to the word list if kanji is valid.

    A Kanji is valid given that there is no hiragana or english in the line.
    """
    hiragana = re.findall(hiragana_full, line)
    katakana = re.findall(katakana_full, line)
    kanji = re.findall(kanji_full, line)

    # I feel like this adds english?
    if (not katakana and not hiragana and kanji):
        elem = "\""
        elem += line.strip()
        elem += "\","
        print(f"Kanji found {elem}")

hiragana_full = r'[ぁ-ゟ]'
katakana_full = r'[゠-ヿ]'


ReadKanji("一")

print(sys.getdefaultencoding())