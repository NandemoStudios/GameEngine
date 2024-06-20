import os
import pathlib
import inspect

class Data:
    def __init__(self, fileLocation):
        self.fileLocation = fileLocation
        self.DataToSave = []
        self.ReadData = []
        
        open(self.fileLocation, 'w+')
        


    def AddSaveData(self, data):
        self.DataToSave.append(data)

    def SaveData(self):
        saveFile = open(self.fileLocation, 'w')
        for item in self.DataToSave:
            saveFile.write(str(item)+'\n')
        saveFile.close()
        self.DataToSave.clear()

    def LoadData(self):
        saveFile = open(self.fileLocation, 'r')
        print(os.stat(self.fileLocation))
        if not os.stat(self.fileLocation) == 0:
            for item in saveFile.readlines():
                self.ReadData.append(item)
        else:
            return False
        return self.ReadData
