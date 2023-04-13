#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size=0):
        self.brand = brand
        self._size = size
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        
    def get_size(self):
        return self._size
    
    def set_size(self, number):
        if type(number) == int:
            self._size = number
      
        print("size must be an integer")
        
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
        
    size = property(get_size, set_size)