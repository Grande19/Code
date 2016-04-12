#!/usr/bin/python

#
# Simple XML parser for JokesXML
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# September 2009
#
# Just prints the jokes in a JokesXML file

from xml.sax.handler import ContentHandler #manejador de contenido
from xml.sax import make_parser
import sys
import string

def normalize_whitespace(text):
    "Remove redundant whitespace from a string"
    return string.join(string.split(text), ' ')

class CounterHandler(ContentHandler): #hereda del manejador generico

    def __init__ (self):
        self.inContent = 0     #si estoy dentro del contenido que me interesa
        self.theContent = ""   #maneja el contenido que me interesa

    def startElement (self, name, attrs): #Se activa cuando empiezo a reconocer un elemento XML
        if name == 'joke':
            self.title = normalize_whitespace(attrs.get('title'))
            print " title: " + self.title + "." #escribe en pantalla el atributo tittle
        elif name == 'start':
            self.inContent = 1 #estoy en contenido
        elif name == 'end':
            self.inContent = 1  #esto en contenido

    def endElement (self, name): #cuando acabe de leer el final de un elmento
        if self.inContent:
            self.theContent = normalize_whitespace(self.theContent)
        if name == 'joke':
            print "" #linea en blanco
        elif name == 'start':
            print "  start: " + self.theContent + "."
        elif name == 'end':
            print "  end: " + self.theContent + "."
        if self.inContent:
            self.inContent = 0
            self.theContent = ""

    def characters (self, chars): #cuando acabe de leer los caracteres de un elemento
        if self.inContent:
            self.theContent = self.theContent + chars #lo aniado al contenido

# --- Main prog

if len(sys.argv)<2:
    print "Usage: python xml-parser-jokes.py <document>"
    print
    print " <document>: file name of the document to parse"
    sys.exit(1)

# Load parser and driver

JokeParser = make_parser()
JokeHandler = CounterHandler()
JokeParser.setContentHandler(JokeHandler)

# Ready, set, go!

xmlFile = open(sys.argv[1],"r")
JokeParser.parse(xmlFile)

print "Parse complete"
