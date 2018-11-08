#! /usr/bin/env python3

import pathlib
import shutil
class FileManager:
    def __init__(self, path, projectName = 'none'):
        self.mainFolder = pathlib.Path(path)
        self.projectFolder = self.mainFolder / projectName
        self.ugrfdtdFolder = self.projectFolder / "ugrfdtd"

    def makeFolders(self):
        self.projectFolder.mkdir(parents=True, exist_ok = True)

    def removeFolders(self):
        try:
            if self.mainFolder.exists:
                shutil.rmtree(str(self.mainFolder))
        except FileNotFoundError: 
            return
                       
    @staticmethod
    def copyFiles(orgn,dstn):
        shutil.copyfile(str(orgn), str(dstn))
