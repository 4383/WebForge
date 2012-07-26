#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: tkListboxMulticolumn.py
Author: Hervé Beraud
Description: Classe de génération de Listbox multicolonne
Date 24/07/2012
Version 1.0
CopyRight Hervé Beraud
"""
try:
    from Tkinter import Frame
    from Tkinter import Label
    from Tkinter import Listbox
except ImportError:
    from tkinter import Frame
    from tkinter import Label
    from tkinter import Listbox

class  TkListboxMulticolumn(Frame):
    """
    TkListboxMulticolumn component which can display multi-sortable listbox
    """

    def __init__(self, master=None, columns=(), cnf={}, **kw):
        """
        Construct a listbox widget with one or many column and label field for header

        Valid resource names: background, bd, bg, borderwidth, class, colormap,
        fg, font, foreground, height, highlightbackground,
        """
        Frame.__init__(self, master)
        if not columns:
           raise Exception('No columns required')

        # Construire le contenur de label
        self.libelle = Frame(self)
        #self.libelle = Frame(self.Conteneur)
        self.libelle.pack(side='top')
        # Construire le conteneur de listbox
        self.listboxs = Frame(self)
        self.listboxs.pack(side='bottom', expand='yes', fill='both')
        self.columns = []

        # Contruire dynamiquement les différents labels et lists
        for texte, dimension in columns:
            Label(
                self.libelle,
                kw,
                text=texte,
                width=dimension
            ).pack(side='left', expand='yes')
            listbox = Listbox(self.listboxs, width=dimension)
            listbox.pack(expand='yes', fill='both', side='left')
            self.columns.append(listbox)

if __name__ == '__main__':
    try:
        from Tkinter import Tk
    except ImportError:
        from tkinter import Tk
    fenetre = Tk()
    test =  TkListboxMulticolumn(fenetre, (
        ('Number', 10),
        ('Name', 40),
        ('Firstname', 40),
        ('City', 50)
    ))
    test.pack(side='top', expand='yes', fill='both')
    fenetre.mainloop()
