#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''A test for the module providing various classes to model a files system.'''

__author__ = 'Russel Winder'
__date__ = '2012-02-18'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007,2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import unittest

from fileSystem import Directory, PlainFile, SymbolicLink, hasCycles


class FileSystem_Test(unittest.TestCase):
    def testRootAndTwoFiles(self):
        bert = PlainFile('bert')
        jane = SymbolicLink('jane', bert)
        tree = Directory(None, None, bert, jane)
        assert not bert.isDirectory()
        assert not jane.isDirectory()
        assert tree.isDirectory()
        self.assertEqual('/bert', bert.absPath())
        self.assertEqual('/jane', jane.absPath())
        self.assertEqual('/', tree.absPath())
        assert not hasCycles(tree)

    def testRootAndSymbolicLinkUp(self):
        tree = Directory('/', None)
        up = SymbolicLink('up', tree, tree)
        assert tree.isDirectory()
        assert not up.isDirectory()
        self.assertEqual('/', tree.absPath())
        self.assertEqual('/up', up.absPath())
        #assert hasCycles(tree)

if __name__ == '__main__':
    unittest.main()
