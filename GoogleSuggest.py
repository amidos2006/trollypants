#!/usr/bin/python
# -*- coding: utf-8 -*-

##################################################
#       Google Suggest Grabber
#-------------------------------------------------
#   Copyright:    (c) 2010 by Damjan Krstevski.
#   License:      GNU General Public License v3
#   Feedback:     krstevsky[at]gmail[dot]com
##################################################

"""
GoogleSuggest
This module will help you to grab the Google suggestion for some expression

Usage:
    # Create instance without given value
    GoogleSuggest()
    # Create instance with given value
    GoogleSuggest( expression )
    # Grab the suggestion
    GoogleSuggest( expression ).read()
    GoogleSuggest().read( expression )
    Instance.read()
    Instance.suggest
    Instance.read( expression )

    # The method read( expression = None )
    # sets the list with the suggestion(s) and
    # returns the list with the suggestion(s)
"""

# public symbols
__all__ 		= ["url", "tag", "attribute", "q", "suggest", "read"]

__version__     = "1.0.0"


import sys
from xml.dom.minidom import parseString


# @Class GoogleSuggestException(Exception)
class GoogleSuggestException(Exception):
    """ Handling GoogleSuggest exception(s) """
    pass
# @End of: GoogleSuggestException(Exception)


# @Class GoogleSuggest(object)
class GoogleSuggest(object):
    """ Class GoogleSuggest - Google suggestion grabber """
    def __init__( self, word = None, tag = "suggestion", attr = "data" ):
        self.url        = "http://google.com/complete/search?output=toolbar&q="
        self.tag        = tag
        self.attribute  = attr
        self.q          = word
        self.suggest    = []


    # Destructor
    def __del__( self ):
        """ Destroy (Liberate) the used memory """
        self.suggest = None

        
    # Filling the list of the suggestion(s)
    def __fill( self, data = None ):
        """ Fill the suggestion(s) """
        if not data:
            return

        try:
            self.suggest = []
            doc = parseString( data )
            nodes = doc.getElementsByTagName( self.tag )
        
            for node in nodes:
                tmp = node.getAttribute( self.attribute )
                self.suggest.append( tmp )
        except Exception as ex:
            raise GoogleSuggestException( ex )


    # Unsolved ...
    def __filter( self, text ):
        """ Filtering the bad character(s) from the query string """
        return text


    #Reading the Google suggestion(s)
    def read( self, word = None ):
        """ Read the suggestion(s) """
        query = None
        if word:
            query = word
        else:
            query = self.q
        if not query:
            return

        try:
            from urllib2 import urlopen
            data = urlopen( self.url + self.__filter( query.replace(" ", "+") ) ).read()
            self.__fill( data )
            return self.suggest
        except Exception as ex:
            raise GoogleSuggestException( ex )
# @End of: GoogleSuggest(object)
