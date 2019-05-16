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


import filters
import comparison 
import json
import subprocess
import os
import pathlib

def search_project(case_file):
    global case_options
    global test_options
    with case_file.open("r") as json_file:
        j = json.loads(json_file.read())
        case_options = filters.Filters(j["filters"]["size"],
                                    [ j["filters"]["keyWords"]["materials"],
                                      j["filters"]["keyWords"]["excitation"],
                                      j["filters"]["keyWords"]["mesh"]
                                    ],
                                      j["filters"]["comparison"],
                                      j["filters"]["execution"]
        )
        case_options.keyWords = [x.upper() for x in case_options.keywords]
          
    if (
       (set(case_options.keywords) &  set(test_options.keywords))!= set() 
       and (case_options.size <= test_options.size)
    ):
        return True

    else : 
        return False



def call_semba(file_name):

    print("                 Entering project " + str(test.project_folder.name))

    try:
        print("-----------------------------------------------------------------"
             )

        print("\n")

        print("                 1. Executing SEMBA")

        #--------------Please comment to display SEMBA's std output-------------

        process = subprocess.Popen(
            ["./semba","-i",str(file_name.name)],
            stdout = subprocess.PIPE,
            cwd = file_name.parent
        )
        process.communicate() 

        #--------------Please uncomment to display SEMBA's std output-----------

        #subprocess.run([str(exePath),"-i",str(fileName)])   
        
        os.remove(str(file_name.parent / "semba"))   


    except RuntimeError:"Unable to launch semba"


def call_ugrfdtd(nfde):
    try:
        print("\n")

        print("                 2. Executing UGRFDTD")

        print("\n")

        print("-----------------------------------------------------------------")
        #----------------Please comment to display UGRFDTD's std output-----------------
   
        process = subprocess.Popen(
            ["./ugrfdtd","-i",str(nfde.name)],
            stdout = subprocess.PIPE, 
            cwd = nfde.parent
        )

        process.communicate() 

        #----------------Please uncomment to display UGRFDTD's std output---------------

        #subprocess.call(["./ugrfdtd","-i",str(nfde.name)], cwd = str(nfde.parent))

        os.system('cls' if os.name == 'nt' else 'clear')
        os.remove(str(nfde.parent / "ugrfdtd"))

    except RuntimeError :"Unable to launch UGRFDTD"

def store_outputs():
    opt_rqs = []
    for i in case.ugrfdtd_folder.glob('**/*_Outputrequests_*'):   
            with i.open("r") as list_of_outputs:
                lines = list_of_outputs.readlines()
                for line in lines:
                    if "!END" in line: 
                        break
                    line = case.ugrfdtd_folder / line.split("\n")[0]

                    opt_rqs.append(pathlib.Path(line))

    return opt_rqs


def launch_test(opt_rqs, cast = float):
    passes = []

    for i in range (0, len(opt_rqs)):
        with open(opt_rqs[i]) as case_output:
            with open(test.ugrfdtd_folder / opt_rqs[i].name) as test_output:
                passes.append(True)    

                try:                    
                    print("[----------] \n     Testing")

                    print("[ RUN      ]",case_options.comparison,"test")

                    for j in case_output:
                        model_line = (j.split("\n")[0]).split()
                        test_line = (
                            (
                                test_output.readline()
                            ).split("\n")[0]
                        ).split()

                        if ((case_options.comparison).upper() == "ISEQUAL") : 
                            try:   

                                if comparison.is_equal(
                                        cast(model_line[1]),
                                        cast(test_line[1])
                                ) == False:
                                    passes[i] = False
                            except ValueError: continue

                        elif ((case_options.comparison).upper() == "ISALMOSTEQ"):
                            try:
                                if comparison.is_almost_equal(
                                        cast(model_line[1]),
                                        cast(test_line[1]),
                                        rel_tolerance,
                                        abs_tolerance
                                ) == False:
                                    passes[i] = False
                            except ValueError: continue

                    if passes[i] ==True:
                        print("[       OK ]",case_options.comparison, "test")                        
                        print("[----------]")
                    else:
                        print("[  FAILED  ]",case_options.comparison, "test")


                except IndexError: 
                   "Test and case files don't have the same length."
                   " Please check that semba compiled correctly"
            test_output.close() 
        case_output.close()

    print("[==========]")           

    if sum(passes)!=len(opt_rqs):       
        print("[  FAILED  ]",len(opt_rqs)-sum(passes),"cases")
            
        print(len(opt_rqs)-sum(passes),"FAILED CASE")
        return False
    else:
        return True
                       
                  
                            