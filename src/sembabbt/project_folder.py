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

from sembabbt.datafile import Dat, Nfde
from sembabbt.state    import State
import shutil
import pathlib
import abc


class ProjectFolder:

    def __init__(self, json_path):
        self._json_path = pathlib.Path(json_path.name)
        self._project_name = self._json_path.parent.name.split(".")[0]
        self._main_f  = {
            "case" : self._json_path.parent,
            "test" : self._json_path.parent  / "Temp"
        }
        self._ugrfdtd_f = {
            "case" : self._main_f["case"] / "ugrfdtd",
            "test" : self._main_f["test"] / "ugrfdtd"
        }
        self._files = {
            "Dat"  : Dat (self),
            "Nfde" : Nfde(self),
        }
        if self._files["Nfde"]._case_path:
            self._can_call_ugrfdtd = True
        else:
            self._can_call_ugrfdtd = False
        self._main_f["test"].mkdir(parents = True, exist_ok = True)
        self._ugrfdtd_f["test"].mkdir(parents = True, exist_ok = True)
        self.copy_executables()
        self.copy_datafiles()

    def copy_executables(self):

        """Copies of semba and ugrfdtd executables"""

        shutil.copy(State.semba_path,   self._main_f["test"] / "semba")
        shutil.copy(State.ugrfdtd_path, self._ugrfdtd_f["test"] / "ugrfdtd")
        
        """Copies of .gen executables"""

        try: 
            genfile = [  
                item for item in self._main_f["case"].glob("./**/*.gen")
            ][0]
            shutil.copy(genfile, self._main_f["test"]    / genfile.name)
            shutil.copy(genfile, self._ugrfdtd_f["test"] / genfile.name)
        except IndexError:
            pass  
        except FileNotFoundError:
            pass
                        
    def copy_datafiles(self): 
        for k in ["Dat", "Nfde"]: 
            try:
                ProjectFolder.cp(
                    self._files[k]._case_path.as_posix(),
                    self._files[k]._test_path.as_posix()
                )
            except AttributeError: "No existing datafiles to copy"
       