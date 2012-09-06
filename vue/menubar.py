#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
"""
from constante import GT_
try:
    from Tkinter import Menu
except ImportError:
    from tkinter import Menu

class Menubar():
    """
    Vue du menu
    """
    def __init__(self, fenetre):
        """
        Construteur du menu
        """
        self.menu = Menu(fenetre)
        self.set_fichier()
        self.set_affichage()
        self.set_aide()
        fenetre.config(menu=self.menu)

    def set_fichier(self):
        """
        Create the "Fichier" menu and sub-menu
        """
        self.fichier = Menu(self.menu, tearoff=0)
        self.fichier.add_command(label=GT_("Quitter"))
        self.menu.add_cascade(label=GT_("Fichier"), menu=self.fichier)

    def set_affichage(self):
        """
        Create the "Affichage" menu and sub-menu
        """
        self.affichage = Menu(self.menu, tearoff=0)
        self.affichage.add_command(label=GT_("Paramêtres"))
        self.affichage.add_command(label=GT_("Entêtes"))
        self.menu.add_cascade(label=GT_("Affichage"), menu=self.affichage)

    def set_aide(self):
        """
        Create the "Fichier" menu and sub-menu
        """
        self.aide = Menu(self.menu, tearoff=0)
        self.aide.add_command(label=GT_("A propos"))
        self.menu.add_cascade(label=GT_("Aide"), menu=self.aide)
