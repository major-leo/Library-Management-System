from database import getInfo, searchData, loanDays

def booksearch ():#searches for a book and returns a dictionary with the information
    book = input("Book Name")  # Todo to implement as a GUI and remove
    bookInfo = {}  # Todo to implement multiple book searches
    bookData = searchData(book,"database.txt","Title")
    if not bookData:
        return False
    bookInfo[book] = getInfo(bookData)
    bookInfo[book].append(["Loan: "])
    for id in range(1,len(bookInfo[book][0])):
        try:
            bookLog = searchData(bookInfo[book][0][id],"logfile.txt","ID")
            daysLoaned = loanDays(bookLog)
            if daysLoaned:
                bookInfo[book][-1].append(str(daysLoaned))
        except:
            pass
    return bookInfo

# Todo to make unit test to test this function and further comment on the function