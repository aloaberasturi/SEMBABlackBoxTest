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

from . import common as BBT
from . import filters as filters
from . import filemanager as FM 
from functools import partial
import pathlib
import shutil
import os
import argparse
import colored
from colored import stylize
from termcolor import cprint

def launcher(size,keyWords):

    sembaPath = pathlib.Path("../bin/semba")
    ugrfdtdPath = pathlib.Path("../bin/ugrfdtd")
    BBT.case = FM.FileManager("../data/Cases/")
    BBT.test = FM.FileManager("../data/Temp/")

    blue = colored.fg(38)
    yellow = colored.fg(214)
    purple = colored.fg(177)
    green = colored.fg(82)
    red = colored.fg(1)
    print(
    stylize(
        "             Welcome to sembaBlackBoxTest" 
        "\n"
        "\nPlease insert size of the case file to " 
        "be tested as well as the keywords.\nThese inputs will be used in order" 
        " to find any projects matching your requests.", blue
    )
    )
   

    BBT.test.removeFolders()

                       #---Change this parameter if desired another tolerance---
    BBT.relTolerance = 2.0 
                       #--- for AlmostEquality tests that can use relative error
                       #--(i.e.: when true value is NOT zero)-------------------
                      
                        
                        #---Change this parameter if desired another tolerance--
    BBT.absTolerance = 1e-5 
                        #--- for AlmostEquality tests that can't use relative---
                        #--- error (i.e.: when true value IS zero)--------------


    
    BBT.testOptions = filters.Filters(size, keyWords)                                                 
    BBT.testOptions.keyWords = [x.upper() for x in BBT.testOptions.keyWords]

    numTests = 0

    for file in BBT.case.mainFolder.glob("**/*.test.json"):
        if BBT.searchMatchingProject(file):
            numTests += 1

    print(
        stylize("[==========]",green),
        "Running ",
        numTests,
        "tests",
    )

    count = 0
    passedTests = 0
    failedTests = 0

    for file in BBT.case.mainFolder.glob("**/*.test.json"):
        BBT.case = FM.FileManager(str(BBT.case.mainFolder),file.parent.name)
        if BBT.searchMatchingProject(file):
            count += 1
            BBT.test = FM.FileManager(str(BBT.test.mainFolder),file.parent.name)

            BBT.test.makeFolders() 

          
            def case1(): 

                FM.FileManager.copyFiles(
                BBT.case.projectFolder / (file.parent.name.split(".")[0] + ".dat"),
                BBT.test.projectFolder / (file.parent.name.split(".")[0] + ".dat") 
                )         
                for genFile in BBT.case.projectFolder.glob("./*.gen"):
                    FM.FileManager.copyFiles(
                    genFile,
                    (BBT.test.projectFolder / genFile.name)
                ) 

                FM.FileManager.copyFiles(
                sembaPath, 
                (BBT.test.projectFolder / "semba")
                )
    
                BBT.callSemba(  
                BBT.test.projectFolder / (file.parent.name.split(".")[0] + ".dat") 
                )
        
                FM.FileManager.copyFiles(
                ugrfdtdPath, 
                (BBT.test.ugrfdtdFolder / "ugrfdtd")
                )
               

                BBT.callUGRFDTD( 
                BBT.test.ugrfdtdFolder / (file.parent.name.split(".")[0] + ".nfde"),
                )
                
            def case2():

                for genFile in BBT.case.projectFolder.glob("./*.gen"):
                    FM.FileManager.copyFiles(
                    genFile,
                    (BBT.test.ugrfdtdFolder / genFile.name)
                ) 

                FM.FileManager.copyFiles(
                    ugrfdtdPath, 
                    (BBT.test.ugrfdtdFolder / "ugrfdtd")
                )
                FM.FileManager.copyFiles(
                    BBT.case.ugrfdtdFolder / (file.parent.name.split(".")[0] + ".nfde"),
                    BBT.test.ugrfdtdFolder / (file.parent.name.split(".")[0] + ".nfde")
                )

                try: 
                    FM.FileManager.copyFiles(
                    BBT.case.ugrfdtdFolder / (file.parent.name.split(".")[0] + ".cmsh"),
                    BBT.test.ugrfdtdFolder / (file.parent.name.split(".")[0] + ".cmsh")
                    )
                except: pass

                try: 
                    FM.FileManager.copyFiles(
                    BBT.case.ugrfdtdFolder / (file.parent.name.split(".")[0] + ".conf"),
                    BBT.test.ugrfdtdFolder / (file.parent.name.split(".")[0] + ".conf")
                    )
                except: pass

                BBT.callUGRFDTD( 
                BBT.test.ugrfdtdFolder / (file.parent.name.split(".")[0] + ".nfde"),
                )

            def switch(execMode):
                switcher = {
                "normal": case1,
                "ugrfdtd": case2
                }
                func = switcher.get(execMode,"invalid execution flag")
                return func()

          
            switch(BBT.caseOptions.execution)
            
            doesPass = False
            doesPass = BBT.launchTest(BBT.storeOutputs())

            if doesPass == True:
                passedTests += 1
            else: 
                failedTests += 1       

            print("\n")

            if (count == numTests):
                continue

            elif (count +1) == 2:
                print(stylize(
                    "press Enter to continue with " +
                    str(count + 1) + "nd test case...",
                    purple
                    )
                )
            elif (count +1) == 3:
                print(stylize(
                    "press Enter to continue with " + 
                    str(count + 1) + "rd test case...",
                    purple
                    )
                )
            else:
                print(stylize(
                    "press Enter to continue with " + 
                    str(count + 1) + "th test case...",
                    purple
                    )
                ) 

            print("\n")
            input()

        else : 
            continue

    print(
        stylize("[  PASSED  ]", green),
        passedTests,
        "tests"
    )
    print(
        stylize("[  FAILED  ]", red),
        failedTests,
        "tests"
    )


    
    print(stylize(
    "-----------------------------------------------------------------", 
    blue)
    )

    cprint(
    "                  SEMBA BlackBoxTest Finished",
    "blue",
    attrs=["bold"]
    )

    print(stylize(
        "-----------------------------------------------------------------", 
        blue)
    )
    print("\n")


