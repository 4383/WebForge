#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
File: vue.py
Author: Hervé Beraud
Description: Parent view for all view
des parametre
Date 19/07/2012
Version 1.0
CopyRight Hervé Beraud
"""

import os

class Vue():
    """
    Contains all basic methods and config
    """
    def __init__(self):
        """
        Builder
        """
        self.is_visible = False
        self.frame = None

    def visible(self, **options):
        """
        Set the parent view visibility
        """
        # Hide
        if self.is_visible:
            self.frame.pack_forget()
            self.is_visible = False
        # Show
        else:
            self.frame.pack(**options)
            self.is_visible = True

