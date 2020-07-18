#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:03:55 2020

@author: mario
"""

# muestra los cuadrados de los numeros del 0 al 5 

def squared(x):
    return x**2

for ii in range(6):
    print(ii,squared(ii))

print("Hecho")    