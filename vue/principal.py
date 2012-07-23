#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
"""

import tkinter as tk
import tkinter.messagebox

class Fenetre(tk.Toplevel):
    """
    Vue principal
    """
    def __init__(self, fenetre):
        """
        Constructeur de la fenetre
        """
        tk.Toplevel.__init__(self, fenetre)
        self.title("WebForge")
        self.geometry("800x600+50+50")
        self.protocol('WM_DELETE_WINDOW', self.destroy)

#    def afficher(self, event):
#        """
#        Afficher une boite de dialogue
#        """
#        tkinter.messagebox.showinfo("test", "test")
