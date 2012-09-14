#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: request.py
Author: Hervé Beraud
Description: Application core.
Date 23/07/2012
Version 1.0
CopyRight Hervé Beraud
"""
from constante import GT_
from model.recherche import Recherche
from model.parametre import Parametre
from model.header import Header
import urllib
import threading
import queue
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
        self.header = Header()

    def search(self):
        """
        """
        q = queue.Queue()
        self.param = urlencode(self.param.myParam.get())
        self.recherche = urlparse(self.recherche.my_recherche.get())
        threading.Thread(target=self._requester, args=(q,)).start()
        print(q.get())

    def _requester(self, q):
        connection = httplib.HTTPConnection(self.recherche[1])
        connection.request("POST", "", self.param, self.header.my_header.get())
        response = connection.getresponse()
        connection.close()
        q.put(response.getheaders())

if __name__ == '__main__':
    test = Action()
