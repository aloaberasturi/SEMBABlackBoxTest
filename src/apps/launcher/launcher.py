#! /usr/bin/env python
import sembabbt.src.core.sembabbt as BBT
import sembabbt.src.core.filemanager as FM 
import pathlib

casesPaths = pathlib.Path("/home/alejandra/workspace/sembabbt/data/Cases/")
test = FM.FileManager("/home/alejandra/workspace/sembabbt/data/Testing/")
test.removeFolders()
for file in casesPaths.glob("**/*.test.json"):
    case = FM.FileManager(casesPaths,file.parent.name)
    blackBoxTest = BBT.SembaBBT()#change this though it's not a class anymore
    if blackBoxTest.searchMatchingProject(file):
        test = FM.FileManager("/home/alejandra/workspace/sembabbt/data/Testing/" \
        , file.parent.name.split(".")[0])
        test.makeFolders()
        FM.FileManager.copyFiles(case.projectFolder / (file.parent.name.split\
        (".")[0] + ".dat"),test.projectFolder / (file.parent.name.split(".")[0] \
         + ".dat"))
        blackBoxTest.callSemba(test.projectFolder / (
        file.parent.name.split(".")[0] + ".dat"))
        blackBoxTest.launchTest(blackBoxTest.storeOutputs(case,test))
    else : 
        continue

