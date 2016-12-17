#!/usr/bin/python
# -*- coding: utf-8 -*-
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string
print (mutate_string('holax',2,'h'))
