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
from observateur.observateur import Observateur

class Parametre(Observateur):
    """
    Class Parametre
    Parameters observator object
    """

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

if __name__ == '__main__':
    test = Parametre()
    print("Dict = %s" % test.get())
    test.set("test", "1")
    print("Dict = %s" % test.get())
    test.set("test2", "2")
    print("Dict = %s" % test.get())
