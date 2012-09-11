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
from observateur.header import Header as O_Header

class Header:
    """
    Class Header
    Modele representation of HTTP REQUEST Headers
    """

    _instance = None
    myParam = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, data={}):
        """
        Comments
        """
        if not self.myParam:
            self.my_header = O_Header(data)

    def add_param(self, name, value):
        """
        Comments
        """
        self.my_header.set(name, value)

    def del_param(self, index):
        """
        docstring for delParam
        """
        self.my_header.delete(index)

if __name__ == '__main__':
    TEST = Header()

