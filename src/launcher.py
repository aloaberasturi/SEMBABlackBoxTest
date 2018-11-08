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

import sembabbt.common as BBT
import sembabbt.filters as filters
import sembabbt.filemanager as FM 
import pathlib
import argparse
import colored
from colored import stylize


blue = colored.fg(38)
yellow = colored.fg(214)
#purple2 = colored.fg(147)
#purple = colored.fg(177)

print(
    stylize(
        "Welcome to sembaBlackBoxTest.\nPlease insert size of the case file to " 
        "be tested as well as the keywords.\nThese inputs will be used in order" 
        " to find any projects matching your requests.", blue
    )
)
print(
    stylize("\n \nSyntax: \n \npython3",blue),
    stylize(
        "<program_name.py> <Size> <Material> <Excitation> <Mesh>", yellow
    )
)

sembaPath = pathlib.Path("../bin/semba")
# casesPaths = pathlib.Path("../data/Cases/")
BBT.case = FM.FileManager("../data/Cases/")
BBT.test = FM.FileManager("../data/Temp/")
BBT.test.removeFolders()

                       #---Change this parameter if desired another tolerance---
BBT.relTolerance = 2.0 #--- for AlmostEquality tests that can use relative error
                       #--(i.e.: when true value is NOT zero)-------------------
                      
                        
                        #---Change this parameter if desired another tolerance--
BBT.absTolerance = 1e-5 #--- for AlmostEquality tests that can't use relative---
                        #--- error (i.e.: when true value IS zero)--------------


#-----Uncomment if command line arguments are desired during program call------

# parser = argparse.ArgumentParser()
# parser.add_argument("size",type = int)
# parser.add_argument("keyWords", nargs = '+', default = [])

# args = parser.parse_args()
# BBT.testOptions = filters.Filters(args.size, args.keyWords)

#------Comment if command line arguments are being used------------------------
BBT.testOptions = filters.Filters(200, ["SGBC","planeWave","conformal"])
                                                  
BBT.testOptions.keyWords = [x.upper() for x in BBT.testOptions.keyWords]
for file in BBT.case.mainFolder.glob("**/*.test.json"):
    BBT.case = FM.FileManager(str(BBT.case.mainFolder),file.parent.name)

    if BBT.searchMatchingProject(file):
        BBT.test = FM.FileManager(str(BBT.test.mainFolder),file.parent.name)

        BBT.test.makeFolders()

        FM.FileManager.copyFiles(
            BBT.case.projectFolder / (file.parent.name.split(".")[0] + ".dat"),
            BBT.test.projectFolder / (file.parent.name.split(".")[0] + ".dat") 
        )

        BBT.callSemba( 
            sembaPath, 
            BBT.test.projectFolder / (file.parent.name.split(".")[0] + ".dat") 
        )
        BBT.launchTest(BBT.storeOutputs())
    else : 
        continue

print("SEMBA BlackBoxTest Finished")

