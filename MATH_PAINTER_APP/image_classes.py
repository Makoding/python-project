import numpy as np
from PIL import Image

basic_colors = 3

class Canvas:
    """Initiates the dimensions of the canvas and its color"""
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.data = np.zeros((self.width, self.height, basic_colors), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, filename):
        """Makes the png file"""
        filename += '.png'
        img = Image.fromarray(self.data, 'RGB')
        img.save(filename)



class Square:
    """Initiates the place of the square in the canvas
     as well as its side and color
     """
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color
    
    def draw(self, canvas_object):
        """Draws the square on the canvas
         by changing some values of the array"""
        canvas_object.data[self.x:self.x+self.side, self.y:self.y+self.side] = self.color

    

class Rectangle:
    """Initiates the place of the rectangle in the canvas
         as well as its side and color
         """
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self, canvas_object):
        """Draws the rectangle on the canvas
                 by changing some values of the array"""
        canvas_object.data[self.x:self.x+self.width, self.y:self.y+self.height] = self.color

