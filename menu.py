from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from bookrecommend import *
from booksearch import *
from bookreturn import *
from bookcheckout import *

def displaySearch():
    #create a message box with an error or the relevent infomation for when a search is entered
    bookName = searchInput.get().strip()
    display = booksearch(bookName)
    if not display:
        messagebox.showinfo("Error", "Invalid Input or Book does not exist")
    else:
        message = ""
        for each in display[bookName]:
            message += "".join(each)+"\n"
        messagebox.showinfo(bookName,message)

def displayCheckout():
    #creates message box relating each relevant error or shows that book is return successfully
    bookID = idInput.get().strip()
    memberID = memberInput.get().strip()
    display = bookcheckout(memberID,bookID)
    if display == 0:
        messagebox.showerror("Error", "Member ID is invalid")
    elif display == 1:
        messagebox.showerror("Error", "Book already on loan")
    elif display == 2:
        messagebox.showerror("Error", "Invalid Book ID")
    elif display[memberID]:
    #returns a warning box if the book is overdue
        message = ""
        for info in display[memberID]:
            message += " ".join("".join(data) for data in info)+"\n"
        messagebox.showwarning("Warning Overdue",message)
        messagebox.showinfo("Success","The book is now loaned out")
    else:
        messagebox.showinfo("Success", "The book is now loaned out")

def displayReturn():
    #shows the relevant errors or a success message when a book is successfully returned
    bookID = returnId_input.get().strip()
    display = bookreturn(bookID)
    if display == 0:
        messagebox.showerror("Error", "Invalid Book ID")
    elif display == 1:
        messagebox.showerror("Error", "Book already available")
    elif display == None:
        messagebox.showinfo("Success", "The book is now returned")
    else:
        #shows a warning of the book has been on loan for over 60 days with the amount of days the book has been on loan for
        messagebox.showwarning("Warning Overdue", str(display) + " days overdue")
        messagebox.showinfo("Success", "The book is now returned")


def displayRecommend():
    #display an error if invalid member id otherwise shows a graph of the recommend books by recommendation score
    memeberID = recommendMember_input.get().strip()
    display = bookrecommend(memeberID)
    if not display:
        messagebox.showerror("Error", "Member ID is invalid")
    else:
        #draws the graph in the given frame
        canvas = FigureCanvasTkAgg(display[0],master=graphFrame)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0,rely= 0,relwidth=1,relheight=1)
        message = ""
        for name in display[1]:
            message += str(display[1].index(name)+1)+": "+name+"\n"
        messagebox.showinfo("Success", message)
        #shows a list of the recommended books with 10 being the most reccommended

window = Tk()
window.title("Leo's Library Management System")
window.minsize(width=400,height=400)
window.geometry("800x600")
window.configure(bg="#000000")

#creates the welcome message
welcomeFrame = Frame(window,bg="#0C0032",bd=5)
welcomeFrame.place(relx=0.1,rely=0.01,relwidth=0.8,relheight=0.2)
welcome = Label(welcomeFrame, font=('Calibri', 40,'italic'),
                text="Welcome to Leo's Library!",bg="#190061",fg="#FFFFFF")
welcome.place(relx=0, rely=0 ,relwidth=1,relheight=1)

#creates a frame, lables and search funcionality (entry box and search button)
searchFrame = Frame(window,bg="#240090",bd=5)
searchFrame.place(relx=0.2,rely=0.25,relwidth=0.6,relheight=0.16)
searchLabel = Label(searchFrame,font=('Calibri', 15,"bold"),
                    text="Book Search",bg="#240090",fg="#FFFFFF")
searchLabel.place(relx=0.25, rely=0 ,relwidth=0.5,relheight=0.5)
bookLable = Label(searchFrame,font=('Calibri', 15),
                  text="Book Name: ",bg="#240090",fg="#FFFFFF")
bookLable.place(relx=0.02, rely=0.5 ,relwidth=0.3,relheight=0.3)
searchInput = Entry(searchFrame, width=90,bg="#282828",fg="#FFFFFF")
searchInput.place(relx=0.3, rely=0.515 ,relwidth=0.5,relheight=0.3)
bookSearchBtn = Button(searchFrame, text="Search", command=displaySearch,
                       bg="#3500D3", fg="#FFFFFF", font=('Calibri', 15))
bookSearchBtn.place(relx=0.8,rely=0.515, relwidth=0.15,relheight=0.3)

