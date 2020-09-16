import os
import shutil
import getpass


def MoveFiles(TargetDir, TargetFile, DestinationDire):

    """
    ** TargetDir: str of the directory from which to transfere the file ex: 'documents/example'

    ** TargetFile: str of the file to be moved  ex: 'test.docx'

    ** DestinationDire: str of the directory to which the file will be transfered  ex: 'templates/example/test.docx'

    Moves TargetFile from a TargetDir to DestinationDire
    """
    
    # Get Current Username
    uname = getpass.getuser()

    # Move file from the target directory to the inputted destination
    shutil.move("C:/Users/" + str(uname) + "/" + str(TargetDir) + "/" + str(TargetFile), str(DestinationDire) + "/" + str(TargetFile))