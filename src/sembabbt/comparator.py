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
            a = [float(_) for _ in a.split()]
            b = [float(_) for _ in b.split()]
            for i in range(len(a)):
                assert a[i] == b[i]

        except ValueError:
            pass

        except AssertionError: 
            print(
                sys.modules[__name__],": error: Expected: ", a[i], " \nto be equal to:",
                b[i], "\nActual: False"
            )
 
    test_folder = test._folder._subfolders["Temp"]._subfolders["ugrfdtd"]
    case_folder = test._folder._subfolders["ugrfdtd"]

    for i in range(len(test_folder._files["Dat"])):
        with open(test_folder._files["Dat"][i], "r") as testfile:
            with open(case_folder._files["Dat"][i], "r") as casefile:
                a = casefile.readline()
                b = testfile.readline()
                while (a,b):
                    is_equal(a,b) 
                    a = casefile.readline()
                    b = testfile.readline()