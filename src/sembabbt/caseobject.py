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

from file_class import Dat, Nfde, Conf, Cmsh
from filters import Filters
from folder import CaseFolder
import json
class Case():
    def __init__(self, json_file):
        j = json.loads(json_file.read())
        self._exec_m =  j["filters"]["execution"]
        self._folder = CaseFolder(json_file)
        self._filters = Filters(
                        size = j["filters"]["size"],
                        comp_mode = j["filters"]["comparison"],
                        keywords =[
                            j["filters"]["keyWords"]["materials"],
                            j["filters"]["keyWords"]["excitation"],
                            j["filters"]["keyWords"]["mesh"]
                        ]
        )

                
    @property
    def filters(self):
        return self._filters
    
    @property
    def exec_m(self):
        return self._exec_m

    def can_call_ugrfdtd(self):
        if self._exec_m == "normal":
            if ".nfde" in self._folder._formats:
                return True
            else:
                return False
        else:
            return True
