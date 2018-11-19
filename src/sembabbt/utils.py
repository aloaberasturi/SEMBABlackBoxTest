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

import colored
from colored import stylize
from termcolor import cprint
import pathlib
from . import filemanager as FM 
from . import common as BBT

blue = colored.fg(38)
yellow = colored.fg(214)
purple = colored.fg(177)
green = colored.fg(82)
red = colored.fg(1)

sembaPath = pathlib.Path("../bin/semba")
ugrfdtdPath = pathlib.Path("../bin/ugrfdtd")
BBT.case = FM.FileManager("../data/Cases/")
BBT.test = FM.FileManager("../data/Temp/")

def welcomeMessage():
    print(
    stylize(   
        "             Welcome to sembaBlackBoxTest" 
        "\n"
        "\nPlease insert size of the case file to " 
        "be tested as well as the keywords.\nThese inputs will be used in order" 
        " to find any projects matching your requests.", blue
        )
    )

def runningTestsMessage(numTests):

    print(
        stylize("[==========]",green),
        "Running ",
        numTests,
        "tests",
    )
def nextTestCaseMessage(count, numTests):
    if (count == numTests):
        return   
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
    
def passedAndFailedTestsMessage(passedTests,failedTests):
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
def goodByeMessage():
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


