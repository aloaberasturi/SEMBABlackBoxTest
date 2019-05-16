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
import shutil

class FM:
    def __init__(self, path, project_name = 'none'):
        self.main_folder = pathlib.Path(path)
        self.project_folder = self.main_folder / project_name
        self.ugrfdtd_folder = self.project_folder / "ugrfdtd"

    def make_folders(self):
        self.project_folder.mkdir(parents = True, exist_ok = True)
        self.ugrfdtd_folder.mkdir(parents = True, exist_ok = True)

    def remove_folders(self):
        try:
            if self.main_folder.exists:
                shutil.rmtree(str(self.main_folder))
        except FileNotFoundError: 
            return
                       
    @staticmethod
    def copy_files(orgn,dstn):
        shutil.copy(str(orgn), str(dstn))
    