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

import pathlib

class State: 
    _count = 0
    _tests = []

    def __new__(cls, *args):
        if args:
            cls._count += 1
            cls._tests.append(*args)

    @classmethod
    def display(cls):
        print("Current number of running _tests: ", cls._count)
        for item in cls._tests:
            print (cls._tests.index(item) + 1,"-th test")
            print ("EXECUTION MODE: ", item._exec_mode)
            print ("COMPARISON MODE: ", item._comp_mode)
            if item._filters:
                print ("Test launched under the following filters:")
                for f in item._filters:
                    print(f)
            else:
                print("No filters were specified for this test")

    @classmethod
    def write(cls): 
        for item in cls._tests:
            with open(pathlib.Path(item._output_path) / "sembabbt.log", "w") as file:
                file.write("EXECUTION MODE: " + str(item._exec_mode) + "\n")
                file.write("COMPARISON MODE: " +str(item._comp_mode) + "\n")
                if item._filters:
                    file.write("Test launched under the following filters:" + "\n")
                    for f in item._filters:
                        file.write(str(f) + "\n")  
                else:
                    file.write("No filters were specified for this test" + "\n")  
            file.close()        