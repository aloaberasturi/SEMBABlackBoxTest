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

from sembabbt.launcher2  import Launcher
from sembabbt.testobject import Test

kwargs = {
    "size"         : 131381,
    "comp_mode"    : "Equal", 
    "keywords"     : [1,2,3], 
    "input_path"   : "www.hola.com",
    "output_path"  : "www.adios.com",
    "semba_path"   : "www.semba.com",
    "ugrfdtd_path" : "www.ugr.com",
    "exec_mode"    : "normal"
    }

#the above can also be loaded in the form of a json file
test1 = Test(**kwargs)
l1 = Launcher(test1) 



