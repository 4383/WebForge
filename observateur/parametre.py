#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: observable.py
Author: Hervé Beraud
Description: Classe observatrice de model
Date 02/08/2012
Version 1.0
CopyRight Hervé Beraud
"""

class Parametre:
    """
    Class Observable
    Observer le comportement de models de données
    """

    def __init__(self, initValue={}):
        """
        Construct standard object for observe model
        parameter
        initValue as tuple of element parameter
        """
        self.data = initValue
        self.callback = {}

    def add_callback(self, func):
        """
        Add callback function to play when watch event on
        """
        self.callback[func] = 1

    def del_callbacl(self, func):
        """
        Delete callback function fr
        """
        del self.callback[func]

    def _do_callbacks(self):
        """
        Play all callbacks defined
        """
        for func in self.callback:
            func(self.data)

    def set(self, name, value):
        """
        Set a new value into dict
        """
        self.data[name] = value
        self._do_callbacks()

    def delete(self, index):
        """
        Delete the item at the position defined by index
        """
        self.data.pop(index)
        self._do_callbacks()

    def get(self):
        """
        Return list of all value
        """
        return self.data

    def unset(self):
        self.data.clear()

if __name__ == '__main__':
    test = Parametre()
    print("Dict = %s" % test.get())
    test.set("test", "1")
    print("Dict = %s" % test.get())
    test.set("test2", "2")
    print("Dict = %s" % test.get())



