# -*- coding: utf-8 -*-
import re


# god my workflow is so screwed
# credit to https://github.com/olsgaard/Japanese_nlp_scripts/blob/master/jp_regex.py
# thank you for saving my ass

hiragana_full = r'[ぁ-ゟ]'
katakana_full = r'[゠-ヿ]'

print(re.findall(hiragana_full, "あ"))
