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
from observateur.recherche import Recherche as O_Recherche

class Recherche:
    """
    Class Recherche
    Modele representation of HTTP URL
    """

    def __init__(self, data=""):
        """
        Comments
        """
        self.my_recherche = O_Recherche(data)

    def add_param(self, url):
        """
        Comments
        """
        self.my_recherche.set(url)

if __name__ == '__main__':
    TEST = Recherche()
