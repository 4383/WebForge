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
    from Tkinter import Canvas
except ImportError:
    from tkinter import Frame
    from tkinter import Canvas

class  TkProgessBar(Frame):
    """
    TkListboxMulticolumn component which can display multi-sortable listbox
    """

    def __init__(self, master, cnf={}, **kw):
        """
        Construct a listbox widget with one or many column and label field for header

        Valid resource names: background, bd, bg, borderwidth, class, colormap,
        fg, font, foreground, height, highlightbackground,
        """
        Frame.__init__(self, master)
        self._value = kw.get('value', 0.0)

        # Create canvas for drawing in
        self._canvas = Canvas(
            self,
            bg=kw.get('bg', 'white'),
            width=kw.get('width', 300),
            height=kw.get('height', 20),
            relief=kw.get('relief', 'sunken'),
            border=kw.get('border', 1)
        )
        self._canvas.pack(fill='both', expand='yes')
        # Drawing a rectangle
        self._rect = self._canvas.create_rectangle(
            0,
            0,
            0,
            self._canvas.winfo_reqheight(),
            fill=kw.get('fillcolor', 'blue'),
            width=0
        )
        # Drawing a text area
        self._text = self._canvas.create_text(
            self._canvas.winfo_reqwidth()/2,
            self._canvas.winfo_reqheight()/2,
            text='',
            fill=kw.get('textcolor', 'gray')
        )
        self.bind('<Configure>', self._update_coords)

    def _update_coords(self, event):
        '''Updates the position of the text and rectangle inside the canvas when the size of
        the widget gets changed.'''
        # looks like we have to call update_idletasks() twice to make sure
        # to get the results we expect
        self._canvas.update_idletasks()
        self._canvas.coords(self._text, self._canvas.winfo_width()/2, self._canvas.winfo_height()/2)
        self._canvas.coords(self._rect, 0, 0, self._canvas.winfo_width()*self._value, self._canvas.winfo_height())
        self._canvas.update_idletasks()

    def get(self, first, last=None):
        """
        return percent and text value
        """
        return self._value, self._canvas.itemcget(self._text, 'text')

    def set(self, value=0.0, text=None):
        '''
        Set different values.
        '''
        #make the value failsafe:
        if value < 0.0:
            value = 0.0
        elif value > 1.0:
            value = 1.0
        self._value = value
        if text == None:
            #if no text is specified use the default percentage string:
            text = str(int(round(100 * value))) + ' %'
        self._canvas.coords(self._rect, 0, 0, self._canvas.winfo_width()*value, self._canvas.winfo_height())
        self._canvas.itemconfigure(self._text, text=text)
        self._canvas.update_idletasks()

if __name__ == '__main__':
    try:
        from Tkinter import Tk
    except ImportError:
        from tkinter import Tk
    fenetre = Tk()
    test =  TkProgessBar(fenetre, bg='yellow', border=1, relief='raised')
    test.pack(side='top', expand='yes', fill='both')
    fenetre.mainloop()
