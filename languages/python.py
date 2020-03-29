from classes import fileSourceCode, classO
from parse_python_indentation import parse_indentation as PI


def iterdict(d):
    resSuite = list()
    for k, v in d.items():
        if isinstance(v, dict):
            iterdict(v)
        else:
            resSuite.append(v)
    return resSuite


def convertPathToObject(path, file_content):
    FSC = fileSourceCode()
    # print(FSC.__dict__)
    # print("\n")
    FSC.setPathName(path)
    FSC.languages = "python"

    tabParse = PI.parse_indentation(file_content)
    aS = list()

    # print(path)

    for j in tabParse:
        tmpaS = iterdict(j)
        aS = aS + tmpaS

    flag_class = 0
    old_i = ""
    for i in aS:
        if "def" in i:
            FSC.addFunc(i)

        elif "class" in i:
            #print(i)
            flag_class = 1
            FSC.addClass(i)
            old_i = i

        elif flag_class == 1:
            flag_class = 0
            for j in i:
                if "def" in j["key"]:
                    FSC.addClassMeth(old_i, j['key'])
            old_i = ""

    return FSC
