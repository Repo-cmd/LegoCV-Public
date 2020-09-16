from terminaltables import DoubleTable

def GlobalViewer(TargetDict):

    """
    ** TargetDict: Dictionary of a model or entered data


    Takes Dicationary and recognize it's type (Model or Data) based on Keys and display the data in terminal tables
    """
    
    # Check if the Dict is Model based on value Key
    if 'template Name' in TargetDict.keys():

        # Create Tbale fields data set
        TableData = [
            ['Value', 'Repeatable', 'Marked']
        ]

        # create Paragraphs fields data set
        ParagraphData = [
            ['Value'],
        ]

        # Loop through fields
        for Field in TargetDict['PlaceHolders']:

            # check if the field is table
            if 'repeatable' in Field.keys():

                # add field content to the table data set
                TableData.append([Field['value'], Field['repeatable'],Field['Marked']])

            # otherwise treat as a paragraph field
            else:
                # add paragraph field content to the paragraph data set
                ParagraphData.append([Field['value']])

        # Create Metadata dataSet
        DictMeta = [
            ['Template Name', (TargetDict['template Name'])],
            ['Description', TargetDict['description']],
            ['Table fields', len(TableData)-1],
            ['Paragraph Fields', len(ParagraphData)-1]
        ]

        # Create main table object
        MainTable = DoubleTable(DictMeta, " Model Meta-Data ")
        MainTable.justify_columns[0] = 'center'
        MainTable.inner_row_border = True

        # Create TableFields table object
        TableFields = DoubleTable(TableData, " Table Fields ")
        TableFields.justify_columns[0] = 'center'
        TableFields.inner_heading_row_border = True

        # Create ParagraphFields table object
        ParagraphFields = DoubleTable(ParagraphData, " Paragraph Fields ")
        ParagraphFields.justify_columns[0] = 'center'
        ParagraphFields.inner_heading_row_border = True

        # Print tables
        print(MainTable.table)
        print(TableFields.table)
        print(ParagraphFields.table)

    # Treat Dict as a Data
    else:

        # Copy paragraph lists data
        CopiedParaPlaceHolders = [ item for item in TargetDict['Paragraphs']['PlaceHolders'] ]
        CopiedParaValues = [ item for item in TargetDict['Paragraphs']['Values'] ]
        
        # create paragraph fields data set
        paraData= []
        for _ in range(len(CopiedParaPlaceHolders)):
            paraData.append([CopiedParaPlaceHolders[0], CopiedParaValues[0]])
            CopiedParaPlaceHolders.pop(0)
            CopiedParaValues.pop(0)
        # add headers
        paraData.insert(0, ['PlaceHolder', 'Value'])

        # copy table lists data
        CopiedTablePlaceHolders = [ item for item in TargetDict['Tables']['PlaceHolders'] ]
        CopiedTableValues = [ item for item in TargetDict['Tables']['Values'] ]
        # create table fields data set
        tabData = []
        for _ in range(len(CopiedTablePlaceHolders)):
            tabData.append([ CopiedTablePlaceHolders[0], CopiedTableValues[0] ])
            CopiedTablePlaceHolders.pop(0)
            CopiedTableValues.pop(0)
        # add headers
        tabData.insert(0, ['PlaceHolder', 'Value'])

        # create duplication data set
        DupliData = [[item, 
        TargetDict['Tables']['MarkedForDuplication']['Reps'][TargetDict['Tables']['MarkedForDuplication']['Values'].index(item)]
        ] for item in TargetDict['Tables']['MarkedForDuplication']['Values']
        ]
        DupliData.insert(0, ['Mark', 'Repetition'])

        # create paragraph fields table
        ParagraphTable = DoubleTable(paraData, ' Paragraph Fields ')
        ParagraphTable.justify_columns[0] = 'center'
        ParagraphTable.inner_heading_row_border = True

        # create table fields table
        TabelTable = DoubleTable(tabData, ' Table fields ')
        TabelTable.justify_columns[0] = 'center'
        TabelTable.inner_heading_row_border = True

        # Create duplication table
        DupliTable = DoubleTable( DupliData, ' Repetitions ')
        DupliTable.justify_columns[0] = 'center'
        DupliTable.inner_heading_row_border = True

        # print tables
        print(ParagraphTable.table)
        print(TabelTable.table)
        print(DupliTable.table)
