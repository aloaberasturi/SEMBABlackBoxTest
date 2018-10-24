#! /usr/bin/env python

import unittest

class EqualityTest(unittest.TestCase):
    def test(self,a,b):
        self.assertEqual(a,b)

class AlmostEqualityTest(unittest.TestCase):
    def test(self,a,b,tolerance):
        self.assertAlmostEqual(a,b,delta = tolerance)
