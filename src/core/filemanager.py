#! /usr/bin/env python

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
        if self.mainFolder.exists:
            shutil.rmtree(str(self.mainFolder))
        
    @staticmethod
    def copyFiles(orgn,dst):
        shutil.copyfile(str(orgn), str(dst))

