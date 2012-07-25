#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
"""

from constante import GT_
try:
    from Tkinter import Frame
    from Tkinter import Entry
    from Tkinter import Button
    from Tkinter import Label
except ImportError:
    from tkinter import Frame
    from tkinter import Entry
    from tkinter import Button
    from tkinter import Label

class Recherche():
    """
    Vue principal
    """
    def __init__(self, fenetre):
        """
        Constructeur de la fenetre
        """
        self.frame_top = Frame(fenetre, borderwidth=1, relief='groove', width=100)
        self.frame_top.pack( side='top', fill='both')
        self.titre = Label(self.frame_top, text=GT_('Url'), font=(20))
        self.titre.pack()
        self.txt_recherche = Entry(self.frame_top)
        self.txt_recherche.pack(expand='yes', fill='both', side='left')
        self.btn_go = Button(self.frame_top, text="GO")
        self.btn_go.pack(side='right')
