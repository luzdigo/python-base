#!/usr/bin/env python

"""Imprime Hello, World em multi línguas

Como usar:

Tenha a linguagem devidamente configurada, ex:
    
    export LANG=pt_BR

Execução:

    Python Hello.py
"""

__author__ = "Rodrigo"
__version__ = "0.0.1"



import os

langs = os.getenv ("LANG", "en_US") [:5]
msg = "Hello, World"

if langs == "en_US":
    print ("Hello, World")
elif langs == "pt_BR":
    print ("Olá, mundo")