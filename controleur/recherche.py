#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: Recherche.py
Author: Hervé Beraud
Description: Controler la zone Recherche
Date 23/07/2012
Version 1.0
CopyRight Hervé Beraud
"""
from constante import GT_
from core.request import Action
import threading
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
try:
    import tkMessageBox as messagebox
except ImportError:
    from tkinter import messagebox

class Recherche:
    """
    Class Recherche
    Classe de controle de la vue "Recherche"
    """

    def __init__(self, vue, model, vue_status):
        """
        Constructeur du controleur de la vue "Recherche"
        A à sa charge la gestion des événements sur la vue "vue.Recherche"
        """
        self.vue = vue
        self.model = model
        self.vue_status = vue_status
        self.model.my_recherche.add_callback(self.param_change)
        self.vue.btn_erase.bind('<Button-1>', self.effacerformulaireSaisie)
        self.vue.btn_go.bind('<Button-1>', self.lancerRecherche)

    def param_change(self, url):
        """
        Check parameters list change
        """
        self.effacerformulaireSaisie(None)
        self.vue.set_url(url)

    def lancerRecherche(self, event):
        """
        Launch url, and run request
        """
        from queue import Queue
        # UI is busy
        self._busy()
        self._loading_ok = False
        self.vue.parent.update_idletasks()
        q = Queue()
        url = self.vue.txt_recherche.get()
        # Check url validity
        if not self._is_valide(url):
            return False
        self.model.add_param(url)
        action = Action()
        request = threading.Thread(target=action.search, args=(q,))
        request.start()
        q.put(request)
        q.join()
        self._loading_ok = True
        self._loader(1.0)
        # Free UI
        self._free()

    def _is_valide(self, url):
        """
        Check if the url as valide
        """
        if not url:
            self.message(GT_('Vous devez saisir obligatoirement une url'))
            self._free()
            return False
        urltest = urlparse(url)
        if not urltest[0]:
            self.message(GT_('''Format d'url non valide '''))
            self._free()
            return False
        if "http" not in urltest[0]:
            self.message(GT_('Protocole non pris en chage : %s' % urltest[0]))
            self._free()
            return False
        return True

    def _loader(self, value):
        """
        """
        self.vue_status.progressbar.set(value)
        if value < 1.0 and not self._loading_ok:
            value = value + 0.005
            self.vue_status.progressbar.after(50, lambda: self._loader(value))
        else:
            self.vue_status.progressbar.set(1.0, GT_('Chargement terminé'))

    def _busy(self):
        """
        Set the application busy
        """
        self.vue.txt_recherche.config(state="disabled")
        self.vue.btn_go.config(state="disabled")
        self.vue.btn_erase.config(state="disabled")
        self.vue.parent.config(cursor='watch')
        self.vue_status.progressbar.set(0.0, GT_('Connexion...'))
        self.vue_status.progressbar.after(50, lambda: self._loader(0.0))

    def _free(self):
        """
        Set the application not busy
        """
        self.vue.txt_recherche.config(state="normal")
        self.vue.btn_go.config(state="normal")
        self.vue.btn_erase.config(state="normal")
        self.vue.parent.config(cursor='arrow')
        self.vue_status.progressbar.after(
            3000,
            lambda: self.vue_status.progressbar.set(0.0, GT_(''))
        )

    def effacerformulaireSaisie(self, event):
        """
        Clear field url
        """
        self.vue.txt_recherche.delete(0, 'end')

    def message(self, message):
        """
        Afficher une boite de dialogue
        avec un message personnalisé
        """
        messagebox.showinfo(
            GT_('Recherche'),
            message
        )

if __name__ == '__main__':
    test = Recherche()


