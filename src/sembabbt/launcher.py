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

import common 
import filters
import filemanager 
import utils

def launcher(test):

    common.test.remove_folders()

                       #---Change this parameter if desired another tolerance---
    common.rel_tolerance = 2.0 
                       #--- for AlmostEquality tests that can use relative error
                       #--(i.e.: when true value is NOT zero)-------------------
                      
                        
                        #---Change this parameter if desired another tolerance--
    common.abs_tolerance = 1e-5 
                        #--- for AlmostEquality tests that can't use relative---
                        #--- error (i.e.: when true value IS zero)--------------

   
    common.test_options = filters.Filters(size, keywords)                                                 
    common.test_options.keywords = [x.upper() for x in common.test_options.keywords]

    numTests = 0

    for file in common.case.main_folder.glob("**/*.test.json"):
        if common.search_project(file):
            numTests += 1

    utils.running_message(numTests)
    count = 0
    passedTests = 0
    failedTests = 0

    for file in common.case.main_folder.glob("**/*.test.json"):
        common.case = filemanager.FM(str(common.case.main_folder),file.parent.name)
        if common.search_project(file):
            count += 1
            common.test = filemanager.FM(str(common.test.main_folder),file.parent.name)

            common.test.make_folders() 
            filemanager.FM.copy_folders(
                utils.ugrfdtd_path, 
                (common.test.ugrfdtd_folder / "ugrfdtd")
            )

          
            def case1(): 

                filemanager.FM.copy_folders(
                common.case.project_folder / (file.parent.name.split(".")[0] + ".dat"),
                common.test.project_folder / (file.parent.name.split(".")[0] + ".dat") 
                )         
                for genFile in common.case.project_folder.glob("./*.gen"):
                    filemanager.FM.copy_folders(
                    genFile,
                    (common.test.project_folder / genFile.name)
                ) 

                filemanager.FM.copy_folders(
                utils.semba_path, 
                (common.test.project_folder / "semba")
                )
    
                common.call_semba(  
                common.test.project_folder / (file.parent.name.split(".")[0] + ".dat") 
                )               
                
            def case2():

                for genFile in common.case.project_folder.glob("./*.gen"):
                    filemanager.FM.copy_folders(
                    genFile,
                    (common.test.ugrfdtd_folder / genFile.name)
                ) 

                filemanager.FM.copy_folders(
                    common.case.ugrfdtd_folder / (file.parent.name.split(".")[0] + ".nfde"),
                    common.test.ugrfdtd_folder / (file.parent.name.split(".")[0] + ".nfde")
                )

                try: 
                    filemanager.FM.copy_folders(
                    common.case.ugrfdtd_folder / (file.parent.name.split(".")[0] + ".cmsh"),
                    common.test.ugrfdtd_folder / (file.parent.name.split(".")[0] + ".cmsh")
                    )
                except: pass

                try: 
                    filemanager.FM.copy_folders(
                    common.case.ugrfdtd_folder / (file.parent.name.split(".")[0] + ".conf"),
                    common.test.ugrfdtd_folder / (file.parent.name.split(".")[0] + ".conf")
                    )
                except: pass

            def switch(execMode):
                switcher = {
                "normal": case1,
                "ugrfdtd": case2
                }
                func = switcher.get(execMode,"invalid execution flag")
                return func()

          
            switch(common.caseOptions.execution)
            common.call_ugrfdtd( 
                common.test.ugrfdtd_folder / (file.parent.name.split(".")[0] + ".nfde"),
            )
            
            doesPass = False
            doesPass = common.launchTest(common.storeOutputs())

            if doesPass == True:
                passedTests += 1
            else: 
                failedTests += 1       

            print("\n")

            utils.next_test_message(count, numTests)          

        else : 
            continue
    utils.passed_tests_message(passedTests,failedTests)
    utils.goodbye_message()
