#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
Système de bascule entre fichiers host
"""

import modele
from vue import fenetre
from vue import recherche
from vue import parametre
from controleur import parametre as CtrlParametre

class Principal:
    """
    Class Principal
    """
    def __init__(self, fenetreRacine):
        """
        Contructeur de la classe Controleur
        Prend en parametre la fenetre parente
        """
        self.fenetre = fenetre.Fenetre(fenetreRacine)
        self.recherche = recherche.Recherche(fenetreRacine)
        self.parametre = parametre.Parametre(fenetreRacine)
        self.ctrlparametre = CtrlParametre.Parametre(self.parametre)
