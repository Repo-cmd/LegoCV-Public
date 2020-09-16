import os
import getpass

def UserDirChecker(Directory):
    """
    **Directory: a list of directories to be checked and created if not found

    Checks for the presence of a directory in the Current user folder and creates one if none was found

    P.S don't start with a backslash (/)

    EX: Documents/example
    """

    # Get Current Username
    uname = getpass.getuser()

    # Loop in the inputted list
    for Dir in Directory:
        # Check if it exists
        if os.path.isdir("C:/Users/" + str(uname) + "/" + str(Dir)):
            print('Directory found')
        else:
            # Create the provided Location
            os.mkdir("C:/Users/" + str(uname) + "/" + str(Dir))
            print('Directory created successfully')