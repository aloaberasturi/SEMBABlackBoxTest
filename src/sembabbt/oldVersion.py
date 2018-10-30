#! /usr/bin/env python

import os 
import pdb
import argparse
import json
import shutil
import unittest
import sys
import pathlib
import subprocess

sys.path.insert(0,'/home/alejandra/workspace/sembabbt/src/apps/test')

import SembaTest as semba

def removeFolders():
    folder = pathlib.Path("/home/alejandra/workspace/sembabbt/data/Testing/")
    if folder.exists():
        shutil.rmtree(str(folder))

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

#solucion provisional: hacer caseOptions una variable global

caseOptions = {}


def callSemba(fileName):
    try:
        folder = pathlib.Path('/home/alejandra/workspace/semba/build/bin/semba/')
        subprocess.run([str(folder),"-i",str(fileName)])
    except: RuntimeError("Unable to launch semba")

def makeFolders(paths):
    for oldDir in paths: 
        aux1 = str(oldDir).split("/Cases/")[1]
        projectName = aux1.split(".")[0] 
        aux2 = pathlib.Path("/home/alejandra/workspace/sembabbt/data/Testing/")
        newDir = aux2 / projectName      
        newDir.mkdir(parents=True, exist_ok = True)
        modelFile = oldDir / (projectName + ".dat")
        newFile = newDir / (projectName + ".dat")
        shutil.copyfile(str(modelFile), str(newFile))

        callSemba(newFile)
        

def openOutputs(paths):
    outputFiles = []
    outputPaths = []
    for oldDir in paths:
        aux = str(oldDir).split("/Cases/")[1]
        projectName = aux.split(".")[0]
        newDir = pathlib.Path("/home/alejandra/workspace/" +
        "sembabbt/data/Testing/") / projectName / "ugrfdtd/"

        oldDir = oldDir / "ugrfdtd/"
        for i in newDir.glob('**/*_Outputrequests_*'):   
            with i.open("r") as listOfOutputs:
                lines = listOfOutputs.readlines()
            #     for (dp,dn,fn) in os.walk(newDir):
            # for f in fn:
            #     if "_Outputrequests_" in f:
            #         with open(dp + f,"r") as listOfOutputs:
            #            lines = listOfOutputs.readlines()
                for line in lines:
                    if "!END" in line: 
                        break
                    line = line.split("\n")[0]
                    outputFiles.append(pathlib.Path(line))
        for j in outputFiles:
            outputPaths.append((oldDir / j.name, newDir / j.name))
    return outputPaths


def launchTests(outputs,cast=float):
    global caseOptions
    for pair in outputs:
        with open(pair[0]) as modelOutput:
            with open(pair[1]) as testingOutput:
                length1 = len(modelOutput.readlines())
                length2 = len(testingOutput.readlines())
                assert length1 == length2 #TODO: HACER LOS ERRORES MAS FACILES DE DEBUGGEAR
                modelOutput.close()
                testingOutput.close()
        with open(pair[0]) as modelOutput:
            with open(pair[1]) as testingOutput:   
                for i in range (0, length1-1):
                    modelLine = (modelOutput.readline()).split("\n")[0]
                    testLine = (testingOutput.readline()).split("\n")[0]
                    modelLine = modelLine.split()
                    testLine = testLine.split()
                    if (caseOptions["flags"]["comparison"] == "equality") : 
                        try:                           
                            (semba.EqualityTest()).test(cast(modelLine[2]),\
                            cast(testLine[2]))
                        except: continue

                    elif (caseOptions["flags"]["comparison"] == "almostEq"):
                        tolerance = 9
                        try:
                            semba.AlmostEqualityTest.test( \
                            cast(modelLine[2]), cast(testLine[2]), tolerance)
                        except TypeError: continue
    modelOutput.close()
    testingOutput.close()
                           
                    
def searchMatchingProjects():#TODO: en vez de crear un vector de casos, ir caso por caso lanzando semba
    casesPaths = []
    global caseOptions
    path = pathlib.Path("/home/alejandra/workspace/sembabbt/data/Cases/")
    for file in path.glob('**/*.test.json'):   
        with file.open("r") as jsonFile:
            caseOptions = json.loads(jsonFile.read())
            jsonFile.close()

            assert caseOptions["filters"].keys() == \
            testOptions["filters"].keys(), "filters don't match"
          
            if (set(caseOptions["filters"]["keyWords"]) & \
            set(testOptions["filters"]["keyWords"]) != set() and 
            caseOptions["filters"]["size"] <= \
            testOptions["filters"]["size"] ):
                casesPaths.append(file.parent)
                parseComparison(caseOptions)                

    return casesPaths


def parseComparison(test):
    comparison = test["flags"]["comparison"]
    return comparison

removeFolders()
makeFolders(searchMatchingProjects())  

launchTests(openOutputs(searchMatchingProjects()))






    

