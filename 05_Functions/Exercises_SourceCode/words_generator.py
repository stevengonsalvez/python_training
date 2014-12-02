#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''
A script that prints out all the permutations of a string (given in the command line) that appear in a
"dictionary".  Here we assume a Debian/Ubuntu system so that there is the default dictionary of
/usr/share/dict/words.
'''

__author__ = 'Russel Winder'
__date__ = '2014-09-27'
__version__ = '1.2'
__copyright__ = 'Copyright © 2007, 2012, 2014  Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import os.path
import sys

# FIXME: the different functions return different sequence structures.

if sys.argv[0] == 'words_iteration.py':
    from permutations import permutations_iteration as permutations
elif sys.argv[0] == 'words_comprehension.py':
    from permutations import permutations_comprehension as permutations
elif sys.argv[0] == 'words_comprehension_alt.py':
    from permutations import permutations_comprehension_alt as permutations
else:
    from permutations import permutations_generator as permutations

if __name__ == '__main__':
    argCount = len(sys.argv) - 1
    if argCount not in (1, 2):
        print('Usage: {} <string> [ <dictionary> ]'.format(os.path.basename(sys.argv[0])))
    else:
        wordListFileName = sys.argv[2] if argCount == 2 else '/usr/share/dict/words'
        with open(wordListFileName) as file:
            wordList = file.read().split()
            for trial in permutations(sys.argv[1]):
                putative = ''.join(trial)
                if putative in wordList:
                    print(putative)
