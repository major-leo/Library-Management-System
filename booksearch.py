
from database import searchData
from database import loanDays

def getInfo(data): # returns a 2D array of the data with headers at point [0] of each array
    firstBook = data[0]
    dataArray = [["ID/s:"],["Genre:",firstBook[1]],["Author/s:",firstBook[3]] # Todo to optimise this function to work for both data base and logfile
        ,["Purchase Date:"],["Member ID:"]]
    for info in data:
        dataArray[0].append(info[0])
        dataArray[3].append(info[4])
        dataArray[4].append(info[5])
    return dataArray


def booksearch ():#searches for a book and returns a dictionary with the information
    book = input("Book Name")  # Todo to implement as a GUI and remove
    bookInfo = {}  # Todo to implement multiple book searches
    bookData = searchData(book,"database.txt","Title")
    if not bookData:
        return False
    bookInfo[book] = getInfo(bookData)
    bookInfo[book].append(["Loan:"])
    for id in range(1,len(bookInfo[book][0])):
        try:
            bookLog = searchData(bookInfo[book][0][id],"logfile.txt","ID")
            daysLoaned = loanDays(bookLog)
            if daysLoaned:
                bookInfo[book][-1].append(str(daysLoaned))
        except:
            return bookInfo
    return bookInfo

# Todo to make unit test to test this function and further comment on the function