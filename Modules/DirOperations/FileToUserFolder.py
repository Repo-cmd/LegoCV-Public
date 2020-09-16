import os
import shutil
import getpass


def FileToUserFolder(TargetDir, TargetFile, DestinationDire):

    """
    ** TargetDir: str of the directory from which to transfere the file ex: 'templates/example/test.docx'

    ** TargetFile: str of the file to be moved  ex: 'test.docx'

    ** DestinationDire: str of the directory to which the file will be transfered  ex: 'documents/example'

    Moves TargetFile from a TargetDir to DestinationDire in User folder
    """
    
    # Get Current Username
    uname = getpass.getuser()

    # Move file from the target directory to the inputted destination
    shutil.move( str(TargetDir) + "/" + str(TargetFile), "C:/Users/" + str(uname) + "/" + str(DestinationDire) + "/" + str(TargetFile))