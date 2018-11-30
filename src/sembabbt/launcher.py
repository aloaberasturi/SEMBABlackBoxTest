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
import sembabbt.utils as utils
from functools import partial
import pathlib
import shutil
import os
import argparse

def launcher(size,keyWords):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    utils.welcomeMessage()
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

    utils.runningTestsMessage(numTests)
    count = 0
    passedTests = 0
    failedTests = 0

    for file in BBT.case.mainFolder.glob("**/*.test.json"):
        BBT.case = FM.FileManager(str(BBT.case.mainFolder),file.parent.name)
        if BBT.searchMatchingProject(file):
            count += 1
            BBT.test = FM.FileManager(str(BBT.test.mainFolder),file.parent.name)

            BBT.test.makeFolders() 
            FM.FileManager.copyFiles(
                utils.ugrfdtdPath, 
                (BBT.test.ugrfdtdFolder / "ugrfdtd")
            )

          
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
                utils.sembaPath, 
                (BBT.test.projectFolder / "semba")
                )
    
                BBT.callSemba(  
                BBT.test.projectFolder / (file.parent.name.split(".")[0] + ".dat") 
                )               
                
            def case2():

                for genFile in BBT.case.projectFolder.glob("./*.gen"):
                    FM.FileManager.copyFiles(
                    genFile,
                    (BBT.test.ugrfdtdFolder / genFile.name)
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

            def switch(execMode):
                switcher = {
                "normal": case1,
                "ugrfdtd": case2
                }
                func = switcher.get(execMode,"invalid execution flag")
                return func()

          
            switch(BBT.caseOptions.execution)
            BBT.callUGRFDTD( 
                BBT.test.ugrfdtdFolder / (file.parent.name.split(".")[0] + ".nfde"),
            )
            
            doesPass = False
            doesPass = BBT.launchTest(BBT.storeOutputs())

            if doesPass == True:
                passedTests += 1
            else: 
                failedTests += 1       

            print("\n")

            utils.nextTestCaseMessage(count, numTests)          

        else : 
            continue
    utils.passedAndFailedTestsMessage(passedTests,failedTests)
    utils.goodByeMessage()

   

    


