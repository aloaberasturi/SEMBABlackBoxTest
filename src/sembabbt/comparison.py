#! /usr/bin/env python3
import sys
from termcolor import colored,cprint

def IsEqual(a,b):
    try:
        assert a == b
        return True
    except AssertionError: 
        print(
            sys.modules[__name__],
            ": error: Expected: ",
            a,
            " \nto be equal to:",
            b,"\nActual: False")
        return False 
      


def IsAlmostEqual(a,b,relTolerance,absTolerance):
    try:

        assert (100*abs(a-b)/a) <= relTolerance
        return True

    except AssertionError:
        print(
            sys.modules[__name__],
            ": error: Expected: ",
            a,
            " \nto be almost equal to:",
            b,
            "\nActual: False")
        return False

    except ZeroDivisionError:     
        if b != 0.0:
            try:

                assert (abs(b) <= absTolerance)
                return True

            except AssertionError:
                print(
                    sys.modules[__name__],
                    ": error: Expected: ",
                    a,
                    " \nto be almost equal to:",
                    b,
                    "\nActual: False")
                return False
        else: 
            return True