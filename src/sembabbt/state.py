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

from decorators import singleton
import json
import pathlib
import filters

@singleton
class State: 
    def __init__(self):
        self.count = 0
        self.tests = []
    def __call__(self, test):
        self.count += 1
        self.tests.append(test)   
        self.search() 

    def search(self): 
        for test in self.tests:#TODO: make this more pythonic and well-indented
            for file in test._input_path.glob("**/*.test.json"):
                with file("r") as json_file:
                    j = json.loads(json_file.read())
                    this_case = filters.Filters(j["filters"]["size"],
                                    [ j["filters"]["keyWords"]["materials"],
                                      j["filters"]["keyWords"]["excitation"],
                                      j["filters"]["keyWords"]["mesh"]
                                    ],
                                      j["filters"]["comparison"],
                                      j["filters"]["execution"]
                                    )
                this_case.keyWords = [x.upper() for x in this_case.keywords] #this line doesn't make sense. See previous versions in git 
          
            if (
                    (set(this_case.keywords) &  set(test.keywords))!= set() 
                    and (this_case.size <= test.size)
                ):
                test._matching_cases.append(pathlib.Path(file))
                return True

            else : 
                return False



    def print_log(self):
        print("Current number of running tests: ", len(self.tests))
        for item in self.tests:
            print (self.tests.index(item) + 1,"-th test")
            print ("EXECUTION MODE: ", item._exec_mode)
            print ("COMPARISON MODE: ", item._comp_mode)
            print ("Test launched under the following filters:")
            for f in item._filters:
                print(f)

    def write_log(self): 
        for item in self.tests:
            with open(pathlib.Path(item._output_path) / "sembabbt.log", "w") as file:
                file.write("EXECUTION MODE: " + str(item._exec_mode))
                file.write("COMPARISON MODE: " +str(item._comp_mode))
                file.write("Test launched under the following filters:")
                for f in item._filters:
                    file.write(str(f))    
            file.close()        