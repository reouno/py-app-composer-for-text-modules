#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

import argparse
import MeCab

def wakati(text):
  tagger = MeCab.Tagger('-Owakati')
  return tagger.parse(text)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('text')
  a = parser.parse_args()
  print(wakati(a.text))
