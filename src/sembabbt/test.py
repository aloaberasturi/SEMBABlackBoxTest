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
from sembabbt.project_folder import ProjectFolder
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
            kwargs["exec_mode"],
            kwargs["semba_path"],
            kwargs["ugrfdtd_path"]
        )
        self._filters = Filters(
            kwargs["size"],
            kwargs["comp_mode"],
            kwargs["keywords"]
        )
        self._folders = []
    
       
    def new_folder(self, path):
        self._folder = ProjectFolder(path)
        self.copy_executables()
        self.copy_datafiles()

    def copy_executables(self):

        """Copies of semba and ugrfdtd executables"""

        shutil.copy(self._exec_info._semba_path,   self._folder._main_f["test"] / "semba")
        shutil.copy(self._exec_info._ugrfdtd_path, self._folder._ugrfdtd_f["test"] / "ugrfdtd")
        
        """Copies of .gen executables"""

        try: 
            genfile = [  
                item for item in self._folder._main_f["case"].glob("./**/*.gen")
            ][0]
            shutil.copy(genfile, self._folder._main_f["test"]    / genfile.name)
            shutil.copy(genfile, self._folder._ugrfdtd_f["test"] / genfile.name)
        except IndexError:
            pass  
        except FileNotFoundError:
            pass
                
    def copy_datafiles(self): 
        for v in self._folder._files.values(): 
            try:
                shutil.copy(
                    v._case_path.as_posix(),
                    v._test_path.as_posix()
                )
            except FileNotFoundError: 
                pass
       


                   

    

