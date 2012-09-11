#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: menubar.py
Author: Hervé Beraud
Description: Controler la zone parametre
Date 23/07/2012
Version 1.0
CopyRight Hervé Beraud
"""
from constante import GT_
try:
    import tkMessageBox as messagebox
except ImportError:
    from tkinter import messagebox

class Menubar:
    """
    Class Menubar
    Classe de controle de la vue "menubar"
    """

    def __init__(self, vue, vues):
        """
        Constructeur du controleur de la vue "parametre"
        A à sa charge la gestion des événements sur la vue "vue.parametre"
        """
        self.vue = vue
        self.vues = vues
        self.init_menu_fichier(None)
        self.init_menu_affichage(None)

    def init_menu_fichier(self, event):
        """
        Initialize fichier menu
        """

    def init_menu_affichage(self, event):
        """
        Initialize affichage menu
        """
        self.vues['parametre'].visible()
        self.vue.affichage.entryconfig(0, command=self.vues['parametre'].visible)
        self.vues['header'].visible()
        self.vue.affichage.entryconfig(1, command=self.vues['header'].visible)

    def init_menu_aide(self, liste):
        """
        Initialize aide menu
        """

    def message(self, message):
        """
        Show messagebox with contains somes informations
        """
        messagebox.showinfo(
            GT_('Menu'),
            message
        )

if __name__ == '__main__':
    test = Menubar()


