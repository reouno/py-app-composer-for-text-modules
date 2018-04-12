# -*- coding: UTF-8 -*-

from bindType import START, BIND, THRU, END
from typing import List, Text, Tuple

def parse(args: List[Text]) -> Tuple[List[int], List[str]]:
  '''parse modules graph
  mod1 >>= mod2 >> mod2 >>= mod4 ...
  '''
  binds = [] # just execute sequential or pass arguments
  modulePaths = []
  binds = addStart(binds)
  for i, arg in enumerate(args):
    if i % 2 == 0:
      modulePaths.append(arg)
    else:
      if arg == '>>=':
        binds.append(BIND) # pass arguments
      elif arg == '>>':
        binds.append(THRU) # just execute sequential (no any arguments)
      else:
        raise RuntimeError('Error: the order of arguments is invalid.\ninput like following:\n\ncomposer module1 >>= module2 >> module3 ...')

  binds = addEnd(binds)

  return binds, modulePaths

def addStart(binds):
  if len(binds)==0 or binds[0] != START:
    binds = [START] + binds
  return binds

def addEnd(binds):
  if len(binds)==0 or binds[-1] != END:
    binds.append(END)
  return binds


if __name__ == '__main__':
  args = ['mod1Path','>>=','mod2Path','>>','mod3Path']
  print('input:',args)
  print('output:',parse(args))
