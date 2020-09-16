import os

def TargetDirListFileType(Directory, FileExtension):
    """
    **Directory: a string of the directory to be searched (use full path name if in another folder)

    **FileExtension: a string of the files extension to search for

    searches Directory for a specific file extension

    P.S don't start with a backslash (/)

    EX: ('Documents/example', '.docx')
    """

    # List all the files in the directory and filter them
    DirFilesList = os.listdir(str(Directory))
    TargetFiles = []
    for file in DirFilesList:
        if file.endswith(FileExtension):
            TargetFiles.append(file)

    # returns the filtered list
    return TargetFiles