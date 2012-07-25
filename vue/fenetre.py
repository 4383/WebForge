#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
"""

class Fenetre():
    """
    Vue principal
    """
    def __init__(self, fenetre):
        """
        Constructeur de la fenetre
        """
        self.fenetre = fenetre
        self.fenetre.title("WebForge")
        self.fenetre.geometry("800x600+50+50")
