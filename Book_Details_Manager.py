def insert_book(BookName, Price, Author, Publisher, MadeFor, Language, Catagory):

    def CodeMaker(Languages_abbreviations, Category_abbreviations, Language, Category, Spreadsheet):
        from openpyxl import load_workbook
        if Language in Languages_abbreviations and Category in Category_abbreviations:
            current_workbook = load_workbook(Spreadsheet)
            current_worksheet = current_workbook[Category]
            last_occupied_row = current_worksheet.max_row
            id_number = last_occupied_row + 1
            Language_ab = Languages_abbreviations[Language]
            Category_ab = Category_abbreviations[Category]
            Code = f'{Language_ab}-{Category_ab}/{id_number}'
            return Code
        else:
            return 1

    prohibited = ['', ' ']
    Languages_abbreviations = {'English': 'E', 'Malayalam': 'M', 'Hindi': 'H'}
    Spreadsheet_addresses = {'M': 'Malayalam_books.xlsx', 'E': 'English_books.xlsx', 'H': 'Hindi_books.xlsx'}
    Category_abbreviations = {'Fiction': 'FC', 'NonFiction': 'NF', 'SelfHelp': 'SF', 'Magazine': 'MG'}

    if BookName not in prohibited and Author not in prohibited and Publisher not in prohibited:
        if Catagory.lower() != 'select' and Language != 'select':
            if Language in Languages_abbreviations and Catagory in Category_abbreviations:
                from openpyxl import load_workbook
                workbook = load_workbook(Spreadsheet_addresses[Languages_abbreviations[Language]])
                worksheet = workbook[Catagory]
                BookDetails = [BookName, Price,
                               CodeMaker(Languages_abbreviations, Category_abbreviations, Language,
                                         Catagory, Spreadsheet_addresses[Languages_abbreviations[Language]]), Author,
                               Publisher, MadeFor]
                if not BookDetails[2] == 1:
                    worksheet.append(BookDetails)
                    print(BookDetails)
                else:
                    return 1
            else:
                return 1
        else:
            return 1
    else:
        return 1
