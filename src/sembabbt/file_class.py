#! /usr/bin/env python3
# OpenSEMBA
# Copyright (C) 2015 Salvador Gonzalez Garcia                    (salva@ugr.es)
#                    Luis Manuel Diaz Angulo          (lmdiazangulo@semba.guru)
#                    Miguel David Ruiz-Cabello Nuñez        (miguel@semba.guru)
#                    Alejandra Lopez de Aberasturi Gomez (aloaberasturi@ugr.es)
#                    
# This BaseFile is part of OpenSEMBA.
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


class BaseFile:
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def format(self):
        pass

    @abc.abstractproperty
    def name(self, path):
        return path.parent.name.split("."[0] + str(self.format))

class Dat(BaseFile):
    def format(self):
        self._format = ".dat"
        return self._format

    def name(self, path):
        self._name = super().name(path)


class Nfde(BaseFile):
    def format(self):
        self._format = ".nfde"
        return self._format
    
    def name(self, path):
        self._name = super().name(path)
        return self._name

class Conf(BaseFile):
    def format(self):
        self._format = ".conf"
        return self._format

    def name(self, path):
        self._name = super().name(path)
        return self._name

class Cmsh(BaseFile):
    def format(self):
        self._format = ".cmsh"
        return self._format
    
    def name(self, path):
        self._name = super().name(path)
        return self._name


