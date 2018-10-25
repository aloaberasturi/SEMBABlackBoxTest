#! /usr/bin/env python

import os 
import pdb
import argparse
import json
import shutil
import unittest
import sys
import pathlib

sys.path.insert(0,'/home/alejandra/workspace/sembabbt/src/apps/test')

import SembaTest as semba

def removeFolders():
    folder = pathlib.Path("home/alejandra/workspace/sembabbt/testData/testing")
    if folder.is_dir():
        shutil.rmtree(folder)



# parser = argparse.ArgumentParser()
# parser.add_argument("size",type = int)
# parser.add_argument('keyWords', nargs = '+', default = [])
# args = parser.parse_args()

#TODO: blindar al programa de otros inputs por parte del usuario
    # "size" : args.size,
    # "keyWords" : args.keyWords


testOptions = { 

    "filters": {
        "size" : 200,
        "keyWords" : [2,3]
    }
}


def callSemba(fileName):
    try:
        folder = pathlib.Path('home/alejandra/workspace/semba/build/bin/semba/')
        os.system(folder + " -i" +fileName)
    except: RuntimeError("Unable to launch semba")

def makeDirs(paths):
    for oldDir in paths: 

        aux1 = oldDir.split("/Cases/")[1]
        projectName = aux1.split(".")[0]
        oldDir = pathlib.Path(oldDir)
        aux2 = pathlib.Path("home/alejandra/workspace/sembabbt/testData/testing/")
        newDir = aux2 / projectName / "/"
        os.makedirs(newDir)

        shutil.copyfile(oldDir / projectName / ".dat", \
                        newDir / projectName / ".dat")
        callSemba(newDir /projectName / ".dat")
        

def openOutputs(paths):
    outputFiles = []
    outputPaths = []
    for oldDir in paths:
        aux = oldDir.split("/Cases/")[1]
        projectName = aux.split(".")[0]
        newDir = pathlib.Path("/home/alejandra/workspace/\
                 sembabbt/testData/testing/") / projectName / "ugrfdtd/"

        oldDir = pathlib.Path(oldDir) / "ugrfdtd/"
        for (dp,dn,fn) in os.walk(newDir):
            for f in fn:
                if "_Outputrequests_" in f:
                    with open(dp + f,"r") as listOfOutputs:
                       lines = listOfOutputs.readlines()
                       for line in lines:
                           if "!END" in line: 
                               break
                           line = line.split("\n")[0]
                           outputFiles.append(line)
        for file in outputFiles:
            outputPaths.append((oldDir / file, newDir / file))
    return outputPaths


def launchTests(outputs,cast=float):
    for pair in outputs:
        with open(pair[0]) as modelOutput:
            with open(pair[1]) as testingOutput:

                modelLines = modelOutput.readlines()
                testLines = testingOutput.readlines()

                for line1 in modelLines:
                    for line2 in testLines:

                        if (caseOptions["flags"]["comparison"] == "equality") : 
                            semba.EqualityTest.test( \
                            cast(line1[1:]), cast(line2[1:]))
                            print("launching equality test")

                        elif (caseOptions["flags"]["comparison"] == "almostEq"):
                            tolerance = 9
                            semba.AlmostEqualityTest( \
                            cast(line1[1:]), cast(line2[1:]), tolerance)
                            print("launching almosteq. test")

                
                    
def searchMatchingProjects(test):#TODO: en vez de crear un vector de casos, ir caso por caso lanzando semba
    casesPaths = []
    path = pathlib.Path("home/alejandra/workspace/sembabbt/testData/Cases/")
    for file in path.glob('**/*.test.json'):   
        with open(file,"r") as jsonFile:
            caseOptions = json.loads(jsonFile.read())
            jsonFile.close()

            assert caseOptions["filters"].keys() == \
            testOptions["filters"].keys(), "filters don't match"
          
            if (set(caseOptions["filters"]["keyWords"]) & \
            set(test["filters"]["keyWords"]) != set() and 
            caseOptions["filters"]["size"] <= \
            test["filters"]["size"] ):
                casesPaths.append(dir)
                parseComparison(caseOptions)

    return casesPaths


def parseComparison(test):
    comparison = test["flags"]["comparison"]
    return comparison

removeFolders()
makeDirs(searchMatchingProjects(testOptions))  
launchTests(openOutputs(searchMatchingProjects(testOptions)))






    

