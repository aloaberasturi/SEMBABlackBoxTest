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
import pathlib
import json

class Test():
    def __init__(self, **kwargs): 
        self._exec_info  = ExecInfo(
            kwargs["input_path"],
            kwargs["output_path"],
            kwargs["exec_mode"]
        )
        self._filters = Filters(
            kwargs["size"],
            kwargs["comp_mode"],
            kwargs["keywords"]

        )
        self._matching_cases = []
        self._folders         = []

    def append_case(self, path):
        self._matching_cases = path
        self._folders.append(TestFolder(path))
        self._folders[-1].__call__()
        self.copy_executables()
        self.copy_datafiles()

    def can_call_ugrfdtd(self): 
        if self._folders[-1]._files["Nfde"]._path:
            return True
        else:
            return False

    def copy_executables(self):

        """Copies of semba and ugrfdtd executables"""

        shutil.copy(State.semba_path,    self._folders[-1]._root_f / "semba")
        shutil.copy(State.ugrfdtd_path,  self._folders[-1]._ugrfdtd_f / "ugrfdtd")
        
        """Copies of .gen executables"""

        try: 
            genfile = [
                item for item in self._folders[-1]._case_f.glob("./**/*.gen")
            ][0]
            shutil.copy(genfile, self._folders[-1]._root_f    / genfile.name)
            shutil.copy(genfile, self._folders[-1]._ugrfdtd_f / genfile.name)
        except IndexError:
            pass  
        except FileNotFoundError:
            pass
                        
    def copy_datafiles(self):
        for k in self._folders[-1]._case_f._files.keys(): #this doesn't work now
            try:
                TestFolder.cp(
                    self.case._folder._files[k]._path.as_posix(), 
                    self._folder._files[k]._path.as_posix()
                )
            except AttributeError: "No existing datafiles to copy"
    
                   

    

