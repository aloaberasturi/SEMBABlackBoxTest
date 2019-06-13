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
import shutil
import pathlib
import abc


class IFolder:
    __metaclass__ = abc.ABCMeta    
 
    @abc.abstractmethod
    def __init__(self, json_path):
        self.json_path = pathlib.Path(json_path.name)
        self.root_f()
        self._ugrfdtd_f = self._root_f / "ugrfdtd"
        self.project_name()
        self._files   = {}
        self._formats = []

    
    @abc.abstractmethod
    def __call__(self):
        self._files = {
            "Dat"  : Dat (self),
            "Nfde" : Nfde(self),
        }
  
    @abc.abstractmethod
    def root_f(self):
        pass
    
    @abc.abstractproperty
    def project_name(self):
        pass

    

class CaseFolder(IFolder):

    def __init__(self, json_path):
        super().__init__(json_path)
        self.__call__()

    def __call__(self):
        super().__call__()
    
    def root_f(self):
        self._root_f = self.json_path.parent

    def project_name(self):
        self._project_name = (self._root_f.name).split(".")[0]


class TestFolder(IFolder):

    def __init__(self, json_path):
        super().__init__(json_path)
        TestFolder.mkdir(self._root_f)
        TestFolder.mkdir(self._ugrfdtd_f)
    
    def __call__(self):
        super().__call__()

    def root_f(self):
        self._root_f = self.json_path.parent  / "Temp"
         
    def project_name(self):
        self._project_name = (self._root_f.parent.name).split(".")[0]

    @staticmethod
    def cp(orgn, dstn):
        shutil.copy(str(orgn), str(dstn))
    
    @staticmethod
    def cptree(orgn, dstn):
        shutil.copytree(str(orgn), str(dstn))

    @staticmethod
    def mkdir(folder):
        folder.mkdir(parents = True, exist_ok = True)

    @staticmethod
    def rmrdir(folder):
        try:
            if folder.exists:
                shutil.rmtree(str(folder))
        except FileExistsError: 
            "Oops! Something went wrong while removing temporary folders"
