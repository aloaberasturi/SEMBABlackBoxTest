#! /usr/bin/env python
import sembabbt.src.core.filemanager as FM 
import sembabbt.src.apps.test.filters as filters
import sembabbt.src.apps.test.family as testFamily
from termcolor import cprint,colored
import json
import pathlib
import subprocess


testOptions = filters.Filters(200, [2,3]) 
caseOptions = ()

def searchMatchingProject(caseFile):
    global caseOptions
    with caseFile.open("r") as jsonFile:
        j = json.loads(jsonFile.read())
        caseOptions = filters.Filters(j["filters"]["size"],\
        j["filters"]["keyWords"],j["filters"]["comparison"])

          
    if ((set(caseOptions.keyWords) &  set(testOptions.keyWords))!= set() and 
        (caseOptions.size <= testOptions.size)):
        return True

    else : 
        return False

def callSemba(exePath, fileName):
    try:
        subprocess.run([str(exePath),"-i",str(fileName)])
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

    passes = []
    print(colored("[==========]","green"),"Running ", \
    len(OptRqs)," cases")
    for i in range (0, len(OptRqs)):
        with open(OptRqs[i]) as caseOutput:
            with open(test.ugrfdtdFolder / OptRqs[i].name) as testOutput:
                passes.append(True)    

                try:                    
                    print(colored("[----------]","green"), "Testing", \
                    OptRqs[i].name)
                    print(colored("[ RUN      ]","green"), \
                    caseOptions.comparison, "test")

                    for j in caseOutput:
                        modelLine = (j.split("\n")[0]).split()
                        testLine = ((testOutput.readline()).split("\n")[0]).split()

                        if ((caseOptions.comparison).upper() == "ISEQUAL") : 
                            try:   

                                if testFamily.IsEqual(cast(modelLine[1]),\
                                cast(testLine[1])) == False:
                                    passes[i] = False
                            except ValueError: continue

                        elif ((caseOptions.comparison).upper() == "ISALMOSTEQ"):
                            try:
                                if testFamily.IsAlmostEqual(cast(modelLine[1]), \
                                cast(testLine[1]),tolerance) == False:
                                    passes[i] = False
                            except ValueError: continue

                    if passes[i] ==True:
                        print(colored("[       OK ]","green"), \
                        caseOptions.comparison, "test")
                    else:
                        print(colored("[  FAILED  ]","red"), \
                        caseOptions.comparison, "test")


                except IndexError: "Test and case files don't have the same"\
                " length. Please check that semba compiled correctly"
            testOutput.close() 
        caseOutput.close()

    print(colored("[==========]","green"))           
    print(colored("[  PASSED  ]", "green"), sum(passes), "cases")

    if sum(passes)!=len(OptRqs):        
        print(colored("[  FAILED  ]", "red"), len(OptRqs)-sum(passes), "cases")
        print(len(OptRqs)-sum(passes),"FAILED CASE")
                       
                  
                            