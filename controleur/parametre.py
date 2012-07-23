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
import gettext
from constante import *
try:
    from Tkinter import messagebox
except ImportError:
    from tkinter import messagebox

gettext.bindtextdomain(APP_NAME, APP_PATH_TRAD)
gettext.textdomain(APP_NAME)
_ = gettext.gettext

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
        nom = self.vue.nom.get()
        param = self.vue.valeur.get()
        if not nom:
            self.message(_('Le nom du paramêtre est obligatoire'))
            return
        if not param:
            self.message(_())
        self.vue.listparam.insert(
            self.vue.listparam.size(),
            nom
        )
        self.formulaireSaisie(event)

    def formulaireSaisie(self, event):
        """
        Effacer les données affichées dans le formulaire de
        saisie des données
        """
        self.vue.nom.delete(0, 'end')
        self.vue.valeur.delete(0)

    def message(self, message):
        """
        Afficher une boite de dialogue
        """
        messagebox.showinfo(
            _('Paramêtres'),
            message
        )

if __name__ == '__main__':
    test = Parametre()

