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

from abc import ABC, abstractmethod, abstractproperty
import glob



def search_files(f, fmt):
    files = []
    for datafile in f._path.glob("*" + fmt):
        files.append(datafile)
    return files


class Folder:

    def __init__(self, path):
        self._path = path
        self._subfolders = {}
        self.update_files()        
        self._path.mkdir(parents = True, exist_ok = True)

    def update_files(self):
        self._files = {}
        self._files.update(
            {
                "Dat" : search_files(self, ".dat"),
                "Nfde": search_files(self, ".nfde")
            }
        )

    def add_subfolders(self, **kwargs):
        for (k,v) in kwargs.items():
            self._subfolders.update( {k : v} )
        
    

