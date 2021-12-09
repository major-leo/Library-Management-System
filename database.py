from datetime import datetime

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

def editData(memberID,bookID):  # Edits the database so that the book is now shown to be borrowed by a member
    f = open("database.txt","r")  # Todo to make it edit both txt files
    replacementTxt = ""
    for line in f:
        if getData(line.strip("\n")) == bookID:
            line = list(line.strip("\n"))
            line[-1] = memberID
            change = "".join(line)+"\n"
            replacementTxt += change
        else:
            replacementTxt += line
    f.close()
    fWrite = open("database.txt","w")
    fWrite.write(replacementTxt)
    fWrite.close()

def addLogs(memberID,bookID):  # appends a new line to the logfile with the date and member id in the correct format
    f = open("logfile.txt","a")
    headerSpace = {0:8,1:10,2:8}
    space = " "
    breaker = "||"
    line = bookID[0]+(headerSpace[0]-len(bookID[0]))*space+breaker+memberID+headerSpace[1]*space+breaker\
           +datetime.today().strftime('%d/%m/%Y')+headerSpace[2]*space+breaker+"0\n"
    f.write(line)
    f.close()


