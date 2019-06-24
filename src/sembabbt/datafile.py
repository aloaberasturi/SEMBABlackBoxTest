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
class IFile(ABC):

    @abstractproperty
    def format(self):
        ...
    @abstractproperty
    def folder(self):
        ...
    def initial_data_file(self):
        return self._folder._project_name + self.format()
    

    @abstractmethod
    def __init__(self, f): 
        self._folder = f
        self._test_path = [self.folder()["test"] / self.initial_data_file()]
        self._case_path = [self.folder()["case"] / self.initial_data_file()]
class Dat(IFile):
    def __init__(self, f):
        super().__init__(f)
    
    def folder(self):
        return self._folder._main_f
    
    def format(self):
        return ".dat"

    def resulting_data_files(self): #change this
        for dat in self._folder._ugrfdtd_f["case"].glob("*.dat"):
            self._case_path.append(self._folder._ugrfdtd_f["case"] / dat.name)
            self._test_path.append(self._folder._ugrfdtd_f["test"] / dat.name)   
class Nfde(IFile):
    def __init__(self, f):
        super().__init__(f)

    def folder(self):
        return self._folder._ugrfdtd_f
    
    def format(self):
        return ".nfde"
    