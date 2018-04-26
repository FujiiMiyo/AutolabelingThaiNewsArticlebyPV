# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 21:40:32 2018

@author: RIKO
"""

from wordcut import Wordcut
if __name__ == '__main__':
    with open('bigthai.txt', encoding="UTF-8") as dict_file:
        word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
        wordcut = Wordcut(word_list)
        print(wordcut.tokenize("กากา cat หมา"))