# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 11:05:32 2021

@author: course

"""
from compass import COMPASS #made by girls

class HelloWorld:
    
    def __init__(self,hello="Hello world!"):
        
        try:
            self.hello="hi "+hello
        except:
            print("This is not a string!")
        
    def show(self):
        try:
            print("%s" % self.hello)
        except:
            print("type error, string expected")
            
if __name__ == "__main__" :

    hello=HelloWorld()
    hola=HelloWorld(hello=5)
    
    CP = COMPASS(0x60)
    print("compass test")
