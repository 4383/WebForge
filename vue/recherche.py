#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
"""

from constante import GT_
from constante import RESSOURCES_PATH
from constante import VERSION
import os
try:
    from Tkinter import Frame
    from Tkinter import Entry
    from Tkinter import Button
    from Tkinter import Label
    from Tkinter import PhotoImage
except ImportError:
    from tkinter import Frame
    from tkinter import Entry
    from tkinter import Button
    from tkinter import Label
    from tkinter import PhotoImage

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
        self.img = PhotoImage(file="%slogo.gif" % RESSOURCES_PATH)
        self.logo = Label(self.frame_top, image=self.img)
        self.logo.pack(pady=(0, 20), side="left")
        self.brand = Label(self.frame_top, text=GT_('WebForge %s' % VERSION), font=(20))
        self.brand.pack(pady=(10, 20), padx=(0, 20), side="left")
        self.txt_recherche = Entry(self.frame_top)
        self.txt_recherche.pack(pady=(0, 20), expand='yes', fill='both', side='left')
        self.btn_go = Button(self.frame_top, text="GO")
        self.btn_go.pack(pady=(0, 20), side='right')
        self.btn_erase = Button(self.frame_top, text="X")
        self.btn_erase.pack(pady=(0, 20), side='right')

    def set_url(self, url):
        """
        Set a new url value to the field
        """
        print("ok")
        self.txt_recherche.insert(0, url)
