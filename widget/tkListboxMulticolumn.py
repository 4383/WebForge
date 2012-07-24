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
except ImportError:
    from tkinter import Frame
    from tkinter import Label

class  TkListboxMulticolumn(Frame):
    """
    Class  TkListboxMulticolumn

    """

    def __init__(self, root, columns):
        """
        Constructeur de la classe TkListboxMulticolumn
        root = La fenetre parente
        columns = Les colonnes à générer
        """
        self.Conteneur = Frame(root)
        self.Conteneur.pack(expand='yes', fill='both')
        self.libelle = Frame(self.Conteneur)
        self.libelle.pack(side='top', expand='yes', fill='both')
        self.columns = []

        for texte, dimension in columns:
            lab = Label(
                self.libelle,
                text=texte,
                borderwidth=1,
                relief='raised',
                width=dimension
            )
            lab.pack(side='left')

if __name__ == '__main__':
    try:
        from Tkinter import Tk
    except ImportError:
        from tkinter import Tk
    fenetre = Tk()
    test =  TkListboxMulticolumn(fenetre, (('test', 40), ('test2', 20)))
    fenetre.mainloop()

