#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: parametre.py
Author: Hervé Beraud
Description: Vue en charge de la saisie et l'affichage
des parametre
Date 19/07/2012
Version 1.0
CopyRight Hervé Beraud
"""
import gettext
from constante import *
try:
    from Tkinter import Frame
    from Tkinter import Button
    from Tkinter import Listbox
    from Tkinter import Entry
    from Tkinter import Label
except ImportError:
    from tkinter import Frame
    from tkinter import Button
    from tkinter import Listbox
    from tkinter import Entry
    from tkinter import Label

gettext.bindtextdomain(APP_NAME, APP_PATH_TRAD)
gettext.textdomain(APP_NAME)
_ = gettext.gettext

class  Parametre():
    """
    """

    def __init__(self, fenetre):
        """
        Comments
        """
        # La frame principale
        self.frame = Frame(fenetre, borderwidth=3, relief='raised', width=40)
        self.frame.pack( fill='both', side='left', pady=10)
        self.titre = Label(self.frame, text=_('Paramêtres'), font=(20))
        self.titre.pack()
        # Créer la zone de saisie
        self.frame_saisie = Frame(self.frame, relief='groove', width=35, borderwidth=1)
        self.frame_saisie.pack(pady=10, padx=10, fill='both', side='top')
        self.label_nom = Label(self.frame_saisie, text='Nom')
        self.label_nom.pack()
        self.nom = Entry(self.frame_saisie)
        self.nom.pack(fill='both')
        self.label_valeur = Label(self.frame_saisie, text=_('Valeur'))
        self.label_valeur.pack()
        self.valeur = Entry(self.frame_saisie)
        self.valeur.pack(fill='both')
        self.bt = Button(self.frame_saisie, text=_('Ajouter'))
        self.bt.pack(side='top')
        # Les éléments directement contenu dans la frame principale
        self.listparam = Listbox(self.frame, width=40)
        self.listparam.grid_configure(row=2, rowspan=3, column=0, columnspan=2)
        self.listparam.pack(side='bottom', expand='yes', fill='both')

if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()
    test = Parametre(root)

