#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
"""

from constante import GT_
from constante import RESSOURCES_PATH
from constante import VERSION
from vue.vue import Vue
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

class Result(Vue):
    """
    Vue principal
    """
    def __init__(self, fenetre):
        """
        Constructeur de la fenetre
        """
        self.frame = Frame(fenetre, borderwidth=1, relief='groove')
        self.frame.pack_configure(side='left', expand='yes', fill='both')
        self.frame.pack()
        self.titre = Label(self.frame, text=GT_('Resultats'), font=(20))
        self.titre.pack()
