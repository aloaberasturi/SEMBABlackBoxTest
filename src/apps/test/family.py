#! /usr/bin/env python

from termcolor import colored,cprint

def IsEqual(a,b):
    try:
        assert a == b
        return True
    except AssertionError: 
        print("family.py: error: Expected: ",a," \n" + "to be equal to:",b,"\n"+
        "Actual: False")
        return False
 
      


def IsAlmostEqual(a,b,tolerance):
    try:
        assert (100*abs(a-b)/a) <= tolerance
        return True
    except AssertionError:
        print("family.py: error: Expected: ",a," \n" + "to be almost equal to:"\
        ,b,"\n"+"Actual: False")
        return False
    except ZeroDivisionError:     
        if b != 0.0:
            try:
               #que hago aqui?
                assert (?? <= tolerance)
                return True
            except AssertionError:
                return False
        else: 
            return True