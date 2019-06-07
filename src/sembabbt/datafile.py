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


import abc
class IFile:
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def __init__(self, folder):
        pass
    
    @abc.abstractmethod
    def path(self, folder):
        self._path = folder._root_f / (str(folder._project_name) + self._format)
        if self._path.exists():
            return self._path
        else:
            return False

class Dat(IFile):
    def __init__(self, folder):
        self._format = ".dat"
        self.path(folder)
 
    def path(self, folder):
        super().path(folder)


class Nfde(IFile):
    def __init__(self, folder):
        self._format = ".nfde"
        self.path(folder)

    def path(self, folder):
        super().path(folder)
    
class Conf(IFile):
    def __init__(self, folder):
        self._format = ".conf"
        self.path(folder)
 
 
    def path(self, folder):
        super().path(folder)

class Cmsh(IFile):
    def __init__(self, folder):
        self._format = ".cmsh"
        self.path(folder)
 
 
    def path(self, folder):
        super().path(folder)

