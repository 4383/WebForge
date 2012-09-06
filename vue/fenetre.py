#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
file: vue/fenetre.py
"""

class Fenetre():
    """
    Vue principal
    """
    def __init__(self, fenetre):
        """
        Constructeur de la fenetre
        """
        width = fenetre.winfo_screenwidth()
        height = fenetre.winfo_screenwidth()
        self.fenetre = fenetre
        self.fenetre.title("WebForge")
        self.fenetre.geometry("%dx%d+0+0" % (width, height))
