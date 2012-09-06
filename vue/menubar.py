#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
"""
from constante import GT_
try:
    from Tkinter import Menu
except ImportError:
    from tkinter import Menu

class Menubar():
    """
    Vue du menu
    """
    def __init__(self, fenetre):
        """
        Construteur du menu
        """
        self.menu = Menu(fenetre)
        self.menu.add_command(label="test")
        fenetre.config(menu=self.menu)
        #self.frame_top = Frame(fenetre, borderwidth=1, relief='groove', width=100)
        #self.frame_top.pack( side='top', fill='both')
        #self.titre = Label(self.frame_top, text=GT_('Url'), font=(20))
        #self.titre.pack()
        #self.img = PhotoImage(file="%slogo.gif" % RESSOURCES_PATH)
        #self.logo = Label(self.frame_top, image=self.img)
        #self.logo.pack(pady=(0, 20), side="left")
        #self.brand = Label(self.frame_top, text=GT_('WebForge %s' % VERSION), font=(20))
        #self.brand.pack(pady=(10, 20), padx=(0, 20), side="left")
        #self.txt_recherche = Entry(self.frame_top, font=(22))
        #self.txt_recherche.pack(pady=(0, 20), expand='yes', fill='both', side='left')
        #self.btn_go = Button(self.frame_top, text="GO")
        #self.btn_go.pack(pady=(0, 20), side='right')
        #self.btn_erase = Button(self.frame_top, text="X")
        #self.btn_erase.pack(pady=(0, 20), side='right')
