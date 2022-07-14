import random

def genRandomBinaryTable(table, length):
    for i in range(length):
        table.append(random.randint(0,1))
def convertTableToString(table, mode):
    string = ""
    if mode == 1:
        loop = 0
        for i in table:
            if loop != len(table):
                string = string + i + " "
            else:
                string = string + i
            loop += 1
    elif mode == 2:
        for i in table:
            string = string + i
    return string


class data():
    def __init__(self,name="",value=None):
        self.name = name
        self.value = value
    def getName(self):
        return self.name
    def getDataType(self):
        return type(self.value)

class dataObject():
    def __init__(self):
        self.data = []
    def addData(self,name,value):
        self.data.append(data(name=name,value=value))
    def findData(self,name):
        for i in self.data:
            if i.getName() == name:
                return i
    def saveData(self,filename):
        file = open(filename,"w")
        toWrite = ""
        for i in self.data:
            pass
