def DynamicListedMenu(MenuListItems, FunctionsList):
    """
    MenuListItems: List , FunctionsList: List

    Add a list of menu items followed by a list of functions to display a menu with numbered selections 
    """

    # add exit menu  option to the menu list at the end of the list
    MenuListItems.insert(len(MenuListItems), 'Exit Menu')

    # add a dummy function in the dunction list
    FunctionsList.insert(len(FunctionsList), 'pass')

    # print the menu with numbers based on the item index in the input List
    for item in MenuListItems:
        print('['+ str(MenuListItems.index(item)) + ']' + ' ' + str(item))
    # infinit loop until user chooses a valid item in the list
    while True:
        try:
            SelectedItemNumber = int(input('choose item: '))
            if SelectedItemNumber >= 0 and SelectedItemNumber <= len(MenuListItems) - 1:
                break
        except:
            print('Enter a Valid Item from the List')
    # run the function from the inputed FunctionsList based on the parallel 
    # item selected from the list of the menu items or exits menu
    if SelectedItemNumber == MenuListItems.index('Exit Menu'):
        pass
    else:
        FunctionsList[SelectedItemNumber]()