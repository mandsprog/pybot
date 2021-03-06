#!/usr/bin/env python
"""
 hellp.py       Be polite.
 Author:        Rael Garcia <self@rael.io>
 Date:          06/2016
 Tested on:     Python 3 / OS X 10.11.5
"""
import re
import random

greetings = ['Buenos días', 'Bon dia', 'Good Morning',
                'Egun on', 'Morning', 'Buon giorno',
                'Bonjour', 'Bos días', 'Buenos días arsa',
                'Hola miarma', 'Goede morgen', 'Bom dia',
                'Días buenos a ti también'] 

nights = ['Buenas noches', 'Bona nit', 'Good night',
              'Nanit', 'Gute natch', 'Buonna note',
              'Bonne nuit','Goedenacht', 'Boa noite']

def hear(words):

    if any(greeting.lower() in words.lower() for greeting in greetings):
        return random.choice(greetings)

    if any(night.lower() in words.lower() for night in nights):
        return random.choice(nights)
