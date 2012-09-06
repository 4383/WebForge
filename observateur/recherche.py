#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: observable.py
Author: Hervé Beraud
Description: Classe observatrice du model de données des url
Date 02/08/2012
Version 1.0
CopyRight Hervé Beraud
"""
from observateur.observateur import Observateur

class Recherche(Observateur):
    """
    Class Observable
    Observer le comportement de models de données
    """

    def set(self, url):
        """
        Set a new url value
        """
        self.data = url
        self._do_callbacks()

if __name__ == '__main__':
    test = Recherche()
    print("Dict = %s" % test.get())
    test.set("http://google.fr")
    print("Dict = %s" % test.get())
    test.set("http://free.fr")
    print("Dict = %s" % test.get())
