# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:00:51 2024

@author: Sven
"""
import logging
debug = logging.basicConfig(level=logging.INFO)
class Dog:

    def __init__(self, name):
        logging.debug('initialised') 
        '''
        

        Parameters
        ----------
        name : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.name = name
        self.tricks = []    # creates a new empty list for each dog
        
        '''
        https://docs.python.org/3/tutorial/classes.html
        “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.

        Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called name mangling. Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.
        '''
        self._pfoten = 4
        self.__farbe =''

    def add_trick(self, trick):
        self.tricks.append(trick)
        logging.info('neuer Trick gelernt') 

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)