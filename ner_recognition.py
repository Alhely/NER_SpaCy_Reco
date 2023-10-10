#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:42:27 2023

@author: alhely
"""

import sys 
import spacy
import json 

#importa el modelo
NER = spacy.load('es_core_news_sm')

def ner_recognition(oraciones):
    ##convierte el string a un diccionario para accesar a la lista de oraciones
    loaded_stings = json.loads(oraciones)['oraciones'] 
    lst = [] # esta lista contendrá los resultados de cada oracion
    result_json = {"resultado":lst} # el resultado final es un diccionario
    
    for oracion in loaded_stings:  # loop para cada oracion
        d ={} # crea un diccionario por oracion
        d['oracion'] = oracion 
        NER_conversion = NER(oracion) # extrae los NER de cada oracion
        d_ent = {}
        for word in NER_conversion.ents:  
            d_ent[word.text] = word.label_## crea el contenido de la llave "entidades"
        d['entidades'] = d_ent
        lst.append(d) # incluye todo en la lista final
#    print((result_json)) 
    return result_json # el resultado es un diccionario


if __name__ == "__main__":
    ner_recognition(sys.argv[1])
