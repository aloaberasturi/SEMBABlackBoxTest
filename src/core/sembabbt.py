#! /usr/bin/env python3
import sembabbt.src.core.filemanager as FM 
import sembabbt.src.core.filters as filters
import sembabbt.src.core.comparison as comparison
import colored as colored
from colored import stylize
from termcolor import colored as clrd
from termcolor import cprint
import json
import pathlib
import subprocess
from subprocess import Popen,PIPE
import os


def searchMatchingProject(caseFile):
    global caseOptions
    with caseFile.open("r") as jsonFile:
        j = json.loads(jsonFile.read())
        caseOptions = filters.Filters(j["filters"]["size"],\
        j["filters"]["keyWords"],j["filters"]["comparison"])
        caseOptions.keyWords = [x.upper() for x in caseOptions.keyWords]
          
    if ((set(caseOptions.keyWords) &  set(testOptions.keyWords))!= set() and 
        (caseOptions.size <= testOptions.size)):
        return True

    else : 
        return False

def callSemba(exePath, fileName):

    blue = colored.fg(38)
    try:
        print(stylize("--------------------------------------------------------"+
        "---------", blue))
        print("\n")
        cprint("                        Executing SEMBA","blue",\
        attrs=["blink","bold"])
        print("\n")
        print(stylize("--------------------------------------------------------"+
        "---------", blue))
        #--------------Please comment to display SEMBA's std output-------------

        process = Popen([str(exePath),"-i",str(fileName)],stdout = PIPE)
        process.communicate() 

        #-----------Uncomment to display SEMBA's std output---------------------
        #subprocess.run([str(exePath),"-i",str(fileName)])
        
        os.system('cls' if os.name == 'nt' else 'clear')
    except: RuntimeError("Unable to launch semba")


def storeOutputs():
    OptRqs = []
    for i in case.ugrfdtdFolder.glob('**/*_Outputrequests_*'):   
            with i.open("r") as listOfOutputs:
                lines = listOfOutputs.readlines()
                for line in lines:
                    if "!END" in line: 
                        break
                    line = case.ugrfdtdFolder / line.split("\n")[0]
                    OptRqs.append(pathlib.Path(line))

    return OptRqs
def launchTest(OptRqs, cast = float):

    red = colored.fg(1)
    green = colored.fg(82)

    passes = []
    print(stylize("[==========]",green),"Running ", \
    len(OptRqs)," cases")
    for i in range (0, len(OptRqs)):
        with open(OptRqs[i]) as caseOutput:
            with open(test.ugrfdtdFolder / OptRqs[i].name) as testOutput:
                passes.append(True)    

                try:                    
                    print(stylize("[----------]",green), "Testing", \
                    OptRqs[i].name)
                    print(stylize("[ RUN      ]",green), \
                    caseOptions.comparison, "test")

                    for j in caseOutput:
                        modelLine = (j.split("\n")[0]).split()
                        testLine = ((testOutput.readline()).split("\n")[0]).split()

                        if ((caseOptions.comparison).upper() == "ISEQUAL") : 
                            try:   

                                if comparison.IsEqual(cast(modelLine[1]),\
                                cast(testLine[1])) == False:
                                    passes[i] = False
                            except ValueError: continue

                        elif ((caseOptions.comparison).upper() == "ISALMOSTEQ"):
                            try:
                                if comparison.IsAlmostEqual(cast(modelLine[1]), \
                                cast(testLine[1]),relTolerance,absTolerance) == False:
                                    passes[i] = False
                            except ValueError: continue

                    if passes[i] ==True:
                        print(stylize("[       OK ]",green), \
                        caseOptions.comparison, "test")
                        
                        print(stylize("[----------]",green))
                    else:
                        print(stylize("[  FAILED  ]",red), \
                        caseOptions.comparison, "test")


                except IndexError: "Test and case files don't have the same"\
                " length. Please check that semba compiled correctly"
            testOutput.close() 
        caseOutput.close()

    print(stylize("[==========]",green))           
    print(stylize("[  PASSED  ]", green), sum(passes), "cases")

    if sum(passes)!=len(OptRqs):        
        print(stylize("[  FAILED  ]", red), len(OptRqs)-sum(passes), "cases")
        print(len(OptRqs)-sum(passes),"FAILED CASE")
                       
                  
                            