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
from sembabbt.folder    import Folder
from sembabbt.filters   import Filters
import shutil


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
        self._folder = None
        self._can_call_ugrfdtd = False
    
       
    def new_folder(self, path):
        self._folder = Folder(path)
        case_ugr = Folder(self._folder._path / "ugrfdtd")
        if case_ugr._files["Nfde"]:
            self._can_call_ugrfdtd = True
        temp_f   = Folder(self._folder._path / "Temp")
        temp_ugr = Folder(temp_f._path / "ugrfdtd")
        temp_f.add_subfolders(ugrfdtd = temp_ugr)
        self._folder.add_subfolders(ugrfdtd = case_ugr, Temp = temp_f)
        self.copy_executables()
        Test.copy_data(self._folder, temp_f, "Dat")
        Test.copy_data(case_ugr, temp_ugr, "Nfde")


    def copy_executables(self):

        """Copies of semba and ugrfdtd executables"""

        shutil.copy(
            self._exec_info._semba_path,
            self._folder._subfolders["Temp"]._path / "semba"
        )
        shutil.copy(
            self._exec_info._ugrfdtd_path, 
            self._folder._subfolders["Temp"]._subfolders["ugrfdtd"]._path / "ugrfdtd"
        )
        
        """Copies of .gen executables"""

        try: 
            genfile = [  
                item for item in self._folder._path.glob("./**/*.gen")
            ][0]
            shutil.copy(genfile, self._folder._subfolders["Temp"]._path / genfile.name)
            shutil.copy(
                genfile, 
                self._folder._subfolders["Temp"]._subfolders["ugrfdtd"]._path / genfile.name
            )
        except IndexError:
            pass  
        except FileNotFoundError:
            pass
                
     
    @staticmethod
    def copy_data(f_orgn, f_dstn, fmt):
        for i in f_orgn._files[fmt]:
            shutil.copy(i, f_dstn._path / i.name)
        
                    


                   

    
