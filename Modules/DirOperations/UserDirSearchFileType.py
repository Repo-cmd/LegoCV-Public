import os
import getpass

def UserDirSearchFileType(Directory, FileExtension):
    """
    **Directory: a string of the directory to be checked and created if not found

    **FileExtension: a string of the files extension to search for

    Checks for the presence of a directory in the Current user folder and creates one if none was found then searches it
    for a specific file extension

    P.S don't start with a backslash (/)

    EX: ('Documents/example', '.docx')
    """

    # Get current user name
    uname = getpass.getuser()

    # Check the existance of the directory
    if os.path.isdir("C:/Users/" + str(uname) + "/" + str(Directory)):
        print('Directory found')
    else:
        os.mkdir("C:/Users/" + str(uname) + "/" + str(Directory))
        print('Directory created successfully')

    # Check if the user is ready for the scan
    while True:
        userInput = input('ready for a scan, y?')
        if str(userInput) == 'y':
            break
    
    # List all the files in the directory and filter them
    DirFilesList = os.listdir("C:/Users/" + str(uname) + "/" + str(Directory))
    TargetFiles = []
    for file in DirFilesList:
        if file.endswith(FileExtension):
            TargetFiles.append(file)

    # print the number of files found with the provided extension
    print(str(len(TargetFiles)) + ' found')

    # returns the filtered list
    return TargetFiles