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
    def __init__(self, path):
        self._path = path
        self._format = None

    @abc.abstractproperty
    def name(self):
        if self._path.parent.name.split("."[0] + str(self._format)).exists:
            return self._path.parent.name.split("."[0] + str(self._format))
        else:
            return False

class Dat(IFile):
    def __init__(self, path):
        self._format = ".dat"
        self._path = path
        self.name()
 
    def name(self):
        pass

class Nfde(IFile):
    def __init__(self, path):
        self._format = ".nfde"
        self._path = path
        self.name()
 
    def name(self):
        pass
    
class Conf(IFile):
    def __init(self, path):
        self._format = ".conf"
        self._path = path
        self.name()
 
    def name(self):
        pass

class Cmsh(IFile):
    def __init__(self, path):
        self._format = ".cmsh"
        self._path = path
        self.name()
 
    def name(self):
        pass

