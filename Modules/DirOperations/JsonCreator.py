import json

def CreateJson(dir, FileName, Data):
    """
    ** dir: a string with the directory to which the file will be created
    
    **FileName: string of the file name to be used in the creation

    **Data: the dictionary that will be dumped into the json file (don't stringfy it) ex. {"test": "test"}
    

    creates a json file using the file name and the data inputted

    P.S  format the data before inputting it as it will be dumped directly to the json file
    """
    with open( str(dir) + str(FileName) + '.json', 'w') as JsonFile :
        json.dump(Data, JsonFile)