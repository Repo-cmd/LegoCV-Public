def DataEntry(TempSchema):
    """
    ** TempSchema: dictionary of the model that will be filled


    takes a dictionary of a predifined schema and fill it based on it's data.
    retuns another Dictionary
    """
    # Declares the schema in use
    print("Processing template ",TempSchema["template Name"], " schema")

    # prints schema description
    print(TempSchema["description"])

    # create the output schema
    OutputModel = {
        'Paragraphs': {'PlaceHolders': [], 'Values': []},
        'Tables': {'MarkedForDuplication': {'Values':[], 'Reps': []}, 'PlaceHolders': [], 'Values': []}
    }

    # Intitiate the Entry process by reading each field of the inputed schema
    for Field in TempSchema['PlaceHolders']:

        # process Paragraph fields
        if Field['type'] == 'paragraph':
            ParagraphField = input('Please enter a value for ' + Field['value'] + ': ')
            OutputModel['Paragraphs']['PlaceHolders'].append(Field['value'])
            OutputModel['Paragraphs']['Values'].append(ParagraphField)
        
        # Process Table fields
        if Field['type'] == 'table':
            #Process repeatable fields
            if Field['repeatable'] == 'yes':
                # Process marked fields
                if Field['Marked'] == 'yes':
                    # start counting duplication rep
                    counter = 0
                    # get field value
                    while True:
                        markedField = input("Please enter value for marked field: ")
                        loopBreaker = ''
                        # check if another value will be added
                        while True:
                            print('add another value?')
                            ans = input('Please answer with y/n: ')
                            if ans == 'y':
                                loopBreaker = 'y'
                                counter = counter + 1
                                break
                            if ans == 'n':
                                loopBreaker = 'n'
                                break
                        # add the placeholder and it's value to the model
                        OutputModel['Tables']['PlaceHolders'].append(Field['value'])
                        OutputModel['Tables']['Values'].append(markedField)
                        # break loop and add the mark and it's rep to the model
                        if loopBreaker == 'n':
                            OutputModel['Tables']['MarkedForDuplication']['Values'].append(Field['value'])
                            OutputModel['Tables']['MarkedForDuplication']['Reps'].append(str(counter))
                            break
                # process repeated fields
                else:
                    while True:
                        repeatedField = input("Please enter value for repeated field: ")
                        loopBreaker = ''
                        # check if another value will be added
                        while True:
                            print('add another value?')
                            ans = input('Please answer with y/n: ')
                            if ans == 'y':
                                loopBreaker = 'y'
                                break
                            if ans == 'n':
                                loopBreaker = 'n'
                                break
                        # add the placeholder and it's value to the model
                        OutputModel['Tables']['PlaceHolders'].append(Field['value'])
                        OutputModel['Tables']['Values'].append(repeatedField)
                        # break loop and add the mark and it's rep to the model
                        if loopBreaker == 'n':
                            break
            # Process non repeated fields
            else:
                nonRepeatedField = input("Please enter value for non-repeated field: ")
                OutputModel['Tables']['PlaceHolders'].append(Field['value'])
                OutputModel['Tables']['Values'].append(nonRepeatedField)
    # returns the filled model
    print(OutputModel)
    return OutputModel

