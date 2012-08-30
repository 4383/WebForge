#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
File: constante.py
Author: Hervé Beraud
Description: Fichier de constantes
Date 20/07/2012
Version 1.0
CopyRight Hervé Beraud
"""
import gettext
import os

APP_NAME = 'WebForge'
APP_PATH_TRAD = '%s%slg' % (os.getcwd(), os.sep)
RESSOURCES_PATH = '%s%sressources%s' % (os.getcwd(), os.sep, os.sep)
VERSION = 0.1

gettext.bindtextdomain(APP_NAME, APP_PATH_TRAD)
gettext.textdomain(APP_NAME)
GT_ = gettext.gettext

if __name__ == '__main__':
    print(APP_NAME)
    print(APP_PATH_TRAD)
    print(RESSOURCES_PATH)
