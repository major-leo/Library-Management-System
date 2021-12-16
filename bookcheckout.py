from database import searchData, editData, addLogs, loanDays, getInfo
from datetime import datetime
#written by: F126783

def bookcheckout(memberID,ID):
    #updated files and returns infomations on books loaned for longer than
    # 60 days
    overDue = {memberID:[]}
    if not memberID.isalpha() or len(memberID) != 4:
    #checking validity
        return 0
    bookID = False
    try:
        bookID = searchData(ID,"database.txt","ID")[0]
        if bookID[-1] != '0':
            return 1
    except:
        pass
    if not bookID:
        return 2
    editData(memberID,bookID,"database.txt")
    addLogs(memberID,bookID)
    memberLoans = searchData(memberID,"logfile.txt","Member ID")
    daysLoaned = loanDays(memberLoans)
    eachBook = 0
    while daysLoaned and eachBook < len(memberLoans):
    #finds all the books that are on loan for longer then 60 days and
    #appends them to the dictionary wiht the member id as the key
        if memberLoans[eachBook][3] == '0'and daysLoaned > 60:
            book = searchData(memberLoans.pop(eachBook)[0],"database.txt","ID")
            bookName = book[0][2]
            book = getInfo(book)
            del book[-1]
            book.append(["Book Name: ",bookName])
            overDue[memberID].append(book)
            daysLoaned = loanDays(memberLoans)
            eachBook -= 1
        eachBook += 1
    return overDue


#--------------------------------------Testing---------------------------------
def test_bookcheckout():
    #test that when a valid input is entered
    # the file is actually edited with the correct information
    actual = bookcheckout(memberID="bnsr",ID="27")
    expected= {"bnsr":[]}
    fCheck = open("database.txt","r")
    lines = fCheck.read().splitlines()
    assert lines[27][-4:] == "bnsr","should edit the txt file"
    fCheck.close()
    fCheck = open("logfile.txt","r")
    lines = fCheck.read().splitlines()
    assert lines[-1] == "27      ||bnsr          ||"+\
           datetime.today().strftime('%d/%m/%Y')+"        ||0",\
        "most recent line should be edited"
    fCheck.close()
    assert actual == expected ,"should edit the files and return a " \
                           "dictionary with member as key and an empty list"

def test_invalid_member():
    #checks the validity of member ID
    actual = bookcheckout(memberID="1234",ID="27")
    expected = False
    assert actual == expected , "should return False as members are " \
                                "not letters"

def test_invalid_member_len():
    #further checking validity
    actual = bookcheckout(memberID="abc",ID="27")
    expected = False
    assert actual == expected , "should return False as members is the not " \
                                "the right length"

def test_invalid_ID():
    #checks the validity of ID
    actual = bookcheckout(memberID="bnsr",ID="100")
    expected = False
    assert actual == expected , "should return False as book id " \
                                "100 doesn't exist"

def test_avalible():
    #check if the book is
    # available
    actual = bookcheckout(memberID="bnsr",ID="2")
    expected = False
    assert actual == expected , "should return False as book is " \
                                "already on loan"


if __name__ == '__main__':
    #runs the tests
    test_bookcheckout()
    test_invalid_member()
    test_invalid_member_len()
    test_invalid_ID()
    test_avalible()
    print("All Test Passed")
