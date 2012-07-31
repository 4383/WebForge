#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: tkListboxMulticolumn.py
Author: Hervé Beraud
Description: Classe de génération de Listbox multicolonne
Date 24/07/2012
Version 1.0
CopyRight Hervé Beraud
"""
try:
    from Tkinter import Frame
    from Tkinter import Label
    from Tkinter import Listbox
except ImportError:
    from tkinter import Frame
    from tkinter import Label
    from tkinter import Listbox

class  TkListboxMulticolumn(Frame):
    """
    TkListboxMulticolumn component which can display multi-sortable listbox
    """

    def __init__(self, master, columns, cnf={}, **kw):
        """
        Construct a listbox widget with one or many column and label field for header

        Valid resource names: background, bd, bg, borderwidth, class, colormap,
        fg, font, foreground, height, highlightbackground,
        """
        Frame.__init__(self, master)
        if not columns:
            raise Exception('2 or many Columns required')

        # Construct label containers
        self.libelle = Frame(self)
        self.libelle.pack(side='top')
        # Construct Listbox containers
        self.listboxs = Frame(self)
        self.listboxs.pack(side='bottom', expand='yes', fill='both')
        self.columns = []

        # Contruct all columns (listbox) with title (label)
        for texte, dimension in columns:
            # Create title
            Label(
                self.libelle,
                kw,
                text=texte,
                width=dimension
            ).pack(side='left', expand='yes')
            # Create columns
            listbox = Listbox(self.listboxs, width=dimension, exportselection='false')
            listbox.pack(expand='yes', fill='both', side='left')
            # Bind all event for override
            listbox.bind('<B1-Motion>', lambda e, s=self: s._select(e.y))
            listbox.bind('<Button-1>', lambda e, s=self: s._select(e.y))
            listbox.bind('<Leave>', lambda e: 'break')
            # Add listbox to list
            self.columns.append(listbox)

    def _select(self, ordinate):
        """
        Configure the widget for call methods of
        all listbox when one list receive event select
        take ordinate position of mouse and convert this
        in position in listbox for get items
        """
        row = self.columns[0].nearest(ordinate)
        self.selection_clear(0, 'end')
        self.selection_set(row)
        return 'break'

    def insert(self, index, *elements):
        """
        Override of Listbox.insert methods
        index is the index to insert on
        elements is a tuple a element to insert on
        One tuple = one row
        One tuple.column = one column
        """
        for el in elements:
            i = 0
            for column in self.columns:
                column.insert(index, el[i])
                i = i + 1

    def selection_set(self, first, last=None):
        """
        Override Listbox method selection_set
        to make same select in many independant Listbox
        """
        for column in self.columns:
            column.selection_set(first, last)

    def selection_clear(self, first, last=None):
        """
        Override
        """
        for column in self.columns:
            column.selection_clear(first, last)

    def size(self):
        """
        Override Listbox method size.
        Return first column size
        """
        return self.columns[0].size()

if __name__ == '__main__':
    try:
        from Tkinter import Tk
    except ImportError:
        from tkinter import Tk
    fenetre = Tk()
    test =  TkListboxMulticolumn(fenetre, (
        ('Number', 10),
        ('Name', 40),
        ('Firstname', 40),
        ('City', 50)
    ))
    test.insert('end', (1, 'BERAUD', 'Hervé', 'Martigues'))
    test.insert('end', (1, 'BERAUD', 'Hervé', 'Martigues'))
    test.pack(side='top', expand='yes', fill='both')
    fenetre.mainloop()
