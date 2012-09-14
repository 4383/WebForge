#-*- coding: utf-8 -*-
"""
"""

from constante import GT_
from vue.vue import Vue
from component.tkprogressbar import TkProgessBar
try:
    from Tkinter import Frame
    from Tkinter import Label
except ImportError:
    from tkinter import Frame
    from tkinter import Label

class Status(Vue):
    """
    Vue principal
    """
    def __init__(self, fenetre):
        """
        Constructeur de la fenetre
        """
        self.frame = Frame(fenetre, borderwidth=1, relief='groove')
        self.frame.pack_configure(side='bottom', fill='both')
        self.frame.pack()
        self.titre = Label(self.frame, text=GT_('Status'), font=(20))
        self.titre.pack()
        self.progressbar = TkProgessBar(self.frame)
        self.progressbar.pack()
