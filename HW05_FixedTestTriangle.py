# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@Editor: Edward Holcomb
"""

import unittest

from FixedTriangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    ##Test if Triangle:
    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(4,1,3),'NotATriangle','4,1,3 is not a Triangle')

    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(1,6,5),'NotATriangle','1,5,6 is not a Triangle')
    
    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(1,3,5), 'NotATriangle','1,3,5 is not a Triangle')

    def testNotATriangleD(self):
        self.assertEqual(classifyTriangle(1,4,5), 'NotATriangle','1,4,5 is not a Triangle')
        
    def testNotATriangleE(self):
        self.assertEqual(classifyTriangle(1,0,1), 'InvalidInput','1,0,1 is not a Triangle')
        
    ##Test if Valid or Not
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(250,300,350),'InvalidInput','250,300,350 should be invalid')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(-10,-1,-10),'InvalidInput','-10,-1,-10 should be invalid')

    ##Test Right Triangle Case
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(5,4,3),'Right','5,4,3 is a Right triangle')

    def testRightTriangleD(self): 
        self.assertEqual(classifyTriangle(4,5,3),'Right','5,3,4 is a Right triangle')

    ##Test Equilateral Triangle Case
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 should be equilateral')

    def testEquilateralTrianglesC(self): 
        self.assertEqual(classifyTriangle(10,10,10),'Equilateral','10,10,10 should be equilateral')

    ##Test Isoceles Triangle Case
    def testIsocelesTrianglesA(self): 
        self.assertEqual(classifyTriangle(2,1,2),'Isoceles','2,1,2 should be isoceles')
        
    def testIsocelesTrianglesB(self): 
        self.assertEqual(classifyTriangle(1,2,2),'Isoceles','1,2,2 should be isoceles')
        
    def testIsocelesTrianglesC(self): 
        self.assertEqual(classifyTriangle(2,2,1),'Isoceles','2,2,1 should be isoceles')
    
    ##Test Scalene Triangle Case
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(10,11,12), 'Scalene', '10,11,12 should be scalene')
        
    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(15,10,13), 'Scalene', '15,10,13 should be scalene')
        
    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(55,45,40), 'Scalene', '11,7,6 should be scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

