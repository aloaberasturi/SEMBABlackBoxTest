#! /usr/bin/env python

class EqualityTest:
    def test(self,a,b):
        assert a == b
        print ("hola")

class AlmostEqualityTes:
    def test(self,a,b,tolerance):
        assert abs(a-b)/a <= tolerance
