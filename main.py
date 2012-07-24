#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
Système de bascule entre fichiers host
"""

import tkinter
from page import principal

if __name__ == "__main__":
    fenetrePrincipal = tkinter.Tk()
    page = principal.Principal(fenetrePrincipal)
    fenetrePrincipal.mainloop()
