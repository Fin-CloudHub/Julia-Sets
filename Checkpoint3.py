#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:29:09 2024

@author: finlay sime

s2212677

"""

import matplotlib.pyplot as plt
import numpy as np

class Grid(object):
    """
    Creates a 2DGrid to be plotted by another class
    
    """
    
    def __init__(self, n, m):
        """
        Constructor magic method
        
        """
        self.grid = np.zeros((n, m))#Creates a array of zeros
        
    def __str__(self):
        """"
        Prints the 2D grid in the correct format
        
        """
        s = ""
        for i in range(len(self.grid)): #Creates loop that prints the grid as an 
                                        # easy to read
           for j in range(len(self.grid[i])): #grid
               s += str(self.grid[j][i]) + "\t"
           s += "\n"
        return s
    
    def checkZ(self, n, m, N):
        """
        Check's if the complex number C is in the mandelbrot set or not and
        modify object's grid to store which ones are.
        

        """
        
        c_real = np.linspace(-2.025, 0.6, n) #creates a linspace of the real parts of c
        c_imag = np.linspace(-1.125, 1.125, m) #creates a linspace of the imaginary 
                                                # parts of c
        
        for i in range(n):
             for j in range(m):
                 c = c_real[i] + 1j * c_imag[j] #creates complex number c
                 z = 0
                 iteration = 0
                 while abs(z) < 2 and iteration < N:
                     z = z**2 + c #checks that c is in the mandelbrot set
                     iteration += 1

                 self.grid[j][i] = iteration  #marks whether or not that point is in
                                             # in mandlebrot set
        
        
class PlotGraph(object):
    """
    Plots a graph to display the mandlebrot set
    
    """
    
    @classmethod
    def plot(cls, array):
        """
        Class method to plot the above class and display it in colour

        """
        
        plt.imshow(array.grid, extent=(-2.025, 0.6, -1.125, 1.125), cmap='plasma')
        plt.show() #Shows the grid as a colour plot and extends it if goes beyond values

        
    

def main():
   """
   Main Function to test above classes
        
   """
        
   n = 512
   m = 512
   N = 255
   test = Grid(n, m)
   test.checkZ(n, m, N)
   PlotGraph.plot(test)
        
main()