#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
file: vue/fenetre.py
"""
try:
    from Tkinter import Frame
except ImportError:
    from tkinter import Frame

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
        self.top = Frame(fenetre)
        self.top.pack(side='top', fill='both')
        self.left = Frame(fenetre)
        self.left.pack(side='left', fill='both')
        self.right = Frame(fenetre)
        self.right.pack(side='right', fill='both', expand='yes')
