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
import inspect
import sembabbt.filemanager as FM 
import sembabbt.common as BBT
import bin.sembabbt_bin as bbtbin
import data.sembabbt_data as data

blue = colored.fg(38)
yellow = colored.fg(214)
purple = colored.fg(177)
green = colored.fg(82)
red = colored.fg(1)

binPath = pathlib.Path(bbtbin.__file__).parent
dataPath = pathlib.Path(data.__file__).parent

sembaPath = binPath / "semba"
ugrfdtdPath = binPath / "ugrfdtd"
BBT.case = FM.FileManager(dataPath / "Cases")
BBT.test = FM.FileManager(dataPath / "Temp")


def welcomeMessage():
    print(
    stylize(   
        "             Welcome to sembaBlackBoxTest" 
        "\n"
        "\n '-s' Input determines MAXIMUM size of cases to be tested. Together"
        " with words following '-k' flag, these parameters will be used in order" 
        " to find projects matching your requests inside /data/ folder.", blue
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


