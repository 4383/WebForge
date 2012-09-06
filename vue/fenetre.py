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
        w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenwidth()
        self.fenetre = fenetre
        self.fenetre.title("WebForge")
        self.fenetre.geometry("%dx%d+0+0" % (w, h))
