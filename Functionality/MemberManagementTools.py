# Section1: Member Statistics and Processed Details

#--End Of Section 1--
#Section2: Book Borrowing
def borrowbook(UserID, ListOfBookCodes):
    ProhibitedCharecters = ['', ' ']
    ColumnsNotNeeded = [1, 4] # Columns in the member details spreadsheet
    MemberDetails = []
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
                cell = Sheet.cell(UserID, column)
                MemberDetails.append(cell.value)
            else:
                pass
    else:
        return [1, 'Please type in a integer! :(']

#--End Of Section 2--
borrowbook('1', [1,2,3])