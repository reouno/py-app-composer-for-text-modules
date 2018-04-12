#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import argparse
import sys

def read(filePath):
  with open(filePath, 'r') as f:
    text = f.read()

  return text



if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('filePath')
  a = parser.parse_args()
  sys.stdout.write(read(a.filePath))
