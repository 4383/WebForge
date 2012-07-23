#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
"""

from tkinter import Frame
from tkinter import Entry
from tkinter import Button
import tkinter.messagebox

class Recherche():
    """
    Vue principal
    """
    def __init__(self, fenetre):
        """
        Constructeur de la fenetre
        """
        self.frame_top = Frame(fenetre, borderwidth=1, relief='groove', width=100)
        self.frame_top.pack( side='top')
        self.txt_recherche = Entry(self.frame_top, width=90)
        self.txt_recherche.pack(expand='yes', side='left')
        self.btn_go = Button(self.frame_top, text="GO")
        self.btn_go.pack(side='right')
