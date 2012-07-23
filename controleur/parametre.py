#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: parametre.py
Author: Hervé Beraud
Description: Controler la zone parametre
Date 23/07/2012
Version 1.0
CopyRight Hervé Beraud
"""

class Parametre:
    """
    Class Parametre
    Classe de controle de la vue "parametre"
    """

    def __init__(self, vue):
        """
        Comments
        """
        self.vue = vue
        self.vue.btn_ajouter.bind('<Button-1>', self.ajouterListe)

    def ajouterListe(self, event):
        """
        Ajouter les informations saisie dans les
        champs nom et parametre à la listbox
        """
        self.vue.listparam.insert(self.vue.nom.get())

if __name__ == '__main__':
    test = Parametre()

