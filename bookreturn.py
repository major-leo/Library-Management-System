from database import searchData, loanDays,editData
from datetime import datetime

def bookreturn():
    bookID = searchData(input("book ID: "),"database.txt","ID")[0]  # Todo to make into a gui
    if not bookID:
        return False
    if bookID[0][-1] == '0':
        return False
    memberBook = searchData(bookID[0],"logfile.txt","ID")
    editData("0",bookID,"database.txt")
    loan = loanDays(memberBook)
    editData(datetime.today().strftime('%d/%m/%Y'),memberBook[0],"logfile.txt")
    if loan > 60:
        return loan

# Todo to further comment and utilise