# coding: utf-8
import os
from pathlib import Path
from languages import python as pyt
import json
from classes import fileSourceCode
import writer


def purify_arbo(lst):
    res = list()
    for file in lst:
        res.append(str(file))
    return res


if __name__ == "__main__":
    project_root = input("Please, indicate the path for your project root's :")
    if os.path.isdir(project_root) is False:
        print("Path not exisiting or it's not a directory.")
        quit()

    lenPR = len(project_root)
    if project_root[lenPR-1:] == "\\":
        project_root = project_root[:lenPR-1]
    elif project_root[lenPR-1:] == "/":
        project_root = project_root[:lenPR-1]

    p = Path(project_root)

    lang_ext = list()
    fileDict = dict()
    lst_lang = list()

    F_lst = open("languages/conf.json")
    conf = json.load(F_lst)

    for l in conf:
        lst_lang.append(l)

    for lg in conf:
        lang_ext = conf[lg][0]
        fileDict[lg] = list()
        for ext in lang_ext:
            x = list(p.glob('**/*.'+ext))
            fileDict[lg] = fileDict[lg] + purify_arbo(x)

    # fileDict contient alors la liste des fichiers correpondant à un langage en fonction
    # d'une extension de fichier donné
    FSC_list = list()
    for proL in lst_lang:
        for path in fileDict[proL]:
            try:
                FSC_list.append(pyt.convertPathToObject(path, open(path).read()))
            except PermissionError:
                print("An permission error as been detected")

    writer.create_doc(project_root, FSC_list)
