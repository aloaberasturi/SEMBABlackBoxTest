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

import json
import shutil
from sembabbt.filters import Filters
from sembabbt.project_folder import ProjectFolder
from sembabbt.callers import call_semba, call_ugrfdtd


def launch(test): 
    for path in test._exec_info._input_path.glob("**/*.test.json"): 
        print(type(path))
        with open(path, "r") as json_file:
            j = json.loads(json_file.read())
            case_filters = Filters(
                j["filters"]["size"],
                j["filters"]["comparison"],
                [
                    j["filters"]["keyWords"]["materials"],
                    j["filters"]["keyWords"]["excitation"],
                    j["filters"]["keyWords"]["mesh"]
                ]            
            )       
            json_file.close()   
        if (set(case_filters._keywords) &  set(test._filters._keywords)
            != set() and case_filters._size <= test._filters._size):
            test.new_folder(path)
            call_executable(test._folder)
            copy_and_clean(test._folder)
        else : 
            pass   
             
    def call_executable(f): 
        if f._can_call_ugrfdtd():
            call_ugrfdtd(f)
        else:
            call_semba(f)
            call_ugrfdtd(f) 

    def copy_and_clean(folder):
        try:
            shutil.rmtree(
                str(test._exec_info._output_path / folder._project_name)
            )
        except FileNotFoundError: 
            pass
        shutil.copytree(
            str(folder._main_f["test"]), 
            str(test._exec_info._output_path / folder._project_name)
        )
        shutil.rmtree(folder._main_f["test"])

    

