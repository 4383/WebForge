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
from constante import GT_
try:
    import tkMessageBox as messagebox
except ImportError:
    from tkinter import messagebox

class Header:
    """
    Class Parametre
    Classe de controle de la vue "parametre"
    """

    def __init__(self, vue, model):
        """
        Constructeur du controleur de la vue "parametre"
        A à sa charge la gestion des événements sur la vue "vue.parametre"
        """
        self.vue = vue
        self.model = model
        self.model.my_header.add_callback(self.param_change)
        self.vue.btn_ajouter.bind('<Button-1>', self.ajouterListe)
        self.vue.btn_delete.bind('<Button-1>', self.retirerListe)

    def ajouterListe(self, event):
        """
        Ajouter les informations saisie dans les
        champs nom et parametre à la listbox
        """
        nom = self.vue.nom.get()
        param = self.vue.valeur.get()
        # Vérifier si le nom du paramêtre est saisie
        if not nom:
            self.message(GT_('Le nom du paramêtre est obligatoire'))
            return
        # Vérifier si la valeur du paramêtre est saisie
        if not param:
            self.message(GT_('La valeur du paramêtre est obligatoire'))
            return
        # Insérer le nom et la valeur dans la liste
        self.model.add_param(nom, param)
        self.effacerformulaireSaisie(event)

    def retirerListe(self, event):
        """
        Delete select row from listbox
        """
        item = self.vue.lsparam.get(self.vue.lsparam.curselection()[0])
        self.model.del_param(item)

    def param_change(self, liste):
        """
        Check parameters list change
        """
        self.vue.set_liste(liste)

    def effacerformulaireSaisie(self, event):
        """
        Effacer les données affichées dans le formulaire de
        saisie des données
        """
        self.vue.nom.delete(0, 'end')
        self.vue.valeur.delete(0, 'end')

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
    test = Header()
