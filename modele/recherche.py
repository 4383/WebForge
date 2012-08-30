#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: recherche.py
Author: Hervé Beraud
Description: modele de données des recherches (url)
Date 29/08/2012
Version 1.0
CopyRight Hervé Beraud
"""
from observateur.parametre import Parametre as O_Parametre

class Recherche:
    """
    Class Recherche
    Modele representation of HTTP URL
    """

    def __init__(self, data=""):
        """
        Comments
        """
        self.my_recherche = O_Parametre(data)

    def add_param(self, url):
        """
        Comments
        """
        self.my_recherche.set(url)

if __name__ == '__main__':
    TEST = Recherche()
