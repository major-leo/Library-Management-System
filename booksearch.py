from database import getInfo, searchData, loanDays

def booksearch (book):
    #searches for a book and returns a dictionary with the information
    bookInfo = {}
    bookData = searchData(book,"database.txt","Title")
    if not bookData:
        return False
    bookInfo[book] = getInfo(bookData)
    bookInfo[book].append(["Loan: "])
    for id in range(1,len(bookInfo[book][0])):
        #for each book checks the loan days if book is being loaned out
        #appends to the dictionary if it's over 60 days
        try:
            bookLog = searchData(bookInfo[book][0][id],"logfile.txt","ID")
            daysLoaned = loanDays(bookLog)
            if daysLoaned:
                if daysLoaned > 60:
                    bookInfo[book][-1].append(str(daysLoaned))
                else:
                    bookInfo[book].remove(["Loan: "])
                    #removes loan list if ther are no loans over 60 days
            else:
                bookInfo[book].remove(["Loan: "])
                #removes loans list if there are no loans
        except:
            pass
    return bookInfo

#--------------------------------------Testing---------------------------------

def test_booksearch():
    #creates a test to check if the booksearch returns the right
    # result give an input
    actual = booksearch(book="The Suspect")
    expected ={'The Suspect': [['ID/s: ', '1'], ['Genre: ', 'Crime'],
                               ['Author/s: ', 'Sarah Waters'],
                               ['Purchase Date: ', '12/04/1995'],
                               ['Member ID: ', '0']]}
    assert actual == expected, "should return a list with correct info"

def test_booksearch_Loan():
    #testing that amount of days the book has been on loan is
    # returned if necessary
    actual = booksearch(book="Watchmen")["Watchmen"]
    expected = ['Loan: ', '233']
    assert expected in actual, "should return loan days amount"

def test_booksearch_loan2():
    #testing that loan is not in if not necessary
    actual = booksearch(book="The Road")["The Road"]
    expected = ['Loan: ']
    assert expected not in actual, "should not have loan list as book loan \
    is less then 60 days"

def test_notInDB():
    #testing invalid input
    actual = booksearch(book="batman vs superman")
    expected = False
    assert actual == expected, "should return False"

def test_booksearch_Multi():
    #testing multiple books with the same name
    actual = booksearch(book="Cold Waters")
    expected ={'Cold Waters': [['ID/s: ', '8', '41'], ['Genre: ', 'Thriller'],
                            ['Author/s: ', 'Debbie Herbert'],
                            ['Purchase Date: ', '17/12/2011', '25/02/2021'],
                            ['Member ID: ', 'thgg', '0'],
                            ['Loan: ', '592']]}
    assert actual == expected, "should have multiple IDs and member Ids"


if __name__=='__main__':
    #runs the test
    test_notInDB()
    test_booksearch()
    test_booksearch_loan2()
    test_booksearch_Loan()
    test_booksearch_Multi()
    print("All Test Passed")
