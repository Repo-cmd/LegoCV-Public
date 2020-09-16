from Modules.DirOperations.UserDirChecker import UserDirChecker
from Modules.Menus.DynamicListedMenu import DynamicListedMenu
from Modules.DirOperations.UserDirSearchFileType import UserDirSearchFileType
from Modules.DirOperations.JsonCreator import CreateJson
from Modules.Modeler.ModelCreator import ModelCreator
from Modules.DirOperations.MoveFiles import MoveFiles
from Modules.DirOperations.DeleteFile import DeleteFile
from Modules.DirOperations.TargetDirListFileType import TargetDirListFileType
from Modules.Viewer.GlobalViewer import GlobalViewer
from Modules.DirOperations.ReadJson import ReadJson
from Modules.DataEntry.FillModel import DataEntry
from Modules.DocxFactory.ParagraphEditor import ParagraphEditor
from Modules.DocxFactory.TableDuplicator import TableDuplicator
from Modules.DocxFactory.TableEditor import TableEditor
from Modules.DirOperations.FileToUserFolder import FileToUserFolder

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Main menu <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def MainRoute():
    
    # checks for the app folder and subfolders in Documents folder
    print("""                                                  
                       mm-               .odMNmmmMNds      /md`        `dm:                         
                       MM:              sMN+`     .+d`      hMy        yMy                          
                       MM:             sMm`                 `NM/      /Mm`                          
                       MM:             NM+                   :MN.    .NM-                           
                       MM:            `MM:                    sMd    dMo                            
                       MM:             mMs                     dMo  oMh                             
                       MM:             -NMo         :          .NM:-MN`                             
                       MMs+++++++/      .hMNs+/:/oyNM`          /MNmM:                                 
    """)
    print('Checking Important folders...')

    UserDirChecker(['Documents/LegoCv', 'Documents/LegoCv/Result', 'Documents/LegoCv/New Templates'])

    print('Done ^_^')
    # print the menu items
    DynamicListedMenu(['Model space', 'Create C.V.'],[ModelsRoute, CreateCV])


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Model routes <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def ModelsRoute():
    # Displays the Modeler routes menu
    DynamicListedMenu(['Create Model', 'Delete Model', 'View Model'], [CreateModel, DeleteModel, ViewModel])


def CreateModel():
    # Creating model route

    print("""
        The app will Create the new templates folder for you once it's done please add all you word templates
        in the folder and confirm to continue
    """)
    # process the files in the documents folder
    for File in UserDirSearchFileType('Documents/LegoCv/New Templates', '.docx'):
        CreateJson('Templates/', File.replace('.docx',''), ModelCreator(File))
        MoveFiles('Documents/LegoCv/New Templates', File, 'Templates')
        print("""
           *** TEMPLATE ADDED SUCCESSFULLY ^_^ ***
        """)

def DeleteModel():

    # read templates folder to list available models
    for File in TargetDirListFileType('Templates/', '.docx'):
        print(TargetDirListFileType('Templates/', '.docx').index(File), '-', str(File.replace('.docx', '')))

    # validate user choice
    while True:
        try:
            ChosenItem = int(input('choose item: '))
            if ChosenItem >= 0 and ChosenItem <= len(TargetDirListFileType('Templates/', '.docx')) - 1:
                break
        except:
            print('Enter a Valid Item from the List')
    
    # confirm deletion
    print("Are you you want to delete this Model? (Doing so will delete the template with it)")

    while True:
        ans = input('Please answer with y/n: ')
        if ans == 'n':
            break
        # delete model with temp
        if ans == 'y':
            DeleteFile('Templates/' + str(TargetDirListFileType('Templates/', '.docx')[ChosenItem].replace('.docx', '.json')))
            DeleteFile('Templates/' + str(TargetDirListFileType('Templates/', '.docx')[ChosenItem]))
            print("""
                *** REMOVED SUCCESSFULLY ***          
            """)
            break
        print('Please ente a valid answer')



def ViewModel():

    # Read templates folder dir and list contained models
    if len(TargetDirListFileType('Templates/', '.json')) > 0:
        for File in TargetDirListFileType('Templates/', '.json'):
            print(TargetDirListFileType('Templates/', '.json').index(File), '-', str(File.replace('.json', '')))
        # validate user choice
        while True:
            try:
                ChosenItem = int(input('choose item: '))
                if ChosenItem >= 0 and ChosenItem <= len(TargetDirListFileType('Templates/', '.json')) - 1:
                    break
            except:
                print('Enter a Valid Item from the List')
        # Display selected Model
        GlobalViewer(ReadJson('Templates/', TargetDirListFileType('Templates/', '.json')[ChosenItem].replace('.json', '')))
    # if no models were found
    else:
        print("""
            *** No Models to View ***
        """)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> C.V. routes <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def CreateCV():

    if len(TargetDirListFileType('Templates/', '.json')) > 0:
        print("""
                >>> Choose template to Use <<<
        """)
        # list all templates
        for File in TargetDirListFileType('Templates/', '.json'):
            print(TargetDirListFileType('Templates/', '.json').index(File), '-', str(File.replace('.json', '')))
        
        # get user choice
        while True:
            try:
                ChosenItem = int(input('choose item: '))
                if ChosenItem >= 0 and ChosenItem <= len(TargetDirListFileType('Templates/', '.json')) - 1:
                    break
            except:
                print('Enter a Valid Item from the List')
        
        SelectedModel = TargetDirListFileType('Templates/', '.json')[ChosenItem]
        # fill selected model
        ReadyData = DataEntry(ReadJson('Templates/', SelectedModel.replace('.json', '')))
        
        # view filled data
        GlobalViewer(ReadyData)
        print('Please Confirm Processing these data')
        print(ReadyData)
        # confirm on creating the output
        while True:

            userChoice = input('Answer with y/n: ')
            
            # return if the answer is no
            if userChoice == 'n':
                break
            
            # process data if the answer is yes
            if userChoice == 'y':
                # duplicate tables if found
                TableDuplicator('Templates/' + str(SelectedModel.replace('.json', '.docx')), ReadyData['Tables']['MarkedForDuplication']['Reps'], 'Templates/Temp/' +  str(SelectedModel.replace('.json', '.docx')), ReadyData['Tables']['MarkedForDuplication']['Values'])
                # fill  tables
                TableEditor('Templates/Temp/' +  str(SelectedModel.replace('.json', '.docx')), ReadyData['Tables']['PlaceHolders'], ReadyData['Tables']['Values'], 'Templates/Temp/' +  str(SelectedModel.replace('.json', '.docx')))
                # fill paragraphs
                ParagraphEditor('Templates/Temp/' +  str(SelectedModel.replace('.json', '.docx')), ReadyData['Paragraphs']['PlaceHolders'], ReadyData['Paragraphs']['Values'], 'Templates/Temp/' +  str(SelectedModel.replace('.json', '.docx')))
                # move output to user folder
                FileToUserFolder('Templates/Temp/' , str(SelectedModel.replace('.json', '.docx')), 'Documents/LegoCv/result/')
                # exit menu
                print("""
                    *** File Created Successfully ^_^ ***
                """)
                break
    # If No Models were found
    else:
        print("""
            *** No Templates to Use ***
        """)