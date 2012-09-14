#-*- coding: utf-8 -*-
"""
"""

from constante import GT_
from vue.vue import Vue
try:
    from Tkinter import Frame
    from Tkinter import Label
except ImportError:
    from tkinter import Frame
    from tkinter import Label

class Onglet(Vue):
    """
    Vue principal
    """
    def __init__(self, fenetre):
        """
        Constructeur de la fenetre
        """
        self.frame = Frame(fenetre, borderwidth=1, relief='groove')
        self.frame.pack_configure(side='top', fill='both', expand='yes')
        self.frame.pack()
        self.titre = Label(self.frame, text=GT_('Onglet'), font=(20))
        self.titre.pack()

