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
import inspect
import filemanager 
import common 
import bin.semba_bin as bin
import data.semba_data as data

bin_path = pathlib.Path(bin.__file__).parent
data_path = pathlib.Path(data.__file__).parent

sembaPath = bin_path / "semba"
ugrfdtdPath = bin_path / "ugrfdtd"
common.case = filemanager.FM(data_path / "Cases")
common.test = filemanager.FM(data_path / "Temp")

    
def passed_tests_message(passed_tests,failed_tests):
    print("[  PASSED  ] ",passed_tests," tests")
    print("[  FAILED  ] ",failed_tests," tests")
def goodbye_message():
    print("-----------------------------------------------------------------")

    print("                  SEMBA BlackBoxTest Finished")

    print("-----------------------------------------------------------------")
    print("\n")


