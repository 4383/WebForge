#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
Système de bascule entre fichiers host
"""

from controleur.principal import Principal
try:
    import Tkinter as tkinter
except ImportError:
    import tkinter

if __name__ == "__main__":
    fenetrePrincipal = tkinter.Tk()
    page = Principal(fenetrePrincipal)
    fenetrePrincipal.mainloop()
