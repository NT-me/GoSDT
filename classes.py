import os


class classO(object):
    """docstring for classO."""

    def __init__(self):
        super(classO, self).__init__()
        self.name = ""
        self.lstMeth = list()

    def addMeth(self, name):
        self.lstMeth.append(name)


class fileSourceCode(object):
    """docstring for fileSourceCode."""

    def __init__(self):
        super(fileSourceCode, self).__init__()
        self.path = ""
        self.name = ""
        self.languages = ""
        self.lstClassO = list()
        self.lstFunc = list()

    def __str__(self):
        res = self.path + "\n"
        res += self.name + "\n"
        res += self.languages + "\n"
        for i in self.lstClassO:
            res += str(i.__dict__) + "\n"
        res += str(self.lstFunc) + "\n"

        return res

    def setPathName(self, path):
        self.path = path
        self.name = os.path.split(path)[1]

    def addClass(self, className):
        newClass = classO()
        newClass.name = className
        self.lstClassO.append(newClass)

    def addClassMeth(self, className, methName):
        for C in self.lstClassO:
            if C.name == className:
                C.addMeth(methName)

    def addFunc(self, funcName):
        self.lstFunc.append(funcName)
