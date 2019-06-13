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

from sembabbt.caseobject import Case
from sembabbt.folder import TestFolder
from sembabbt.callers import call_semba, call_ugrfdtd

def launch(test):
    
    def search(test): 
        for path in test.exec_info.input_path.glob("**/*.test.json"): 
            with open(path, "r") as json_file:
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

    def call_executable(test):
        try:
            for case in test._matching_cases:
                if case.can_call_ugrfdtd():
                    call_ugrfdtd(test)
                else:
                    call_semba(test)
                    call_ugrfdtd(test)

        except IndexError : "No cases matching the input test"                        


    search(test)
    call_executable(test)
    try:

        TestFolder.cptree(
            test._folder._root_f, 
            test._exec_info._output_path / test._folder._project_name)

    except FileExistsError: 
            TestFolder.rmrdir(
                test._exec_info._output_path / test._folder._project_name
            )
            TestFolder.cptree(
            test._folder._root_f, 
            test._exec_info._output_path / test._folder._project_name)
            
    TestFolder.rmrdir(test._folder._root_f)
    

