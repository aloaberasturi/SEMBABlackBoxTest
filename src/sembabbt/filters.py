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
import pathlib
import abc
from state import State
from tolerance import Tolerance

class Filters:

    def __init__(self, size, comp_mode, keywords):
        self._size = size
        self._comp_mode = comp_mode 
        if keywords is list:
            self._keywords = keywords
            self.order_kw()
        else:
            raise TypeError("keywords must be given in form of a list")
 
    def order_kw(self):
        self._keywords = [x.upper() for x in self._keywords]

    @property
    def size(self):
        return self._size
        
    @property
    def keywords(self):
        return self._keywords
    
    @property
    def comp_mode(self):
        return self._comp_mode
    




