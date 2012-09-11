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
from constante import GT_
from component.tkListboxMulticolumn import TkListboxMulticolumn
from vue.vue import Vue
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

class Header(Vue):
    """
    """

    def __init__(self, fenetre):
        """
        Initialiser la classe
        fenetre = fenetre parente ou seront collé les éléments
        """
        # La frame principale
        super(Header, self).__init__()
        self.frame = Frame(fenetre, borderwidth=1, relief='groove', width=40)
        self.titre = Label(self.frame, text=GT_('Entêtes'), font=(20))
        self.titre.pack()
        self.creer_zone_de_saisie()
        self.creer_liste()

    def visible(self):
        """
        Override the parent method for config element visibility
        """
        super(Header, self).visible(fill='both', side='right', pady=0)

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
        self.label_valeur = Label(self.frame_saisie, text=GT_('Valeur'))
        self.label_valeur.pack()
        self.valeur = Entry(self.frame_saisie)
        self.valeur.pack(fill='both')
        self.btn_ajouter = Button(self.frame_saisie, text=GT_('Ajouter'))
        self.btn_ajouter.pack(side='top')

    def creer_liste(self):
        """
        Creer les elements affichant la liste de parametres
        """
        self.lsparam = TkListboxMulticolumn(self.frame, ((GT_('Nom'), 20),(GT_('Valeur'), 20)), relief='groove')
        self.lsparam.pack(expand='yes', fill='both')
        self.btn_delete = Button(self.frame, text=GT_('Supprimer'))
        self.btn_delete.pack(side='bottom')

    def set_liste(self, liste):
        """
        Update parameters list
        """
        self.lsparam.delete(0, 'end')
        for key, value in  liste.items():
            self.lsparam.insert('end', (key, value))

if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()
    test = Header(root)


