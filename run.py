#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from argparse import ArgumentParser, Namespace
from bindType import START, BIND, THRU, END
from graphParser import parse
from itertools import zip_longest
from Node import Node
from typing import List, Text

def parseArgs(args: List[Text]) -> Namespace:
  psr = ArgumentParser()
  psr.add_argument('graphStr', help='graph definition such as "mod1 >>= mod2 >> mod3"')
  psr.add_argument('-i', '--input', help='input to this app', required=False, default='')
  return psr.parse_args()

def run(binds: List[int], nodes: List[Node], appArg: Text) -> int:
  arg = appArg
  for bind, node in zip_longest(binds, nodes):
    if bind in [START, BIND] and node:
      print('\nSTART or BIND')
      arg = node.run(arg)
    elif bind == THRU and node:
      print('\nTHRU')
      arg = node.run('')
    else: # END
      print('\nEND')
      print('output:\n',arg)
      print('end')

  return 0




if __name__ == '__main__':
  a = parseArgs(sys.argv[1:])
  binds, modPaths = parse(a.graphStr.split(' '))
  nodes = [Node(mod) for mod in modPaths]
  run(binds, nodes, a.input)
