#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: request.py
Author: Hervé Beraud
Description: Utils functions.
Date 23/07/2012
Version 1.0
CopyRight Hervé Beraud
"""

def list_display_to_textarea(iterable):
    """
    Return list to format :
    key : value\n
    key : value\n
    ...
    """
    liste_formate = None
    if type(iterable) == type(dict()):
        for key, value in iterable.items():
            liste_formate = "%s%s : %s\n" % (key, value, liste_formate)
    elif type(iterable) == type(tuple()):
        for value in iterable:
            if not liste_formate:
                liste_formate = "%s" % value
            else:
                liste_formate = "%s : %s" % (liste_formate, value)
    return liste_formate
