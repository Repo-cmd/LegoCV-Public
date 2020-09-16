import os


def DeleteFile(FileName):
    """
    **FileName: a string with the file name and location

    checks if the file in the provided directory exists then deletes it
    """
    if os.path.exists(FileName):
        os.remove(FileName)
    else:
        print("file doesn't exist")