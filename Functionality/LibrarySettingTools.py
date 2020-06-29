# Section 1: Language and catagory tools 
def GetLanguageSpreadsheetAdresses():
    SpreadsheetAdresses = {}
    with open("BasicProgramData/LibraryLanguages.txt") as LLanguage:
        for line in LLanguage:
            #line is "language/spreadsheetAdress.xlsx"
            if "/" in line and ".xlsx" in line:
                line = line.split("/")
                SpreadsheetAdresses[line[0]] = line[1]
            else:
                pass
    return SpreadsheetAdresses
# -- end of section 1 --



