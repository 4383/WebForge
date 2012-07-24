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
# Importer la version 2
try:
    from Tkinter import Frame
    from Tkinter import Button
    from Tkinter import Listbox
    from Tkinter import Entry
    from Tkinter import Label
# Gérer l'erreur en important la version 3
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
        Initialiser la classe
        fenetre = fenetre parente ou seront collé les éléments
        """
        # La frame principale
        self.frame = Frame(fenetre, borderwidth=3, relief='raised', width=40)
        self.frame.pack(fill='both', side='left', pady=10)
        self.titre = Label(self.frame, text=_('Paramêtres'), font=(20))
        self.titre.pack()
        self.creer_zone_de_saisie()
        # Les éléments directement contenu dans la frame principale
        self.frame_list = Frame(self.frame, width=40)
        self.frame_list.pack(side='bottom', fill='both', expand='yes')
        self.listparam_nom = Listbox(self.frame_list, width=20)
        self.listparam_nom.pack(expand='yes', fill='both', side='left')
        self.listparam_valeur = Listbox(self.frame_list, width=20)
        self.listparam_valeur.pack(expand='yes', fill='both', side='right')

    def creer_zone_de_saisie(self):
        """
        Générer la zone de saisie des parametres
        """
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
        self.btn_ajouter = Button(self.frame_saisie, text=_('Ajouter'))
        self.btn_ajouter.pack(side='top')

if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()
    test = Parametre(root)

