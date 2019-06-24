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

from subprocess import Popen, PIPE
import os  
from sembabbt.state import State
from sembabbt.test  import Test


def call_semba(test):
    try:
        process = Popen(
            [
                (test._exec_info._semba_path).as_posix(),
                "-i", 
                test._folder._files["Dat"]._test_path[0].as_posix()
            ],
            stdout = PIPE,
            cwd = test._folder._main_f["test"]
        )
        process.communicate()    

       #------------------Uncomment to display SEMBA's std output--------------#
       #                                                                       #
       #subprocess.run([(State.semba_path).as_posix(),"-i",test._files["Dat"]])#
       #                                                                       #
       #-----------------------------------------------------------------------#
        
    except RuntimeError:"Unable to launch semba"

def call_ugrfdtd(test):
    try:
        process = Popen(
            [
                (test._exec_info._ugrfdtd_path).as_posix(),
                "-i",
                test._folder._files["Nfde"]._test_path[0].as_posix()
            ],
            stdout = PIPE, 
            cwd = test._folder._ugrfdtd_f["test"]
        )
        process.communicate() 
        os.system('cls' if os.name == 'nt' else 'clear')
        test._folder._files["Dat"].resulting_data_files()

    except RuntimeError:"Unable to launch ugrfdtd"
     
