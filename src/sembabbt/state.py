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
    
    def __new__(cls, exec_paths, test):
        cls._count += 1
        cls._tests.append(test)
        cls._semba_path   = exec_paths["semba_path"]
        cls._ugrfdtd_path = exec_paths["ugrfdtd_path"]
        cls.display()

    @classmethod
    def display(cls):
        print("Current number of running _tests: ", cls._count)
        for item in cls._tests:
            filters   = item.filters
            exec_info = item.exec_info
            print (cls._tests.index(item) + 1,"-th test")
            print ("TESTING CASES IN:", exec_info.input_path)
            print ("OUTPUT FOLDER :"  , exec_info.output_path)
            print ("EXECUTION MODE: " , exec_info.exec_mode) 
            print ("COMPARISON MODE: ", filters.comp_mode)
            if item.filters.keywords:
                print ("Test launched with the following keywords:")
                for k in item.filters.keywords:
                    print(k)
            else:
                print("No keywords were specified for this test")

    @classmethod
    def write(cls): 
        for item in cls._tests:
            with open(
                pathlib.Path(item.exec_info.output_path) / "sembabbt.log", "w"
            ) as file:
                filters   = item.filters
                exec_info = item.exec_info
                file.write("EXECUTION MODE: " + str(exec_info.exec_mode) + "\n")
                file.write("COMPARISON MODE: " +str(filters.comp_mode) + "\n")
                if filters.keywords:
                    file.write("Test launched with the following keywords:"+"\n")
                    for k in filters.keywords:
                        file.write(str(k) + "\n")  
                else:
                    file.write("No keywords were specified for this test" + "\n")  
            file.close()        