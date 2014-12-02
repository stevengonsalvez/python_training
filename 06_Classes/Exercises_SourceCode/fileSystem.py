# -*- coding:utf-8; -*-

'''A module providing various classes to model a files system.'''

__author__ = 'Russel Winder'
__date__ = '2012-02-18'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007,2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'


class Node(object):
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory

    def setDirectory(self, directory):
        self.directory = directory

    def absPath(self):
        if self.directory:
            return(self.directory.absPath() + '/' + self.name).replace('//', '/')
        else:
            return '/'


class Directory(Node):
    def __init__(self, name, directory=None, *args):
        Node.__init__(self, name, directory)
        self.directory = directory
        self.children = [e for e in args]
        for node in self.children:
            node.setDirectory(self)

    def isDirectory(self):
        return True

    def add(self, node):
        self.children += [node]
        node.setDirectory(self)


class PlainFile(Node):
    def __init__(self, name, directory=None):
        Node.__init__(self, name, directory)

    def isDirectory(self):
        return False


class SymbolicLink(Node):
    def __init__(self, name, path, directory=None):
        Node.__init__(self, name, directory)
        self.path = path

    def isDirectory(self):
        return False


def hasCycles(node):
    return False
