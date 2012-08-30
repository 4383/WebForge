#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: Recherche.py
Author: Hervé Beraud
Description: Controler la zone Recherche
Date 23/07/2012
Version 1.0
CopyRight Hervé Beraud
"""
from constante import GT_
try:
    import tkMessageBox as messagebox
except ImportError:
    from tkinter import messagebox

class Recherche:
    """
    Class Recherche
    Classe de controle de la vue "Recherche"
    """

    def __init__(self, vue, model):
        """
        Constructeur du controleur de la vue "Recherche"
        A à sa charge la gestion des événements sur la vue "vue.Recherche"
        """
        self.vue = vue
        self.model = model
        self.model.my_recherche.add_callback(self.param_change)
        self.vue.btn_erase.bind('<Button-1>', self.effacerformulaireSaisie)

    def param_change(self, url):
        """
        Check parameters list change
        """
        self.vue.set_url(url)

    def lancerRecherche(self, event):
        """
        Launch url, and run request
        """

    def effacerformulaireSaisie(self, event):
        """
        Clear field url
        """
        self.vue.txt_recherche.delete(0, 'end')

    def message(self, message):
        """
        Afficher une boite de dialogue
        avec un message personnalisé
        """
        messagebox.showinfo(
            GT_('Paramêtres'),
            message
        )

if __name__ == '__main__':
    test = Recherche()

