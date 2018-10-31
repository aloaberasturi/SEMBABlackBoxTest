#! /usr/bin/env python

def IsEqual(self,a,b):
        assert a == b

def IsAlmostEqual(self,a,b,tolerance):
        assert abs(a-b)/a <= tolerance
