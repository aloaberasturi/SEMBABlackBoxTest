#! /usr/bin/env python
import sys
import FileManager as FM
import json
import pathlib
import subprocess

sys.path.insert(0,'/home/alejandra/workspace/sembabbt/src/apps/test')
import SembaTest


class SembaBBT: 
    testOptions = { 
    "filters": {
        "size" : 200,
        "keyWords" : [2,3]
        }
    
    }
    caseOptions = {}
    def searchMatchingProject(self, caseFile):
        with caseFile.open("r") as jsonFile:
            SembaBBT.caseOptions = json.loads(jsonFile.read())
            jsonFile.close()

        assert SembaBBT.caseOptions["filters"].keys() == \
        SembaBBT.testOptions["filters"].keys(), "filters don't match"
          
        if (set(SembaBBT.caseOptions["filters"]["keyWords"]) & \
        set(SembaBBT.testOptions["filters"]["keyWords"]) != set() and 
        SembaBBT.caseOptions["filters"]["size"] <= \
        SembaBBT.testOptions["filters"]["size"] ):
            return True

        else : 
            return False

    def callSemba(self,fileName):
        try:
            folder = pathlib.Path('/home/alejandra/workspace/semba/build/bin/semba/')
            subprocess.run([str(folder),"-i",str(fileName)])
        except: RuntimeError("Unable to launch semba")


    def storeOutputs(self, case, test):
        OptRqs = {
            "case" : [],
            "test" : []
        }
        for i in case.ugrfdtdFolder.glob('**/*_Outputrequests_*'):   
                with i.open("r") as listOfOutputs:
                    lines = listOfOutputs.readlines()
                    for line in lines:
                        if "!END" in line: 
                            break
                        line = case.ugrfdtdFolder / line.split("\n")[0]
                        OptRqs["case"].append(pathlib.Path(line))
        for i in test.ugrfdtdFolder.glob('**/*_Outputrequests_*'):   
                with i.open("r") as listOfOutputs:
                    lines = listOfOutputs.readlines()
                    for line in lines:
                        if "!END" in line: 
                            break
                        line = test.ugrfdtdFolder / line.split("\n")[0]
                        OptRqs["test"].append(pathlib.Path(line))
        return OptRqs


    def launchTest(self, OptRqs, cast = float):

        #-------Change this parameter to set Almost-Equality preferences-------

        tolerance = 0.0 

        #----------------------------------------------------------------------
        assert len(OptRqs["case"]) == len(OptRqs["test"]), "number of " \
        "outputRqs is different in Testing and Cases folder. Please make sure" \
        "you are calling Semba from the right directory and testcase." \
        "Unable to launch tests"        
        for i in range (0, len(OptRqs["case"])-1):
            with open(OptRqs["case"][i]) as caseOutput:
                with open(OptRqs["test"][i]) as testOutput:
                    try:
                        for i in range(0, len(OptRqs["case"])):
                            modelLine = (caseOutput.readline()).split("\n")[0]
                            testLine = (testOutput.readline()).split("\n")[0]
                            modelLine = modelLine.split()
                            testLine = testLine.split()
                            if (SembaBBT.caseOptions["flags"]["comparison"] \
                            == "equality") : 
                                try:                           
                                    (SembaTest.EqualityTest())\
                                    .test(cast(modelLine[2]), cast(testLine[2]))
                                except: continue

                            elif (SembaBBT.caseOptions["flags"]["comparison"] \
                            == "almostEq"):
                                try:
                                    SembaTest.AlmostEqualityTest.test( \
                                    cast(modelLine[2]), cast(testLine[2]),tolerance)
                                except TypeError: continue
                        caseOutput.close()
                        testOutput.close()        
                        
                    except: EOFError("Case output-requests files have " \
                    "different size to Testing output-requests files, so they" \
                    "can't be compared. Please make sure you are calling Semba" \
                    "from the right directory and testcase. Unable to launch tests")
                