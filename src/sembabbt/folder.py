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
from file_class import Dat, Nfde, Conf, Cmsh
from launcher import Launcher


class Folder:
    __metaclass__ = abc.ABCMeta    
    
    @abc.abstractproperty
    def raw_path(self, path):
        pass

    @abc.abstractproperty
    def root_folder(self):
        pass
        
    @abc.abstractproperty
    def project_name(self):
        pass

    @abc.abstractproperty
    def case_folder(self):
        pass
    
    @abc.abstractproperty
    def nfde_file(self):
        self._nfde_file = Nfde().name(self.raw_path)

    @abc.abstractproperty
    def conf_file(self):
        self._conf_file = Conf().name(self.raw_path)

    @abc.abstractproperty
    def dat_file(self):
        self._dat_file  = Dat ().name(self.raw_path)

    @abc.abstractproperty
    def cmsh_file(self):
        self._cmsh_file = Cmsh().name(self.raw_path)

    @staticmethod
    def cp(orgn, dstn):
        shutil.copy(str(orgn), str(dstn))


class Case(Folder):

    def __init__(self, path):
        self.raw_path
        self.root_folder
        self.project_name
        self.case_folder
        self.nfde_file
        self.conf_file
        self.dat_file
        self.cmsh_file

    def raw_path(self, path):
        self._raw_path = path
        return self._raw_path
    
    def root_folder(self):
        self._root_folder = Launcher._test._input_path
        return self._root_folder
    
    def project_name(self):
        self._project_name = self._raw_path.parent.name
        return self._project_name

    def case_folder(self):
        self._case_folder =  self.root_folder / self.project_name
        return self._case_folder
    
    def nfde_file(self):
        return super().nfde_file()
    
    def conf_file(self):
        return super().conf_file()

    def dat_file(self):
        return super().dat_file()
    
    def cmsh_file(self):
        return super().cmsh_file()


class Test(Case):

    def __init__(self, path):

        super().raw_path
        super().root_folder
        super().project_name
        self.test_folder
        self.ugrfdtd_folder
        super().nfde_file
        super().conf_file
        super().dat_file
        super().cmsh_file
        self.mkdirs()

    def test_folder(self):
        self._test_folder = self.root_folder / self.project_name / "Test"
        return self._test_folder

    def ugrfdtd_folder(self):
        self._ugrfdtd_folder = self.case_folder / "ugrfdtd"
        return self._ugrfdtd_folder

    def mkdirs(self):
        self.root_folder.mkdir(parents = True, exist_ok = True)
        self._ugrfdtd_folder.mkdir(parents = True, exist_ok = True)


    def rmdirs(self):
        try:
            if self._root_folder.exists:
                shutil.rmtree(str(self._root_folder))
        except FileNotFoundError:
            return
        pass

