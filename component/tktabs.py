#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: tktabs.py
Author: Hervé Beraud
Description: Tabs component for tkinter
Date 24/07/2012
Version 1.0
CopyRight Hervé Beraud
"""
try:
    from Tkinter import Frame
    from Tkinter import Button
    from Tkinter import Label
    from Tkinter import Entry
except ImportError:
    from tkinter import Frame
    from tkinter import Button
    from tkinter import Label
    from tkinter import Entry

class  Tabs(Frame):
    """
    Tabs class pluggins for tkinter.
    Provide a multi-tabs component.
    """

    def __init__(self, master, onglets=None, cnf={}, **kw):
        """
        Construct a Tabs component and join it to the master

        TODO : Add a valid resource implementation, to personnalize
        background, foreground
        """
        Frame.__init__(self, master)
        self.kw = kw
        self.onglets = []
        self.content = []
        self.frame_btn = Frame(self)
        self.frame_content = Frame(self)
        # Create all tabs
        if onglets:
            self.add_tabs(onglets)

        self.frame_btn.pack()
        self.frame_content.pack(side='bottom')

        # Create canvas for drawing in

    def add_tabs(self, tabs=None):
        """
        Add tab or lot of tabs
        tabs args is a list of dict where dict is a single tab
        format of dict is :
            * title => title for this tab
            * content => content for this tab

        If no title's defined the default title as NaN
        If no centent's defined the default content is the index of the tabs
        """
        if not tabs or len(tabs) == 0:
            raise TabsError('Tabs args is required.')
        for current_tabs in tabs:
            # Button configure
            button = Button(
                self.frame_btn,
                text=current_tabs.get('title', 'NaN')
            )
            button.configure(
                state='disabled',
                relief='flat',
                highlightbackground='white'
            )
            button.pack(side='left')
            # Content configure
            #content = Frame(self.frame_content)
            content = current_tabs.get(
                'content',
                Label(text='Tab %s' % len(self.content))
            )
            content.config()
            arguments = {'button' : button, 'content' : content}
            button.bind(
                '<Button-1>',
                lambda event,
                args=arguments: self.show_tabs(event, args)
            )
            #component = current_tabs.get('content', Label(text='Tabs %d' % len(self.onglets)))
            #component.pack(side='bottom')
            self.onglets.append(button)
            self.content.append(content)
            if len(self.onglets) == 1:
                button.configure(state='normal', highlightbackground='gray')
                content.pack(side='bottom', fill='both', expand='yes')

    def delete_tabs_by_index(self, index):
        """
        Deleting tab positioned at the index 'index'
        """
        if type(index) != type(int()):
            raise TabsError('Bad value for index deleting')
        try:
            if len(self.onglets) > 0:
                if self.onglets[index].winfo_ismapped():
                    self.onglets[index].pack_forget()
                self.onglets.pop(index)
                if self.content[index].winfo_ismapped():
                    self.content[index].pack_forget()
                self.content.pop(index)
        except IndexError:
            raise TabsError('Index to delete is out of range')

    def delete_tabs_by_value(self, value):
        """
        Deleting tab matching with the parameter value
        """
        print("base %s" % value)
        for el in self.content:
            print(value)
        if value in self.content:
            index = self.content.index(value)
            self.onglets.pop(index)
            self.content.pop(index)

    def contains(self, tab):
        """
        Return True if tab is in tabs list else False
        """
        if tab in self.onglets():
            return True
        return False

    def _reset_content(self):
        """
        Reset all content for tabs.
        Every all tabs have no focus.
        """
        for tab in self.content:
            if tab.winfo_ismapped():
                tab.pack_forget()

    def _reset_button(self):
        """
        Reset all button (tabs switcher) for tabs.
        Every all tabs have no focus.
        """
        for tab in self.onglets:
            tab.configure(state='disabled', highlightbackground='white')

    def show_tabs(self, event, args):
        """
        Set focus at tab after click tab event
        """
        # Initialize display
        self._reset_content()
        self._reset_button()
        # Display the current tabs
        args['button'].configure(state='normal', highlightbackground='gray')
        args['content'].pack()

class TabsError(Exception):
    """
    Class type exception for raise error in tabs component
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

if __name__ == '__main__':
    try:
        from Tkinter import Tk
    except ImportError:
        from tkinter import Tk
    fenetre = Tk()
    frame_test_1 = Frame()
    btn_test_1 = Button(frame_test_1, text='test')
    btn_test_1.pack()
    test =  Tabs(
        fenetre,
        [
            {'title' : 'test1'},
            {'content' : Entry()},
            {'title' : 'test2', 'content' : frame_test_1}
        ],
        bg='yellow',
        border=1,
        relief='raised'
    )
    test.pack(side='top', expand='yes', fill='both')
    btn_test_2 = Button(text='add')
    btn_test_2.bind('<Button-1>', lambda event: test.add_tabs([{'title' : 'after'}]))
    test.add_tabs([{'content' : btn_test_2}])
    btn_test_1.bind('<Button-1>', lambda event: test.delete_tabs_by_index(1))
    btn_test_3 = Button(text='delete by value')
    btn_test_3.bind('<Button-1>', lambda event: test.delete_tabs_by_value(btn_test_2))
    test.add_tabs([{'content' : btn_test_3}])
    fenetre.mainloop()

