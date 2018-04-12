# -*- coding: UTF-8 -*-

from bindType import START, BIND, THRU, END
import subprocess

class Node(object):
  def __init__(self, exePath: str):
    self.__exePath = exePath
    self.__return = None

  def run(self, arg: str):
    '''ノードを実行する'''
    cmd = [self.__exePath, arg]
    print('cmd:',cmd)
    self.__return = subprocess.run(cmd,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   check=False,
                                   shell=False
                                  )
    print(self.__return.stderr.decode('utf-8'))
    return self.__return.stdout.decode('utf-8')


if __name__ == '__main__':
  import argparse
  psr = argparse.ArgumentParser()
  psr.add_argument('modPath',help='path to exe')
  psr.add_argument('-i', '--input', help='input to exe', required=False, default='')
  a = psr.parse_args()
  node = Node(a.modPath)
  res = node.run(a.input)
  print(res)
