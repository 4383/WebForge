#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: request.py
Author: Hervé Beraud
Description: Controler la zone Recherche
Date 23/07/2012
Version 1.0
CopyRight Hervé Beraud
"""
from constante import GT_
from model.recherche import Recherche
from model.parametre import Parametre
import urllib
try:
    from urllib.parse import urlparse
    from urllib.parse import urlencode as urlencode
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
try:
    import http.client as httplib
except ImportError:
    import httplib

class Action:
    """
    Class Recherche
    Classe de controle de la vue "Recherche"
    """

    def __init__(self):
        """
        Constructeur du controleur de la vue "Recherche"
        A à sa charge la gestion des événements sur la vue "vue.Recherche"
        """
        self.param = Parametre()
        self.recherche = Recherche()

    def search(self):
        """
        """
        self.param = urlencode(self.param.myParam.get())
        self.recherche = urlparse(self.recherche.my_recherche.get())

        connection = httplib.HTTPConnection(self.recherche[1])
        connection.request("POST", "", self.param)
        response = connection.getresponse()
        print(response.getheaders())

if __name__ == '__main__':
    test = Action()
