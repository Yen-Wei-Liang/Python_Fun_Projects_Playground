#===============================================================
# Lab     : Kdd 721
# Name    : Yen-Wei-Liang
# function: Unit tests for a time complexity experience program
#===============================================================

import unittest
import Time_Complexity_Experience
from Time_Complexity_Experience import Time_Complexity_Experience

class Time_Complexity_Experience_Test(unittest.TestCase):

    def test_funtion1(self):
        result_1 = Time_Complexity_Experience().Time_Complexity(314159265358979)
        self.assertEqual(-157079632679488, result_1)

    def test_funtion2(self):        
        result_2 = Time_Complexity_Experience().Time_Complexity(10)
        self.assertEqual(7, result_2)

    def test_funtion3(self):        
        result_3 = Time_Complexity_Experience().Time_Complexity(20)
        self.assertEqual(12, result_3)

    def test_funtion4(self):        
        result_4 = Time_Complexity_Experience().Time_Complexity(15)
        self.assertEqual(-6, result_4)

    def test_funtion5(self):        
        result_5 = Time_Complexity_Experience().Time_Complexity(7110064013)
        self.assertEqual(-3555032005, result_5)