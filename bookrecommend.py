import matplotlib.pyplot as plt
from database import searchData, getDate
from datetime import datetime

def bookrecommend (memberID):
    #this function takes a member ID searched the data base for the books the
    # member would be most likely to read using a given formula which is
    # explained below
    if not memberID.isalpha() or len(memberID) != 4:
    #validity checks
        return False
    memberBooks = searchData(memberID,"logfile.txt","Member ID")
    genres = {}
    tiedGenre = {}
    bookDict = {}
    bookGenres = [searchData(eachBook[0],"database.txt","ID")[0][1] for
                  eachBook in memberBooks]
    #finds all the genre of books the member has read
    for genre in bookGenres:
    #assigns the frequency of genre to genre with the genre as the key
        genres[genre] = bookGenres.count(genre)
    bookCount = int(9/len(bookGenres))
    for key, value in genres.items():
    #finds all the genre with same frequency
        tiedGenre.setdefault(value, set()).add(key)
    #adds them to this list
    tied = [values for key, values in tiedGenre.items() if len(values) > 1]
    if tied:
        tiedArray = list(tied[0])
        tiedCount = round(10/len(tiedArray))
        for eachBook in memberBooks:
            #checks which genres have the same frequencies
            if searchData(eachBook[0], "database.txt", "ID")[0][1] in \
                    tiedArray:
                key = searchData(eachBook[0], "database.txt", "ID")[0][1]
                #finds all the books in that genre
                if eachBook[-1] == '0':
                    #if the book of said genre is currently on loan
                    # assign the max value
                    genres[key] += 0.5
                else:
                    #otherwise use this formula to change the weighting
                    # of the value assigned the genre
                    genres[key] += len(str((datetime.today() -
                                    getDate(eachBook[-1])).days))/100*tiedCount
    for key, values in genres.items():
        #goes through all the genres
        count = int(values*bookCount)
        #calculated the number of books to be retrieved for the given genre
        books = searchData(key,"database.txt","genre")
        #finds all the books with the given genre
        allBooks = {}
        counter = 0
        while counter < len(books):
            if books[counter][2] in [searchData(ID[0],
                                    "database.txt","ID")[0][2]
                                     for ID in memberBooks]:
                #removes the books that the user has already read
                books.remove(books[counter])
                counter -= 1
            counter += 1
        if len(books) < count:
            #appends all the books if the number of books in the given genre
            # is less the amount of books to be retrieved
            for eachBook in books:
                bookDict[eachBook[2]] = len(searchData(eachBook[0],
                                                       "logfile.txt","ID"))+\
                                        values+count
        else:
            for eachBook in books:
                #otherwise get the top amount of books from the given genre
                # assigning a value to it so it can be sorted
                allBooks[eachBook[2]] = len(searchData(eachBook[0],
                                                       "logfile.txt","ID"))+\
                                        values+count
        if allBooks:
            #sorts out the most popular books and adds the top count
            # amount of books
            allBooks = {k: v for k, v in sorted(allBooks.items(),
                                                key=lambda item: item[1])}
            allBooks = list(allBooks.items())[:count]
            for books in allBooks:
                bookDict[books[0]] = books[1]
    bookDict = {k: v for k, v in sorted(bookDict.items(), key=lambda item:
    item[1])}
    #sorts the dictionary of books
    x = [number for number in range(1,len(bookDict.keys())+1)]
    y = bookDict.values()
    fig = plt.figure(figsize=(5,2))
    graph = fig.add_subplot(1,1,1)
    graph.plot(x,y,"r--")
    #creates a graph with the index of the books as the x-axis and the
    # popluarity value as the y-axis
    return fig, list(bookDict.keys())

#--------------------------------------Testing---------------------------------

def testing_bookrecommend():
    #test that the graph is created and with the right data for the given
    # member
    actual = bookrecommend("ilug")
    expected = [10, 10, 10, 10, 10, 11, 12, 15]
    assert list(actual[0].gca().lines[0].get_ydata()) == expected, \
        "should return a graph showing a list of recommended books"
    plt.show()

def test_invalid_member():
    #test if id is not a valid id, not part of the alphabet
    actual = bookrecommend(memberID="1234")
    expected = False
    assert actual == expected , "should return False as members are not " \
                                "letters"

def test_invalid_member_len():
    #test if id is not a valid id, too short
    actual = bookrecommend(memberID="abc")
    expected = False
    assert actual == expected , "should return False as members is the not " \
                                "the right length"

if __name__ == "__main__":
    #runs all test
    test_invalid_member_len()
    test_invalid_member()
    testing_bookrecommend()
    print("All test passed")

