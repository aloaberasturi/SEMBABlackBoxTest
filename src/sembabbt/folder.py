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

import shutil
import pathlib
import abc
from datafile import Dat, Nfde, Conf, Cmsh
from launcher import Launcher


class IFolder:
    __metaclass__ = abc.ABCMeta    
 
    @abc.abstractmethod
    def __init__(self, json_path):
        json_path = pathlib.Path(json_path)
        self._formats = []
        self._project_name = json_path.parent.name
        self._files = [
            Dat (json_path),
            Nfde(json_path),
            Conf(json_path),
            Cmsh(json_path)
        ]
        for file in self._files:
            self._formats.append(file._format)

    @abc.abstractproperty
    def files(self):
        return self._files
    @abc.abstractstaticmethod
    def cp(orgn, dstn):
        shutil.copy(str(orgn), str(dstn))

    @abc.abstractstaticmethod
    def mkdir(folder):
        folder.mkdir(parents = True, exist_ok = True)

    @abc.abstractstaticmethod
    def rmrdir(folder):
        try:
            if folder.exists:
                shutil.rmtree(str(folder))
        except FileNotFoundError:
            return
        pass


class CaseFolder(IFolder):

    def __init__(self, json_path):
        super().__init__(json_path)
        self._case_folder = json_path.parent

    @property
    def files(self):
        pass

    @property
    def case_folder(self):
        return self._case_folder

    @staticmethod
    def cp(orgn, dstn):
        super().cp(orgn, dstn)

    @staticmethod
    def mkdir(folder):
        super().mkdir(folder)
    
    @staticmethod
    def rmrdir(folder):
        super().mkdir(folder)


class TestFolder(IFolder):

    def __init__(self, json_path):
        super().__init__(json_path)
        self._test_folder    = json_path.parent  / "Test"
        self._ugrfdtd_folder = self._test_folder / "ugrfdtd"
        TestFolder.mkdir(self._ugrfdtd_folder)

    @property
    def files(self):
        pass

    @property
    def test_folder(self):
        return self.test_folder

    @staticmethod
    def cp(orgn, dstn):
        super().cp(orgn, dstn)

    @staticmethod
    def mkdir(folder):
        super().mkdir(folder)
    
    @staticmethod
    def rmrdir(folder):
        super().mkdir(folder)
