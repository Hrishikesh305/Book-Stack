# Section1: Member Statistics and Processed Details

#--End Of Section 1--
#Section2: Book Borrowing
def borrowbook(UserID, ListOfBookCodes):
    ProhibitedCharecters = ['', ' ']
    if not UserID in ProhibitedCharecters:
        try:
            int(UserID)
        except ValueError:
            return [1, 'Only type in a number :(']
        UserID = int(UserID)
#--End Of Section 2--