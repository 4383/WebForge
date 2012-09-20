#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
File: principal.py
Author: Hervé Beraud
Description: Primary controler
'''
from model.parametre import Parametre as M_Parametre
from model.recherche import Recherche as M_Recherche
from model.header import Header as M_Header
from model.result import Result as M_Result
from vue.fenetre import Fenetre as V_Fenetre
from vue.menubar import Menubar as V_Menubar
from vue.recherche import Recherche as V_Recherche
from vue.parametre import Parametre as V_Parametre
from vue.result import Result as V_Result
from vue.header import Header as V_Header
from vue.status import Status as V_Status
from vue.onglet import Onglet as V_Onglet
from controleur.menubar import Menubar as C_Menubar
from controleur.parametre import Parametre as C_Parametre
from controleur.recherche import Recherche as C_Recherche
from controleur.header import Header as C_Header
from controleur.result import Result as C_Result

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
        self.m_recherche = M_Recherche()
        self.m_header = M_Header()
        self.m_result = M_Result()
        # Instanciate all view
        self.v_fenetre = V_Fenetre(root)
        self.v_menubar = V_Menubar(root)
        self.v_recherche = V_Recherche(self.v_fenetre.top)
        self.v_parametre = V_Parametre(self.v_fenetre.left)
        self.v_result = V_Result(self.v_fenetre.right)
        self.v_header = V_Header(self.v_fenetre.right)
        self.v_status = V_Status(self.v_result.frame)
        self.v_onglet = V_Onglet(self.v_result.frame)
        # Instanciate all controlers
        self.c_menubar = C_Menubar(
            self.v_menubar,
            {
            'parametre' : self.v_parametre,
            'header' : self.v_header,
            }
        )
        self.c_parametre = C_Parametre(self.v_parametre, self.m_parametre)
        self.c_recherche = C_Recherche(
            self.v_recherche,
            self.m_recherche,
            self.v_status
        )
        self.c_parametre = C_Header(self.v_header, self.m_header)
        self.c_result = C_Result(self.v_onglet, self.m_result)
