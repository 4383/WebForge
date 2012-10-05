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
from datetime import datetime
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
        url = "%s%s%s" % (
            self.recherche[1],
            self.recherche[2],
            self.recherche[3]
        )
        ok, response, timer = self._requester()
        if not ok:
            self.error = Error()
            self.error.add_param(
                GT_('Erreur'),
                GT_('Url injoignable : %s\n%s') % (url, response)
            )
        else:
            self.result = Result()
            self.result.unset()
            # Request information (url, execution time)
            self.result.add_param(
                GT_('http://%s en %d.%06d secondes') % (
                    url,
                    timer.seconds,
                    timer.microseconds
                ),
                '%s : %s' % (response.status, response.reason)
            )
            # Request information (url, execution time)
            self.result.add_param(
                GT_('Entetes'),
                response.getheaders()
            )
            version = 1.0
            if response.version == 11:
                version = 1.1

            self.result.add_param(
                GT_('Version du protocole'),
                GT_('HTTP/%s' % version)
            )
        q.task_done()

    def _requester(self):
        """
        Execute request and return result
        """
        try:
            methode = 'POST'
            if not self.param:
                methode = 'GET'
            debut = datetime.now()
            connection = httplib.HTTPConnection(self.recherche[1])
            connection.request(
                methode,
                '%s/%s' % (self.recherche[2], self.recherche[3]),
                self.param,
                self.header.my_header.get()
            )
            response = connection.getresponse()
            connection.close()
            timer = datetime.now() - debut
            return True, response, timer
        except socket.gaierror:
            return False, GT_("Socket erreur"), None
        except http.client.InvalidURL:
            return False, GT_("Url non valide"), None

if __name__ == '__main__':
    test = Action()
