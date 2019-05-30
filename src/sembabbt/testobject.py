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

from info import Info
from folder import TestFolder
from filters import Filter
from state import State

class Test():
    def __init__(self, filters, input_path, output_path):
        self._launcher_info  = Info(input_path, output_path)
        self._filters        = filters
        self._matching_cases = []
        self._folder         = None
            
    @folder.setter
    def folder(self, json_path):
        self._folder = TestFolder(json_path)

    @matching_cases.setter 
    def matching_cases(self, matching_case):
        for data_file in matching_case.folder.files:
            if data_file:
                TestFolder.cp(
                    matching_case.folder.case_folder / data_file, 
                    self._folder.test_folder / data_file
                        )
        self._matching_cases.append(matching_case)
        State(self)

    @property
    def launcher_info(self):
        return self._launcher_info

    @property
    def filters(self):
        return self._filters

