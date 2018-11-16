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

import sembabbt.launcher as LN
from LN import launcher
from LN import case1
from LN import case2
import argparse
import colored
from colored import stylize

blue = colored.fg(38)
yellow = colored.fg(214)

# if __name__ == "__main__":

    # parser = argparse.ArgumentParser()
    # parser.add_argument("-s","--size",type = int)
    # parser.add_argument("-k","--keyWords", nargs = '+', default = [])
    # args = parser.parse_args()
   
    # if args.size is None or args.keyWords is None:    
    #     parser.error(
    #         print(
    #        stylize("\n \nIncorrect syntax. Please type: \n \npython3",blue),
    #         stylize(
    #             "<program_name.py> -s <Size> -k <Material> <Excitation> <Mesh>",
    #             yellow
    #             )   
    #         )
    #     )

#LN.launcher(args.size,args.keyWords) 
LN.launcher(16000, ["conformal", "hola"])
