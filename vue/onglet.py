#-*- coding: utf-8 -*-
"""
file:vue/onglet.py
"""

from constante import GT_
from vue.vue import Vue
try:
    from Tkinter import Frame
    from Tkinter import Label
    from Tkinter import Text
    from Tkinter import Scrollbar
except ImportError:
    from tkinter import Frame
    from tkinter import Label
    from tkinter import Text
    from tkinter import Scrollbar

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
        self.scrollbar = Scrollbar()
        self.result = Text(self.frame, yscrollcommand=self.scrollbar)
        self.result.tag_configure(
            'error',
            background='red',
            foreground='white',
            font='helvetica 15 bold',
            relief='raised',
        )
        self.result.tag_configure(
            'result',
            background='green',
            font='helvetica 15 bold',
            relief='raised',
        )
        self.result.pack(side='top', fill='both', expand='yes')

    def set_result(self, liste):
        """
        Update parameters list
        """
        self.result.delete(0.0, 'end')
        for key, value in  liste.items():
            self.result.insert('end', "%s\n\n" % key, ('result', ))
            self.result.insert('end', value)

    def set_error(self, liste):
        """
        Update parameters list
        """
        self.result.delete(0.0, 'end')
        for key, value in  liste.items():
            self.result.insert('end', "%s\n\n" % key, ('error', ))
            self.result.insert('end', value)
