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
    
    def __new__(cls, test):
        cls._count += 1
        cls._tests.append(test)        
        cls.write()

    @classmethod
    def write(cls): 
        file = cls._tests[-1]._logfile
        filters   = cls._tests[-1]._filters
        exec_info = cls._tests[-1]._exec_info
        file.write("EXECUTION MODE: " + str(exec_info._exec_mode) + "\n")
        file.write("COMPARISON MODE: "+ str(filters._comp_mode)   + "\n")
        if filters._keywords:
            file.write("Test launched with the following keywords:"+"\n")
            for k in filters._keywords:
                file.write(str(k) + "\n")  
        else:
            file.write("No keywords were specified for this test" + "\n")  
    
