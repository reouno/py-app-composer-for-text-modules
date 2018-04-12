#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from argparse import ArgumentParser
from collections import OrderedDict
from csv import QUOTE_NONNUMERIC
from gensim import corpora
from pandas import DataFrame
from typing import List, Text, Tuple

def words2bow(words: List[Text]) -> List[Tuple[Text, int]]:
  '''単語リストからbag of wordsを作る'''
  dic = corpora.Dictionary([words])
  idBow = dic.doc2bow(words)
  id2token = {v:k for k,v in dic.token2id.items()}
  wordsBow = [(id2token[id_], count) for id_, count in idBow]
  sortedBow = sorted(wordsBow, key = lambda x:(-x[1], x[0]))
  return sortedBow

def writeFile(bow: List[Tuple[Text, int]], output: Text) -> None:
  '''bowを書き出す'''
  df = DataFrame(bow, columns = ['words', 'count'])
  df.to_csv(output, index=False, quoting=QUOTE_NONNUMERIC)


if __name__ == '__main__':
  psr = ArgumentParser()
  psr.add_argument('text', help='space-separated words list')
  psr.add_argument('-o', '--output', help='csv file path to output bag of words', required=False, default='bow.csv')
  a = psr.parse_args()
  words = a.text.split(' ')
  bow = words2bow(words)
  writeFile(bow, a.output)
  print(a.output)
