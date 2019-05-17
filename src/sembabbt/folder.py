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
from launcher import Launcher


class Folder: 

    def __init__(self, file):
        Folder.raw_path = pathlib.Path(file)
        self._project_name = file.parent.name
        self._root_folder = Launcher.test()._input_path
        self._case_folder = self._root_folder / self._project_name 
        self._ugrfdtd_folder = self._case_folder / "ugrfdtd"
        self._nfde_file = self.Nfde()#is this ok? shouldn't it be cls.Nfde?
        self._conf_file = self.Conf()
        self._dat_file  = self.Dat()
        self._cmsh_file = self.Cmsh()
        self.mkdirs()

    def mkdirs(self):
        self._root_folder.mkdir(parents = True, exist_ok = True)
        self._ugrfdtd_folder.mkdir(parents = True, exist_ok = True)

    def rmdirs(self):
        try:
            if self._root_folder.exists:
                shutil.rmtree(str(self._root_folder))
        except FileNotFoundError:
            return

    @staticmethod
    def cp(orgn, dstn):
        shutil.copy(str(orgn), str(dstn))

    class File:
        def __init__(self):#hacer esto bien, mirando como se hereda.
            self._name = Folder.raw_path.parent.name.split("."[0] + ".dat")


    class Dat(File):
        pass
    class Nfde(File):
        pass
    class Conf(File):
        pass
    class Cmsh(File):
        pass