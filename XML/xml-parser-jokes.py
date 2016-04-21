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
import sys #modulo que da accesi a variables que interactuan con el interprete
import string

def normalize_whitespace(text):
    "Remove redundant whitespace from a string"
    return string.join(string.split(text), ' ')

class CounterHandler(ContentHandler): #hereda del manejador generico

    def __init__ (self):
        self.inContent = 0     #si estoy dentro del contenido que me interesa
        self.theContent = ""   #maneja el contenido que me interesa

    def startElement (self, name, attrs): #Se activa cuando empiezo a reconocer un elemento XML
        #recibe la notificacion del comienzo del documento
        #name contiene el nombre del tipo de elemento en el XML en est caso joke
        #attrs tiene una instancia de AttributesNS
        #Se invoca cuando el parser SAX encuentra el elemento de apertura del documento
        if name == 'joke':
            self.title = normalize_whitespace(attrs.get('title'))
            print " title: " + self.title+ "." #escribe en pantalla el atributo tittle
        elif name == 'start':
            self.inContent = 1 #estoy en contenido
        elif name == 'end':
            self.inContent = 1  #esto en contenido
        elif name == 'intermedia' :
            self.inContent = 1 

    def endElement (self, name): #cuando acabe de leer el final de un elmento
    #recibe notificacion del final de documento . Es el ultimo metodo en invocarse
    #se invoca cuando se encuentra la etiqueta de cierre
        if self.inContent:
            self.theContent = normalize_whitespace(self.theContent)
        if name == 'joke':
            print "" #linea en blanco
        elif name == 'start':
            print "  start: " + self.theContent + "."
        elif name == "intermedia" :
            print " linea intermedia :" + self.theContent
        elif name == 'end':
            print "  end: " + self.theContent + "."
        if self.inContent:
            self.inContent = 0
            self.theContent = ""

    def characters (self, chars): #cuando acabe de leer los caracteres de un elemento le lo que hay entre las etiquetas de start y end
        if self.inContent:
            self.theContent = self.theContent + chars  #lo aniado al contenido

# --- Main prog



#if len(sys.argv)<2:
#    print "Usage: python xml-parser-jokes.py jokes.xml"
#    print sys.argv[0]
#    print " jokes.xml: file name of the document to parse"
#    sys.exit(0)

# Load parser and driver

JokeParser = make_parser() #objeto analizador sintactico . Esta funcion nos devuelve un objeto parser
#que se utiliza para analizar sinctactimanete el fichero XML
JokeHandler = CounterHandler()
JokeParser.setContentHandler(JokeHandler) #manejador de contenidos generico que se pasa
#a la funcion ContentHandler

# Ready, set, go!

xmlFile = open(sys.argv[0],"r")
JokeParser.parse("jokes.xml")


print "Parse complete"
