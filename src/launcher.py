#! /usr/bin/env python3
import sembabbt.src.core.sembabbt as BBT
import sembabbt.src.core.filters as filters
import sembabbt.src.core.filemanager as FM 
import pathlib
import argparse
import colored
from colored import stylize


blue = colored.fg(38)
purple2 = colored.fg(147)
#purple = colored.fg(177)



print(stylize("Welcome to sembaBlackBoxTest.\nPlease insert size of the case"+
" file to be tested as well as the keywords.\nThese inputs will be used in order"+ 
" to find any projects matching your requests.", blue))
print(stylize("\n \nSyntax: \n \npython3",blue),stylize("<program_name.py> <size> " + 
"<1st_kW> <2nd_kW> ... <n-th kW>", purple2))

sembaPath = pathlib.Path('/home/alejandra/workspace/semba/build/bin/semba/')
casesPaths = pathlib.Path("/home/alejandra/workspace/sembabbt/data/Cases/")
BBT.test = FM.FileManager("/home/alejandra/workspace/sembabbt/data/Temp/")
BBT.test.removeFolders()

                       #---Change this parameter if desired another tolerance---
BBT.relTolerance = 2.0 #--- for AlmostEquality tests that can use relative error
                       #--(i.e.: when true value is NOT zero)-------------------
                      
                        
                        #---Change this parameter if desired another tolerance--
BBT.absTolerance = 1e-5 #--- for AlmostEquality tests that can't use relative---
                        #--- error (i.e.: when true value IS zero)--------------


#-----Uncomment if command line arguments are desired during program call------

parser = argparse.ArgumentParser()
parser.add_argument("size",type = int)
parser.add_argument("keyWords", nargs = '+', default = [])

args = parser.parse_args()
BBT.testOptions = filters.Filters(args.size, args.keyWords)

#------Comment if command line arguments are being used------------------------
#BBT.testOptions = filters.Filters(200, ["kw1","kw2"])
                                                  
BBT.testOptions.keyWords = [x.upper() for x in BBT.testOptions.keyWords]
for file in casesPaths.glob("**/*.test.json"):
    BBT.case = FM.FileManager(casesPaths,file.parent.name)

    if BBT.searchMatchingProject(file):
        BBT.test = FM.FileManager(str(BBT.test.mainFolder),\
        file.parent.name.split(".")[0])

        BBT.test.makeFolders()

        FM.FileManager.copyFiles(BBT.case.projectFolder / (file.parent.name.split\
        (".")[0] + ".dat"),BBT.test.projectFolder / (file.parent.name.split(".")[0] \
         + ".dat"))

        BBT.callSemba(sembaPath, BBT.test.projectFolder / (
        file.parent.name.split(".")[0] + ".dat"))
        BBT.launchTest(BBT.storeOutputs())
    else : 
        continue

