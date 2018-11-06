#! /usr/bin/env python
import sembabbt.src.core.sembabbt as BBT
import sembabbt.src.apps.test.filters as filters
import sembabbt.src.core.filemanager as FM 
import pathlib

sembaPath = pathlib.Path('/home/alejandra/workspace/semba/build/bin/semba/')
casesPaths = pathlib.Path("/home/alejandra/workspace/sembabbt/data/Cases/")
BBT.test = FM.FileManager("/home/alejandra/workspace/sembabbt/data/Testing/")
BBT.test.removeFolders()
BBT.tolerance = 2.0 #---Change this parameter for AlmostEqual test---

for file in casesPaths.glob("**/*.test.json"):
    BBT.case = FM.FileManager(casesPaths,file.parent.name)

    if BBT.searchMatchingProject(file):
        BBT.test = FM.FileManager("/home/alejandra/workspace/sembabbt/data/Testing/" \
        , file.parent.name.split(".")[0])

        BBT.test.makeFolders()

        FM.FileManager.copyFiles(BBT.case.projectFolder / (file.parent.name.split\
        (".")[0] + ".dat"),BBT.test.projectFolder / (file.parent.name.split(".")[0] \
         + ".dat"))

        BBT.callSemba(sembaPath, BBT.test.projectFolder / (
        file.parent.name.split(".")[0] + ".dat"))
        BBT.launchTest(BBT.storeOutputs())
    else : 
        continue

