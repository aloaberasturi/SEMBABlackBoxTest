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

from caseobject import Case
from exe_calls import call_semba, call_ugrfdtd
class Launcher: #this can be a function instead of a class
    def __new__(cls, test):
        cls.search(test)
        cls.launch(test)
        cls.output(test)
    
    @classmethod
    def search(cls, test): 
        for path in test.launcher_info.in_path():
            with path("r") as json_file:
                case = Case(json_file)
            if (
                    
                set(case.filters.keywords) &  set(test.filters.keywords)
                                          != 
                                          set() 
                                          and 
                case.filters.size <= test.filters.size
            ):
                test(json_file, case)
            else : 
                pass

    @classmethod
    def launch(cls, test):
        if test.matching_cases:
            for case in test.matching_cases:
                if case.can_call_ugrfdtd:
                    call_ugrfdtd(test)
                else:
                    call_semba(test)
                    call_ugrfdtd(test)
                        
    @classmethod
    def output(cls, test):
        pass
