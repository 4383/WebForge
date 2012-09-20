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
# Standard lib
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
import socket
# Personal package and module
from constante import GT_
from model.recherche import Recherche
from model.parametre import Parametre
from model.header import Header
from model.result import Result
from model.error import Error
import core.formateur as formateur

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

    def search(self, q):
        """
        Prepare elements for request and play it
        """
        self.param = urlencode(self.param.myParam.get())
        self.recherche = urlparse(self.recherche.my_recherche.get())
        self.url = "%s%s%s" % (self.recherche[1], self.recherche[2], self.recherche[3])
        response = self._requester()
        if not response:
            self.error = Error()
            self.error.add_param(GT_('Erreur'), GT_('Url injoignable : %s') % self.url)
        else:
            self.result = Result()
            self.result.add_param(GT_('OK'), GT_('OK'))
        q.task_done()

    def _requester(self):
        """
        Execute request and return result
        """
        try:
            methode = 'POST'
            if not self.param:
                methode = 'GET'
            print(self.url)
            connection = httplib.HTTPConnection(self.url)
            connection.request(methode, "", self.param, self.header.my_header.get())
            response = connection.getresponse()
            connection.close()
            return response
        except socket.gaierror:
            print("Socket error")
            return False
        except http.client.InvalidURL:
            print("Invalid url")
            return False

if __name__ == '__main__':
    test = Action()
