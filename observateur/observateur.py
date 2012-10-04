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

class Observateur:
    """
    Class Observable
    Observer le comportement de models de données
    """

    def __init__(self, initValue):
        """
        Construct standard object for observe model
        initValue is initialized data
        """
        self.data = initValue
        self.callback = {}

    def add_callback(self, func):
        """
        Add callback function to play when watch event on
        """
        self.callback[func] = 1

    def del_callback(self, func):
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

    def get(self):
        """
        Return list of all value
        """
        return self.data

    def unset(self):
        """
        Delete all data
        """
        self.data.clear()

    def is_empty(self):
        """
        Return True if not empty else return False
        """
        if not self.data:
            return False
        return True

if __name__ == '__main__':
    test = Observateur()
