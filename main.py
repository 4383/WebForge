#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
Système de bascule entre fichiers host
"""

import tkinter
from controleur import principal
import observateur

if __name__ == "__main__":
    fenetrePrincipal = tkinter.Tk()
    controleur = principal.Controleur(fenetrePrincipal)
    fenetrePrincipal.mainloop()
