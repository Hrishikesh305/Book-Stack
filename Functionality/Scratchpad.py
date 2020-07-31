def convert():
    number = 'gdfgsfdhah'
    print(number)
    try:
        int(number)
    except ValueError:
        return([1, 'Only type in a number :('])

    return(int(number) + 1)
print(convert())