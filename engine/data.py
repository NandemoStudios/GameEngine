import os
import pathlib
import inspect

class Data:
    def __init__(self, FileLocation):
        self.fileLocation = pathlib.Path(FileLocation)
        self.saveData = {}

    def retrieve_name(var):
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
        return [var_name for var_name, var_val in callers_local_vars if var_val is var]

    def AddSaveData(self, data):
        self.saveData.update(data)

    def SaveData(self):
        if self.fileLocation.is_file():
            saveFile = open(self.fileLocation, 'w')
            for item in self.saveData.items():
                saveFile.write(item)
            saveFile.close()
        else:
            saveFile = open(self.fileLocation, 'w+')
            for item in self.saveData.items():
                saveFile.write(item)
            saveFile.close()

    def LoadData(self):
        if self.fileLocation.is_file():
            saveFile = open(self.fileLocation, 'r')
            for item in saveFile.read():
                self.saveData.update(item)
        else:
            open(self.fileLocation, 'w+')
            self.SaveData()