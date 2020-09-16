import json


def ReadJson(Dir, FileName):
    """
    **FileName: string of the file name to be used in the creation

    Reads a Json file and returns the output

    P.S  file name with the directory but without extension ex. /test
    """

    y = json.load(open(str(Dir) + str(FileName) + '.json','r'))

    return y
