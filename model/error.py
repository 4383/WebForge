#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: Error.py
Author: Hervé Beraud
Description: modele de données des parameters
Date 03/08/2012
Version 1.0
CopyRight Hervé Beraud
"""
from observateur.error import Error as O_Error

class Error:
    """
    Class Parameters
    Modele representation of HTTP REQUEST PARAMETERS
    """

    _instance = None
    my_error = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, data={}):
        """
        Comments
        """
        if not self.my_error:
            self.my_error = O_Error(data)

    def add_param(self, name, value):
        """
        Comments
        """
        self.my_error.set(name, value)

    def del_param(self, index):
        """
        docstring for delParam
        """
        self.my_error.delete(index)

if __name__ == '__main__':
    TEST = Error()


