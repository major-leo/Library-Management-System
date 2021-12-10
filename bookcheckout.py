from database import searchData, editData, addLogs, loanDays, getInfo

def bookcheckout():
    memberID = input("member ID: ")  # Todo to make gui and create error boxes for specific errors
    overDue = {memberID:[]}
    if not memberID.isalpha() or len(memberID) != 4:
        return False
    bookID = searchData(input("book ID: "),"database.txt","ID")[0]
    if not bookID:
        return False
    if bookID[-1] != '0':
        return False
    editData(memberID,bookID,"database.txt")
    addLogs(memberID,bookID)
    memberLoans = searchData(memberID,"logfile.txt","Member ID")
    daysLoaned = loanDays(memberLoans)
    eachBook = 0
    if daysLoaned:
        while eachBook < len(memberLoans):
            if memberLoans[eachBook][3] == '0':
                book = searchData(memberLoans.pop(eachBook)[0],"database.txt","ID")
                book = getInfo(book)
                del book[-1]
                overDue[memberID].append(" ".join(["".join(x) for x in book]))
                eachBook -= 1
            eachBook += 1
    return overDue

#todo to optimise and to further commemnt