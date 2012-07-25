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

class  TkListboxMulticolumn():
    """
    Class  TkListboxMulticolumn

    """

    def __init__(self, root, columns):
        """
        Constructeur de la classe TkListboxMulticolumn
        root = La fenetre parente
        columns = Les colonnes à générer
        """
        if not columns:
           raise Exception('No data imported')

        # Construire le conteneur qui contiendra tout nos élements
        self.Conteneur = Frame(root)
        # Construire le contenur de label
        self.libelle = Frame(self.Conteneur)
        self.libelle.pack(side='top')
        # Construire le conteneur de listbox
        self.listboxs = Frame(self.Conteneur)
        self.listboxs.pack(side='bottom', expand='yes', fill='both')
        self.columns = []

        # Contruire dynamiquement les différents labels et lists
        for texte, dimension in columns:
            Label(
                self.libelle,
                text=texte,
                borderwidth=1,
                relief='raised',
                width=dimension
            ).pack(side='left')
            listbox = Listbox(self.listboxs, width=dimension)
            listbox.pack(expand='yes', fill='both', side='left')
            self.columns.append(listbox)

    def pack(self, side='top', expand='no', fill='both'):
        self.Conteneur.pack(side=side, expand=expand, fill=fill)

if __name__ == '__main__':
    try:
        from Tkinter import Tk
    except ImportError:
        from tkinter import Tk
    fenetre = Tk()
    test =  TkListboxMulticolumn(fenetre, (('test', 40), ('test2', 20), ('test3', 30)))
    #test =  TkListboxMulticolumn(fenetre, "")
    fenetre.mainloop()
