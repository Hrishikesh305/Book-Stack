def GetSpreadsheetDetails():
    SpreadsheetAdresses = {}
    with open("TextData/LibraryLanguages.txt") as LLanguage:
        for line in LLanguage:
            #line is "language/spreadsheetAdress.xlsx"
            if "/" in line and ".xlsx" in line:
                line = line.split("/")
                SpreadsheetAdresses[line[0]] = line[1]
            else:
                pass
    return SpreadsheetAdresses



