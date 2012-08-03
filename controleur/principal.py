#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
File: principal.py
Author: Hervé Beraud
Description: Primary controler
'''
import modele
from vue.fenetre import Fenetre as V_Fenetre
from vue.recherche import Recherche as V_Recherche
from vue.parametre import Parametre as V_Parametre
from modele.parametre import Parametre as M_Parametre
from controleur.parametre import Parametre as C_Parametre

class Principal:
    """
    Class Principal
    Bind all view and controlers
    """
    def __init__(self, root):
        """
        Construct of primary controler
        root = parent window tkinter
        """
        # Instanciate all transverse modele
        self.m_parametre = M_Parametre()
        # Instanciate all view
        self.v_fenetre = V_Fenetre(root)
        self.v_recherche = V_Recherche(root)
        self.v_parametre = V_Parametre(root)
        # Instanciate all controlers
        self.c_parametre = C_Parametre(self.v_parametre)
