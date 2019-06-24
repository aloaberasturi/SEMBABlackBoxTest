#! /usr/bin/env python3
# OpenSEMBA
# Copyright (C) 2015 Salvador Gonzalez Garcia                    (salva@ugr.es)
#                    Luis Manuel Diaz Angulo          (lmdiazangulo@semba.guru)
#                    Miguel David Ruiz-Cabello Nuñez        (miguel@semba.guru)
#                    Alejandra Lopez de Aberasturi Gomez (aloaberasturi@ugr.es)
#                    
# This file is part of OpenSEMBA.
#
# OpenSEMBA is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# OpenSEMBA is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with OpenSEMBA. If not, see <http://www.gnu.org/licenses/>.

import sys

def compare(test):

    def is_equal(a,b):
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
        except ValueError:
            pass
        return False 

    for i in range (len(test._folder._files["Dat"]._test_path) - 1):
        with open(test._folder._files["Dat"]._test_path[i+1], "r") as testfile:
            with open(test._folder._files["Dat"]._case_path[i+1], "r") as casefile: #make this easier to read
                a = casefile.readline()
                b = testfile.readline()
                while (a,b):
                    is_equal(a,b) 
                    a = casefile.readline()
                    b = testfile.readline()