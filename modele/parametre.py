#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: parametre.py
Author: Hervé Beraud
Description: modele de données des parameters
Date 03/08/2012
Version 1.0
CopyRight Hervé Beraud
"""
from observateur.parametre import Parametre as O_Parametre

class Parametre:
    """
    Class Parameters
    Modele representation of HTTP REQUEST PARAMETERS
    """

    def __init__(self, data={}):
        """
        Comments
        """
        self.myParam = O_Parametre(data)

    def add_param(self, name, value):
        """
        Comments
        """
        self.myParam.set(name, value)

    def del_param(self, index):
        """
        docstring for delParam
        """
        self.myParam.delete(index)

if __name__ == '__main__':
    TEST = Parametre()
