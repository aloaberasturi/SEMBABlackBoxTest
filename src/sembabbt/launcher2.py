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

from filters import Filters
from folder import Folder
from case import Case
import json
import pathlib

class Launcher:
    def __new__(cls, test):
        cls._test = test
        cls.search()
        #TODO: cls.switcher
        #TODO: cls.copy
        cls.launch()
    
    @classmethod
    def search(cls): 
        for file in cls._test._input_path.glob("**/*.test.json"):
            with file("r") as json_file:
                j = json.loads(json_file.read())
                c = Case(file)
                c.filters = Filters(j["filters"]["size"],
                                [ j["filters"]["keyWords"]["materials"],
                                  j["filters"]["keyWords"]["excitation"],
                                  j["filters"]["keyWords"]["mesh"]
                                ],
                                  j["filters"]["comparison"],
                                  j["filters"]["execution"]
                                )
            c.filters.keywords = [x.upper() for x in c.filters.keywords]

            if (
                    (set(c.filters.keywords) &  set(cls._test.keywords))!= set() 
                    and (c.filters.size <= cls._test.size)
                ):
                cls._test._matching_cases.append(c)
                return True
            else : 
                return False

    @classmethod
    def switch(cls):
        pass

    @classmethod
    def copy(cls):
        pass

    @classmethod
    def launch(cls):
        pass
