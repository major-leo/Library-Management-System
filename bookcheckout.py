from database import searchData
from database import editData
from database import addLogs


def bookcheckout():
    memberID = input("member ID: ")  # Todo to make gui and create error boxes for specific errors
    if not memberID.isalpha() or len(memberID) != 4:
        return False
    bookID = searchData(input("book ID: "),"database.txt","ID")[0]
    if not bookID:
        return False
    if bookID[-1] != '0':
        return False
    editData(memberID,bookID)
    addLogs(memberID,bookID)

#todo to optimise and to further commemnt