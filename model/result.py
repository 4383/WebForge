#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: result.py
Author: Hervé Beraud
Description: modele de données des parameters
Date 03/08/2012
Version 1.0
CopyRight Hervé Beraud
"""
from observateur.result import Result as O_Result

class Result:
    """
    Class Parameters
    Modele representation of HTTP REQUEST PARAMETERS
    """

    _instance = None
    my_result = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, data={}):
        """
        Comments
        """
        if not self.my_result:
            self.my_result = O_Result(data)

    def add_param(self, name, value):
        """
        Comments
        """
        self.my_result.set(name, value)

    def del_param(self, index):
        """
        docstring for delParam
        """
        self.my_result.delete(index)

    def unset(self):
        self.my_result.unset()

    def is_empty(self):
        return self.my_result.is_empty()

if __name__ == '__main__':
    TEST = Result()

