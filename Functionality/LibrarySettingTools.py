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

def GetCategoryFullForms():
    CategoryNames = {}
    with open("BasicProgramData/LibraryCategories.txt") as LCategories:
        for line in LLanguage:
            #line is "CategoryAbbriviation/CategoryFullForm"
            if "/" in line:
                line = line.split("/")
                CategoryNames[line[0]] = line[1]
            else:
                pass
    return CategoryNames
# -- end of section 1 --