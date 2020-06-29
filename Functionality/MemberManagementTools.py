# Section1: Member Statistics and Processed Details
def FindOverdueBooks():
    from openpyxl import load_workbook
    import datetime
    borrowed_book_details = []
    Borrowed_Books_Data = load_workbook("Borrowed_books.xlsx")
    DataSheet = Borrowed_Books_Data['DataSheet']
    for row in range(2, DataSheet.max_row + 1):
        returned = DataSheet.cell(row=row, column=6).value
        if not returned:
            R_Date = DataSheet.cell(row=row, column=3).value
            R_Month = DataSheet.cell(row=row, column=4).value
            R_Year = DataSheet.cell(row=row, column=5).value
            Original_Return_Date = datetime.date(R_Year, R_Month, R_Date)
            today = datetime.date.today()
            print(today)
            time_left_for_return = Original_Return_Date - today
            if time_left_for_return.days <= 0:
                Book_Details = []
                for column in range(1, 3):
                    Book_Details.append(DataSheet.cell(row=row, column=column).value)
                borrowed_book_details.append(Book_Details)
    print(borrowed_book_details)
#--End Of Section 1--