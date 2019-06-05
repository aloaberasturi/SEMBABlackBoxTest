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

from sembabbt.datafile import Dat, Nfde, Conf, Cmsh
import shutil
import pathlib
import abc


class IFolder:
    __metaclass__ = abc.ABCMeta    
 
    @abc.abstractmethod
    def __init__(self, json_path):
        json_path = pathlib.Path(json_path)
        self._root_f  = None
        self._project_name = json_path.parent.name
        self._project_f = self._root_f / self._project_name
        self._files   = []
        self._formats = []
        self.files(json_path)
        self.formats()

    @abc.abstractmethod
    def files(self, json_path):
        try:
            self._files = {
                "Dat"  : self._project_f / Dat (json_path),
                "Nfde" : self._project_f / Nfde(json_path),
                "Conf" : self._project_f / Conf(json_path),
                "Cmsh" : self._project_f / Cmsh(json_path)
            }
        except TypeError:
            pass

    @abc.abstractmethod
    def formats(self):
        for file in self._files:
            self._formats.append(file._format)

    @abc.abstractproperty
    def root(self):
        return self._root_f

    @abc.abstractstaticmethod
    def cp(orgn, dstn):
        shutil.copy(str(orgn), str(dstn))



class CaseFolder(IFolder):

    def __init__(self, json_path):
        super().__init__(json_path)
        self._root_f = json_path.parent 

    def files(self, json_path):
        pass

    def formats(self):
        pass
    
    @property
    def root(self):
        pass

    @staticmethod
    def cp(orgn, dstn):
        super().cp(orgn, dstn)
    


class TestFolder(IFolder):

    def __init__(self, json_path):
        super().__init__(json_path)
        self._root_f    = json_path.parent  / "Temp"
        self._ugrfdtd_folder = self._root_f / "ugrfdtd"
        TestFolder.mkdir(self._ugrfdtd_folder)

    def files(self, json_path):
        pass

    def formats(self):
        pass

    @property
    def root(self):
        pass
        
    @staticmethod
    def cp(orgn, dstn):
        super().cp(orgn, dstn)

    @staticmethod
    def mkdir(folder):
        folder.mkdir(parents = True, exist_ok = True)

    @staticmethod
    def rmrdir(folder):
        try:
            if folder.exists:
                shutil.rmtree(str(folder))
        except FileNotFoundError:
            return
        pass
