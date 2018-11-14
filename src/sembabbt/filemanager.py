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
import fileinput
import sys
class FileManager:
    def __init__(self, path, projectName = 'none'):
        self.mainFolder = pathlib.Path(path)
        self.projectFolder = self.mainFolder / projectName
        self.ugrfdtdFolder = self.projectFolder / "ugrfdtd"

    def makeFolders(self):
        self.projectFolder.mkdir(parents=True, exist_ok = True)

    def removeFolders(self):
        try:
            if self.mainFolder.exists:
                shutil.rmtree(str(self.mainFolder))
        except FileNotFoundError: 
            return
                       
    @staticmethod
    def copyFiles(orgn,dstn):
        shutil.copy(str(orgn), str(dstn))
    
    # @staticmethod
    # def modifyTextFile(file, extension):
    #     for line in fileinput.input(str(file), inplace = 1):
    #         if extension in line:
    #             newLine = file.parent / line
    #             line = line.replace(line, str(newLine))
    #         sys.stdout.write(line)

    #     return
                                      

