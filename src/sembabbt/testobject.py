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

from sembabbt.exec_info import ExecInfo
from sembabbt.folder import TestFolder
from sembabbt.filters import Filters
from sembabbt.state import State
import shutil

class Test():
    def __init__(self, **kwargs): 

        self._exec_info  = ExecInfo(
            kwargs["input_path"],
            kwargs["output_path"],
            kwargs["exec_mode"]
        )
        self._filters = Filters (
            kwargs["size"],
            kwargs["comp_mode"],
            kwargs["keywords"]

        )
        self._matching_cases = []
        self._folders        = []

    def __call__(self, path, case):
        self._folders.append(TestFolder(path))
        self.copy_datafiles(case)
        self.copy_executables(case)
        TestFolder.cp(case._folder._files, self._folders[-1]._files)
        self.matching_cases(case)


    @property
    def exec_info(self):
        return self._exec_info

    @property
    def filters(self):
        return self._filters


    def copy_executables(self, case):
        shutil.copy(State.semba_path,    self._folders[-1]._root_f / "semba")
        shutil.copy(State.ugrfdtd_path, self._folders[-1]._ugrfdtd_f / "ugrfdtd")
        
        for genfile in case._folder._root_f.glob("./**/*.gen"):
            shutil.copy(genfile, self._folders[-1]._root_f / genfile.name)
            if case.can_call_ugrfdtd:
                shutil.copy(genfile, self._folders[-1]._ugrfdtd_f / genfile.name)
                        
    def copy_datafiles(self, case):
        try:
            for k,v in case._folder._files.items():
                TestFolder.cp(
                    v._path.as_posix(), 
                    str(self._folders[-1]._root_f / v._path._name)
                )

            self._folders[-1].files()
        except:
            pass
        

    def matching_cases(self, matching_case):
        self._matching_cases.append(matching_case)

    

