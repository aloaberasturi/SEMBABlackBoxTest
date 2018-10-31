#! /usr/bin/env python
import sembabbt.src.core.filemanager as FM 
import sembabbt.src.apps.test.filters as filters
import sembabbt.src.apps.test.family as testFamily
import json
import pathlib
import subprocess



testOptions = {
    "filters": {#hacer una clase Options en vez de un dict
    "size" : 200,
    "keyWords" : [2,3]
    }
    
}
caseOptions = {}
comparison = "equality"
def searchMatchingProject(self, caseFile):
    with caseFile.open("r") as jsonFile:
        filters.caseOptions = json.loads(jsonFile.read())
        jsonFile.close()

    assert filters.caseOptions["filters"].keys() == \
    filters.testOptions["filters"].keys(), "filters don't match"
      
    if (set(filters.caseOptions["filters"]["keyWords"]) & \
    set(filters.testOptions["filters"]["keyWords"]) != set() and 
    filters.caseOptions["filters"]["size"] <= \
    filters.testOptions["filters"]["size"] ):
        return True

    else : 
        return False

def callSemba(self,fileName):#meter ubicacion del ejecutable desde el launcher
    try:
        folder = pathlib.Path('/home/alejandra/workspace/semba/build/bin/semba/')
        subprocess.run([str(folder),"-i",str(fileName)])
    except: RuntimeError("Unable to launch semba")


def storeOutputs(self, case, test):#asegurarme de que comparo los mismos archivos. Pasar optrqs solo del caso qe estoy testeando
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
                        if (filters.caseOptions["flags"]["comparison"] \
                        == "equality") : 
                            try:                           
                                (SembaTest.EqualityTest())\
                                .test(cast(modelLine[2]), cast(testLine[2]))
                            except: continue
                        elif (filters.caseOptions["flags"]["comparison"] \
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
              