#creates the frame,lables, entry boxes and the buttons for the bookcheckout function
checkFrame  = Frame(window,bg="#240090",bd=5)
checkFrame.place(relx=0.2,rely=0.43,relwidth=0.6,relheight=0.16)
checkLabel = Label(checkFrame,font=('Calibri', 15,"bold"),
                    text="Book Checkout",bg="#240090",fg="#FFFFFF")
checkLabel.place(relx=0.25, rely=0 ,relwidth=0.5,relheight=0.5)
idLable = Label(checkFrame,font=('Calibri', 15),
                  text="Book Id: ",bg="#240090",fg="#FFFFFF")
idLable.place(relx=0, rely=0.5 ,relwidth=0.3,relheight=0.3)
idInput = Entry(checkFrame, width=30,bg="#282828",fg="#FFFFFF")
idInput.place(relx=0.25, rely=0.515 ,relwidth=0.13,relheight=0.3)
memberLable = Label(checkFrame,font=('Calibri', 15),
                  text="Member Id: ",bg="#240090",fg="#FFFFFF")
memberLable.place(relx=0.38, rely=0.5 ,relwidth=0.3,relheight=0.3)
memberInput = Entry(checkFrame, width=30,bg="#282828",fg="#FFFFFF")
memberInput.place(relx=0.67, rely=0.515 ,relwidth=0.13,relheight=0.3)
bookcheckoutBtn = Button(checkFrame, text="Search", command=displayCheckout, bg="#3500D3", fg="#FFFFFF",
                   font=('Calibri', 15))
bookcheckoutBtn.place(relx=0.8,rely=0.515, relwidth=0.15,relheight=0.3)

##creates the frame,lables, entry box and the button for the bookreturn function
returnFrame = Frame(window,bg="#240090",bd=5)
returnFrame.place(relx=0.2,rely=0.61,relwidth=0.6,relheight=0.16)
returnLable = Label(returnFrame,font=('Calibri', 15,"bold"),
                    text="Book Return",bg="#240090",fg="#FFFFFF")
returnLable.place(relx=0.25, rely=0 ,relwidth=0.5,relheight=0.5)
returnID_lable = Label(returnFrame,font=('Calibri', 15),
                  text="Book Id: ",bg="#240090",fg="#FFFFFF")
returnID_lable.place(relx=0, rely=0.5 ,relwidth=0.3,relheight=0.3)
returnId_input = Entry(returnFrame, width=90,bg="#282828",fg="#FFFFFF")
returnId_input.place(relx=0.3, rely=0.515 ,relwidth=0.5,relheight=0.3)
bookreturnBtn = Button(returnFrame, text="Search", command=displayReturn, bg="#3500D3", fg="#FFFFFF",
                   font=('Calibri', 15))
bookreturnBtn.place(relx=0.8,rely=0.515, relwidth=0.15,relheight=0.3)

#creates the frame,lables, entry box and the button for the bookrecommend function
recommendFrame = Frame(window,bg="#240090",bd=5)
recommendFrame.place(relx=0.1,rely=0.79,relwidth=0.6,relheight=0.16)
recommendLabel = Label(recommendFrame,font=('Calibri', 15,"bold"),
                    text="Book Recommend",bg="#240090",fg="#FFFFFF")
recommendLabel.place(relx=0.25, rely=0 ,relwidth=0.5,relheight=0.5)
recommendMember_lable = Label(recommendFrame,font=('Calibri', 15),
                  text="Member Id: ",bg="#240090",fg="#FFFFFF")
recommendMember_lable.place(relx=0, rely=0.5 ,relwidth=0.3,relheight=0.3)
recommendMember_input = Entry(recommendFrame, width=90,bg="#282828",fg="#FFFFFF")
recommendMember_input.place(relx=0.3, rely=0.515 ,relwidth=0.5,relheight=0.3)
recommendBtn = Button(recommendFrame, text="Search", command=displayRecommend, bg="#3500D3", fg="#FFFFFF",
                   font=('Calibri', 15))
recommendBtn.place(relx=0.8,rely=0.515, relwidth=0.15,relheight=0.3)
#creates the fram for the graphed to be place later on
graphFrame = recommendFrame = Frame(window,bg="#240090",bd=5)
graphFrame.place(relx=0.7,rely=0.79,relwidth=0.2,relheight=0.16)


window.mainloop()
