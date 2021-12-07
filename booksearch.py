from datetime import datetime

def getInfo(data): # returns a 2D array of the data with headers at point [0] of each array
    firstBook = data[0]
    dataArray = [["ID/s:"],["Genre:",firstBook[1]],["Author/s:",firstBook[3]] # Todo to optimise this function to work for both data base and logfile
        ,["Purchase Date:"],["Member ID:"]]
    for info in data:
        dataArray[0].append(info[0])
        dataArray[3].append(info[4])
        dataArray[4].append(info[5])
    return dataArray


def searchData(book,txt,column):  # searches the text file and returns a 2D array of all the information
    f = open(txt,"r")
    columnTitles = getData(f.readline().strip("\n"))  # finds the columns to compare to the headers we're searching for
    for eachColumn in columnTitles:
        if eachColumn.lower() == column.lower():
            column = columnTitles.index(eachColumn)
            break
    bookData = []
    for data in f:
        columnSub = getData(data.strip("\n"))[column]  # finds the column that should be compared and compares
        if book.lower() == columnSub.lower():
            bookData.append(getData(data.strip("\n")))
    f.close()
    return bookData


def getData(bookData):  # takes an array and returns an array of the cleaned data
    bookData = bookData.split('||')
    for data in range(len(bookData)):
        bookData[data] = bookData[data].strip(" ")
    return bookData

def getDate(date):  # converts a string date to a datetime date
    dateArray = date.split("/")
    for date in range(len(dateArray)):
        if dateArray[date][0] == '0':
            dateArray[date] = dateArray[date][1]
        dateArray[date]=int(dateArray[date])
    return datetime(dateArray[2],dateArray[1],dateArray[0])


def loanDays(logInfo):  # finds how long a book has been on loan for
    today = datetime.today()
    for log in logInfo:
        if log[3] == '0':
            return (today - getDate(log[2])).days
        else:
            return False

def booksearch ():#searches for a book and returns a dictionary with the information
    book = input("Book Name")  # Todo to implement as a GUI and remove
    bookInfo = {}  # Todo to implement multiple book searches
    bookData = searchData(book,"database.txt","Title")
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