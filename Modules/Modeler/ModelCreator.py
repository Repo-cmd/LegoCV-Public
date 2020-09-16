def ModelCreator(TemplateName):
    """
    **TemplateName: string with the file name (ex. test.docx)

    Takes a docx file name to create dictionary model for it (P.s. predefined)
    """

    # model Dictionary for template
    Template = {
    "template Name": "",
    "description" : "",
    "PlaceHolders": []
    }
    # name the template from the docx file
    JsonName = TemplateName.replace(".docx", "")
    # add the name to the template
    Template['template Name'] = JsonName
    # starting the modelling process
    print('started Modelling process for template ' + str(Template['template Name']))
    # get template description 
    TempDescription = input('Please enter a template description: ')
    # add the description to the template
    Template['description'] = TempDescription
    # placeholders inputting process
    while True:
        # placeHolders temp field
        tempField = {'type':'', 'value':''}
        
        # select the field type
        print("1 - Paragraph")
        print("2 - Table")
        Fieldtype = input('Please input placeholder type: ')
       
        # esnure the entered choice exists
        while Fieldtype != '1' and Fieldtype != '2':
            print('invalid option')
            Fieldtype = input('Please input placeholder type: ')
        
        # input field value
        print('Please input placeholder value')
        val = input('value: ')
        tempField['value'] = val

        # apply field type for paragraph
        if str(Fieldtype) == '1':
            tempField['type'] = 'paragraph'
        
        # apply field type for table and chek if it was repeatable or not
        if str(Fieldtype) == '2':
            tempField['type'] = 'table'
            print('Is this field repeatable?')
            while True:
                ans = input('please answer with y/n: ')
                if str(ans) == "y":
                    tempField['repeatable'] = 'yes'
                    # check if this field marked for table repetition
                    print('Is this field Marked?')
                    while True:
                        markstat = input('please answer with y/n: ')
                        if str(markstat) == 'y':
                            tempField['Marked'] = 'yes'
                            break
                        else:
                            if str(markstat) == 'n':
                                tempField['Marked'] = 'no'
                                break
                    break
                else:
                    if str(ans) == "n":
                        tempField['repeatable'] = 'no'
                        break
        
        # add the tempfield to the main template Dictionary
        Template['PlaceHolders'].append(tempField)
        
        # check if the user will add another field
        print('Add another field?')
        ans = input('please answer with (y) to add or enter to exit: ')
        if str(ans) == "y":
            print('')
        else:
            break
    
    # return the dictionary
    return Template