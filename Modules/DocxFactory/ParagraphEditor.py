from docx import Document


def ParagraphEditor(TargetDocument, Keyword, Value, OutputFile):

    """
    **TargetDocument: str of the location and file name

    **Keyword: list of the keyword that will be replaced

    **Value: list of the desired value

    **OutputFile: str of the location and file name (replaces files with the same name)

    Searches in a document in a directory to replace all keywords with their equavalent values using the same style

    P.s. For Paragraphs only (free text not tables) and copies style only
    """
    document = Document(TargetDocument)
    # loop through each paragraph inside the target document (free text only)
    for paragraph in document.paragraphs:
        # loop in the list of Keywords
        for key in Keyword:
            # check the presence of the key
            if key in paragraph.text:
                x= paragraph.text
                # copies the current text style
                styleHolder = paragraph.style
                #replace the key with the value provided
                Y = x.replace(key , Value[Keyword.index(key)])
                paragraph.text = Y
                # apply the copied text
                paragraph.style = styleHolder
                #remove the values and the keys used
                Value.pop(Keyword.index(key))
                Keyword.pop(Keyword.index(key))
    # save the document in the provided directory with the provided name
    document.save(str(OutputFile))