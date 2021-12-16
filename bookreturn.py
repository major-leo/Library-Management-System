from database import searchData, loanDays,editData
from datetime import datetime
#written by: F126783


def bookreturn(ID):
    #updates the files with relevant infomation and alerts the user if the
    #book has been on loan for longer then 60 days
    try:
        bookID = searchData(ID,"database.txt","ID")[0]
        if not bookID:
            return 0
        if bookID[-1] == '0':
            return 1
    except:
        return 0
    memberBook = searchData(bookID[0],"logfile.txt","ID")
    editData("0",bookID,"database.txt")
    loan = loanDays(memberBook)
    editData(datetime.today().strftime('%d/%m/%Y'),memberBook[0],"logfile.txt")
    if loan > 60:
        return loan

#--------------------------------------Testing---------------------------------

def testing_bookreturn():
    #test that the files are actually updated with the correct information
    actual = bookreturn("27")
    expected = None
    assert actual == expected
    fCheck = open("database.txt","r")
    lines = fCheck.read().splitlines()
    assert lines[27][-1] == "0","should edit the txt file"
    fCheck.close()
    fCheck = open("logfile.txt", "r")
    lines = fCheck.read().splitlines()
    assert lines[-1][-10:] == datetime.today().strftime('%d/%m/%Y'),\
        "should edit the text file"
    fCheck.close()

def testing_invalid():
    #testing if id is not in the database
    actual = bookreturn("100")
    expected = False
    assert actual == expected, "should return false"

def testing_invalid_return():
    #testing if book is on loan
    actual = bookreturn("1")
    expected = False
    assert actual == expected, "should return false"

def testing_invalid_input():
    #testing id validity
    actual = bookreturn("abc")
    expected = False
    assert actual == expected, "should return false"

if __name__ == '__main__':
    #runs all the test
    testing_bookreturn()
    testing_invalid()
    testing_invalid_return()
    testing_invalid_input()
    print("All test passed")