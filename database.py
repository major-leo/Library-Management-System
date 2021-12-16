from datetime import datetime
#written by: F126783


def searchData(book,txt,column):
    # searches the text file and returns a 2D array of all the information
    f = open(txt,"r")
    columnTitles = getData(f.readline().strip("\n"))
    # finds the columns to compare to the headers we're searching for
    for eachColumn in columnTitles:
        if eachColumn.lower() == column.lower():
            column = columnTitles.index(eachColumn)
            break
    bookData = []
    for data in f:
        columnSub = getData(data.strip("\n"))[column]
        # finds the column that should be compared and compares
        if book.lower() == columnSub.lower():
            bookData.append(getData(data.strip("\n")))
    f.close()
    return bookData

def getData(bookData):
    # takes an array and returns an array of the cleaned data
    bookData = bookData.split('||')
    for data in range(len(bookData)):
        bookData[data] = bookData[data].strip(" ").strip('\t')
    return bookData

def getDate(date):
    # converts a string date to a datetime date
    dateArray = date.split("/")
    for date in range(len(dateArray)):
        if dateArray[date][0] == '0':
            dateArray[date] = dateArray[date][1]
        dateArray[date]=int(dateArray[date])
    return datetime(dateArray[2],dateArray[1],dateArray[0])


def loanDays(logInfo):
    # finds how long a book has been on loan for
    today = datetime.today()
    for log in logInfo:
        if log[3] == '0':
            return (today - getDate(log[2])).days
    return False

def editData(memberID,bookID,txt):
    # Edits the database so that the book is now shown to be borrowed
    # by a member
    f = open(txt,"r")
    replacementTxt = ""
    for line in f:
        if getData(line.strip("\n")) == bookID:
            line = line.strip("\n").split("||")
            line[-1] = memberID
            change = "||".join(line)+"\n"
            replacementTxt += change
        else:
            replacementTxt += line
    f.close()
    fWrite = open(txt,"w")
    fWrite.write(replacementTxt)
    fWrite.close()

def addLogs(memberID,bookID):
    # appends a new line to the logfile with the date and member id in
    # the correct format
    f = open("logfile.txt","a")
    headerSpace = {0:8,1:10,2:8}
    space = " "
    breaker = "||"
    line = bookID[0]+(headerSpace[0]-len(bookID[0]))*space+breaker+memberID+\
           headerSpace[1]*space+breaker\
           +datetime.today().strftime('%d/%m/%Y')+headerSpace[2]*space+\
           breaker+"0\n"
    f.write(line)
    f.close()

def getInfo(data):
    # returns a 2D array of the data with headers at point [0] of each array
    firstBook = data[0]
    dataArray = [["ID/s: "],["Genre: ",firstBook[1]],
                 ["Author/s: ",firstBook[3]]
        ,["Purchase Date: "],["Member ID: "]]
    for info in data:
        #appends the relevant information to the correct headers
        dataArray[0].append(info[0])
        dataArray[3].append(info[4])
        dataArray[4].append(info[5])
    return dataArray

#--------------------------------------Testing---------------------------------

def testing_getInfo():
    #testing if the getInfo function refactors the array correctly
    actual = getInfo([['1', 'Crime', 'The Suspect', 'Sarah Waters',
                       '12/04/1995', '0']])
    expected = [['ID/s: ', '1'], ['Genre: ', 'Crime'],['Author/s: ',
                                                       'Sarah Waters'],
                               ['Purchase Date: ', '12/04/1995'],
                ['Member ID: ', '0']]
    assert actual == expected ,"should refactor array inputed"

def testing_addlogs():
    #test the addLogs function to see if it updates the file accordingly
    #with the right information
    addLogs("abcd",["100"])
    fCheck = open("logfile.txt","r")
    lines = fCheck.read().splitlines()
    assert lines[-1] == "100     ||abcd          ||14/12/2021        " \
                        "||0", "should add a new log line"
    fCheck.close()

def testing_edit_data():
    #test to see if the edit data function changes the files accurately
    editData("0",['2', 'Sci-Fi', 'Watchmen', 'Alan Moore', '07/11/2008',
                  'trte'],"database.txt")
    fCheck = open("database.txt","r")
    lines = fCheck.read().splitlines()
    assert lines[2][-1] == "0" , "should edit file to change id to the new one"
    fCheck.close()

def testing_loandays():
    #tests to see if loan days can filter through a list and return the
    #correct amount of days said book has been on loan for
    actual = loanDays([['15', 'esno', '15/06/2020', '20/09/2020'],
                       ['15', 'orat', '01/12/2021', '0'],
                       ['15', 'jvrc', '17/07/2019', '16/09/2020'],
                       ['15', 'bnsr       ', '19/08/2019', '23/09/2021']])
    expected = (datetime.today() - datetime(2021,12,1)).days
    assert actual == expected, "should return the amount days the current " \
                               "book has been one loan for"

def testing_getDate():
    #test to see if function converts a string to date type
    actual = getDate(datetime.today().strftime('%d/%m/%Y'))
    expected = datetime.today().date()
    assert actual.date() == expected, "should return date in a datetime format"

def testing_getData():
    #test to see if the data is stripped correctly and turned into an array
    actual = getData("47      ||Classics  ||Atlas Shrugged            "
                     "||Ayn Rand||27/04/2019        ||0")
    expected = ['47', 'Classics', 'Atlas Shrugged', 'Ayn Rand',
                '27/04/2019', '0']
    assert actual == expected, "should reformat the string into a" \
                               " list stripe of white space"

def testing_seachdata():
    #test to see if the search data returns the right line reformated
    actual = searchData("2","database.txt","ID")
    expected = [['2', 'Sci-Fi', 'Watchmen', 'Alan Moore', '07/11/2008',
                 'trte']]
    assert actual == expected, "should return 2D array of line searched for"


if __name__ == "__main__":
    #runs the all the test
    testing_seachdata()
    testing_getData()
    testing_getDate()
    testing_loandays()
    testing_edit_data()
    testing_addlogs()
    testing_getInfo()
    print("All test passed")