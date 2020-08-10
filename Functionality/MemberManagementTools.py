# Section1: Member Statistics and Processed Details

#--End Of Section 1--
#Section2: Book Borrowing
def borrowbook(UserID, ListOfBookCodes):
    ProhibitedCharecters = ['', ' ']
    ColumnsNotNeeded = [1, 4] # Columns in the member details spreadsheet
    MemberDetails = []
    AllBookDetails = []
    if not UserID in ProhibitedCharecters:
        try:
            int(UserID)
        except ValueError:
            return [1, 'Only type in a number :(']
        UserID = int(UserID)
        from openpyxl import load_workbook
        AllMembersDetails = load_workbook("Spreadsheets\Members_deails.xlsx")
        Sheet = AllMembersDetails['Sheet1']
        for column in range(1, 7):
            if not column in ColumnsNotNeeded:
                cell = Sheet.cell(UserID + 1, column)
                MemberDetails.append(cell.value)
            else:
                pass
        #Prepare the borrowed book Details    
        import BookManagementTools
        for BookCode in ListOfBookCodes:
            BookDetails = BookManagementTools.FetchBookDetails(str(BookCode))
            AllBookDetails.append(BookDetails)

        # Empties textfile from last codes
        f = open('BasicProgramData\TemoraryStorage\BorrowerDetails.txt', 'r+')
        f.truncate(0)
        f.close()
        # Append details    
        with open("BasicProgramData\TemoraryStorage\BorrowerDetails.txt", 'w') as TempFile:
            for Detail in MemberDetails:
                TempFile.write(str(Detail) + ', ')

            for Book in AllBookDetails:
                TempFile.write(f'\n')
                for Detail in Book:
                    TempFile
    else:
        return [1, 'Please type in a integer! :(']

#--End Of Section 2--
borrowbook('1', ['M-FC/1', 'M-NF/1'])