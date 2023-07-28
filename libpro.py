from cProfile import label
import sqlite3
from tkinter import *
from tkinter import messagebox

from tkinter.messagebox import showerror, showinfo
from PIL import Image,ImageTk
from datetime import date as dt
Date = dt.today().strftime("%d/%m/%Y")


def strCheck(entry):
        try:
            if entry.isdigit() or entry == '':
                return True
        except:
            return False

def intcheck(entry):
        try:
            int(entry)
            return True
        except:
            return False



def home():
    win = Tk()
    win.title('Library app')
    win.geometry('600x500')
    win.resizable(False, False)
    win['bg'] = '#1b2328'
    win.iconbitmap("libraryIcons\li (1).ico")

    # global properties

    font_header = ("Helvetica", 12, "bold")
    font_body = ("Helvetica", 11, "bold")
    font_btn = ("Comic Sans MS", 10, "bold")
    theme_color = "#1b2328"
    #win.counts = 0

    # stringVar
    info = StringVar()
    name = StringVar()
    author = StringVar()
    isbn = StringVar()
    pn = StringVar()
    yop = StringVar()
    dname = StringVar()
    disbn = StringVar()
    eisbn = StringVar()
    ename = StringVar()
    epname = StringVar()
    eAname = StringVar()
    eyop = StringVar()
    getImage = Image.open("libraryIcons/search2.png")
    getImage2 = Image.open("libraryIcons/home2.png")
    getImage3 = Image.open("libraryIcons/akrix.png")
    getImage4 = Image.open("libraryIcons/book.png")
    getImage5 = Image.open("libraryIcons/destroy.png")
    getImage6 = Image.open("libraryIcons/garbage.png")
    getImage7 = Image.open("libraryIcons/edit.png")

    #Resize the image. resize is a tkinter function.
    resizedImage = getImage.resize((20,20))
    resizedImage2 = getImage2.resize((30,30))
    resizedImage3 = getImage3.resize((300,250))
    resizedImage4 = getImage4.resize((30,25))
    resizedImage5 = getImage5.resize((20,20))
    resizedImage6 = getImage6.resize((30,25))
    resizedImage7 = getImage7.resize((25,25))
    
    #Make image readable or displayable on tkinter
    newImg= ImageTk.PhotoImage(resizedImage)
    newImg2= ImageTk.PhotoImage(resizedImage2)
    newImg3= ImageTk.PhotoImage(resizedImage3)
    newImg4= ImageTk.PhotoImage(resizedImage4)
    newImg5= ImageTk.PhotoImage(resizedImage5)
    newImg6= ImageTk.PhotoImage(resizedImage6)
    newImg7= ImageTk.PhotoImage(resizedImage7)

    first = Label(win,width=600,height=2,bd=1,border=2, borderwidth=1,bg=theme_color).place(x=0,y=0)

    # horizontal line
    hLine = LabelFrame(win, width=600, height=1, bd=0, borderwidth=1, bg="grey").place(x=0, y=37)

    # add buttons at top of windows
    button1 = Button(first,image=newImg2 ,bg=theme_color,bd=0, command=lambda: resetApp()).place(x=5,y=2)
    button2 = Button(first,image=newImg4 ,bg=theme_color,command=lambda:add(),bd=0).place(x=55,y=5)
    button3 = Button(first,image=newImg, bg=theme_color,bd=0,command=lambda:display()).place(x=575,y=5)
    button4 = Button(first,image=newImg6,bg=theme_color,bd=0,command=lambda:rid()).place(x=155,y=5)
    button5 = Button(first,image=newImg7,bg=theme_color,bd=0,command=lambda:ed()).place(x=105,y=5)

    
    welcome = Label(win,image=newImg3,fg='black', bg=theme_color,)
    welcome.place(x=160,y=150)

    inputVal = Entry(win,width=35,bd=2,fg='grey',relief=FLAT,font=('Arial bold',10))
    inputVal.place(x=320,y=6)

    inputVal.insert(0,'search by Author | Title | ISBN')
    def onClick(event):
        inputVal.config(state=NORMAL,fg='black',font=('Arial bold',10),textvariable=info)
        inputVal.delete(0,END)
    inputVal.bind("<Button-1>",onClick)

    def add():
                global frame


                frame = LabelFrame(win, width=600,height=500,bg=theme_color)
                frame.place(x=0,y=0)

                fieldTitle = Label(frame, text='Book Entry Field', fg='grey', bg=theme_color, font=font_header)
                fieldTitle.place(x=10, y=8)

                exitBtn = Button(frame, image=newImg5, fg='white', bg=theme_color, bd=0, command=des)
                exitBtn.place(x=570, y=8)

                # horizontal line
                hLine = LabelFrame(win, width=600, height=1, bd=0, borderwidth=1, bg="grey").place(x=0, y=37)

                nl = Label(frame,text='Book Title:',fg='white',bg=theme_color, font=font_body)
                nl.place(x=10,y=70)
                n = Entry(frame,width=35,bd=2,fg='black',relief=FLAT,font=('Arial bold',10),textvariable=name)
                n.place(x=130,y=70)

                al = Label(frame,text='Book Author:',fg='white',bg=theme_color, font=font_body)
                al.place(x=10,y=115)
                a = Entry(frame,width=35,bd=2,fg='black',relief=FLAT,font=('Arial bold',10),textvariable=author)
                a.place(x=130,y=115)

                il = Label(frame,text='ISBN:',fg='white', bg=theme_color, font=font_body)
                il.place(x=10,y=160)
                i = Entry(frame,width=35,bd=2,fg='black',relief=FLAT,font=('Arial bold',10),textvariable=isbn)
                i.place(x=130,y=160)

                pl = Label(frame,text='Publisher:',fg='white',bg=theme_color, font=font_body)
                pl.place(x=10,y=205)
                p = Entry(frame,width=35,bd=2,fg='black',relief=FLAT,font=('Arial bold',10),textvariable=pn)
                p.place(x=130,y=205)

                yl = Label(frame,text='Publishing year:',fg='white',bg=theme_color, font=font_body)
                yl.place(x=10,y=250)
                y = Entry(frame,width=35,bd=2,fg='black',relief=FLAT,font=('Arial bold',10),textvariable=yop)
                y.place(x=130,y=250)

                b = Button(frame,text='+Add Book',fg='white',bg='green',bd=0,width=10,height=1,command=addBooks, font=font_btn)
                b.place(x=10,y=464)

                c = Button(frame,text='Clear field',fg='white',bg='blue',bd=0,width=10,height=1,command=clear, font=font_btn)
                c.place(x=120,y=464)


    def clear():
        name.set('')
        author.set('')
        isbn.set('')
        pn.set('')
        yop.set('')

    def des():
        frame.destroy()

    def des2():
        frame2.destroy()
        info.set('')

    def des3():
        frame3.destroy()
        info.set('')

    def des4():
        frame4.destroy()

    def des5():
        frame5.destroy()

    def resetApp():
        win.destroy()
        home()

    def addBooks():
        try:
            global bookName
            global bookAuthor
            global ISBN
            global pName
            global YOP
            global databaseData
    
            bookTitle = name.get()
            bookName = bookTitle.title()
            authorName = author.get()
            bookAuthor = authorName.title()
            ISBN = isbn.get()
            pN = pn.get()
            pName = pN.title()
            YOP = yop.get()

            databaseData = []
            cn = sqlite3.connect('shelf.db')
            cur = cn.cursor()
            cur.execute("SELECT * FROM shelf")
            records = cur.fetchall()
            for row in records:
                for i in row:
                    databaseData.append(i)
        except:
            pass


        if  bookName == '':
            showerror(title='info',message='please enter bookname')
        elif bookAuthor == '':
            showerror(title='info',message='please enter authors name')
        elif strCheck(bookAuthor):
            showerror(title='info',message="author's name must be alphabetic")
        elif ISBN == '':
            showerror(title='info',message='please enter ISBN')
        elif intcheck(ISBN) is False:
            showerror(title='info',message='ISBN must be numeric')
        elif pName == '':
            showerror(title='info',message="please enter publisher's name")
        elif strCheck(pName):
            showerror(title='info',message="publisher's name must be aplhabetic")
        elif YOP == "":
            showerror(title='info',message='please enter publishing year')
        elif intcheck(YOP) is False:
            showerror(title='info',message='year of publication must be numeric')
        # checking database for isbn
        elif ISBN in databaseData:
            showerror(title='info', message='ISBN already exist!')

        else:
            save()

    def rid():
        
        global frame4
        frame4 = LabelFrame(win, width=600,height=500,bg=theme_color)
        frame4.place(x=0,y=0)

        fieldTitle = Label(frame4, text='Delete Book By Title and ISBN', fg='grey', bg=theme_color, font=font_header)
        fieldTitle.place(x=10, y=8)

        hLine = LabelFrame(win, width=600, height=1, bd=0, borderwidth=1, bg="grey").place(x=0, y=37)

        dn = Label(frame4,text='Book Title:',fg='white',bg=theme_color, font=font_body)
        dn.place(x=10,y=70)
        en = Entry(frame4,width=35,bd=2,fg='black',relief=FLAT,font=('Arial bold',10),textvariable=dname)
        en.place(x=130,y=70)

        di = Label(frame4,text='ISBN:',fg='white',bg=theme_color, font=font_body)
        di.place(x=10,y=115)
        i = Entry(frame4,width=35,bd=2,fg='black',relief=FLAT,font=('Arial bold',10),textvariable=disbn)
        i.place(x=130,y=115)

        delBtn = Button(frame4,text='Delete',bg='red',fg='white',font=font_btn,command=Crid)
        delBtn.place(x=4,y=460)

        exitBtn = Button(frame4, image=newImg5, fg='white', bg=theme_color, bd=0, command=des4)
        exitBtn.place(x=570, y=8)
                # horizontal line
        

        pass
    def Crid():
        global dName, Disbn
        Dname = dname.get()
        dName = Dname.title()
        Disbn = disbn.get()

        if dName == '':
            showerror(title='info',message='please enter book tilte')
        elif Disbn == '':
            showerror(title='info',message='please enter ISBN')
        elif intcheck(Disbn) is False:
            showerror(title='info',message='ISBN must be Numeric')
        else:
            delete()
            showinfo(title='info',message='year of publication must be numeric')

    def delete():
        try:
            cn = sqlite3.connect('shelf.db')
            cur = cn.cursor()

            cur.execute("DELETE from shelf WHERE BookTitle = ? AND ISBN = ? ",(dName,Disbn)) 

            cn.commit()
        except:
            pass

    def ed():
        global frame5
        frame5 = LabelFrame(win, width=600,height=500,bg=theme_color)
        frame5.place(x=0,y=0)

        fieldTitle = Label(frame5, text='Edit Book Info', fg='grey', bg=theme_color, font=font_header)
        fieldTitle.place(x=10, y=8)

        hLine = LabelFrame(win, width=600, height=1, bd=0, borderwidth=1, bg="grey").place(x=0, y=37)
        exitBtn = Button(frame5, image=newImg5, fg='white', bg=theme_color, bd=0, command=des5)
        exitBtn.place(x=570, y=8)

        ei = Label(frame5,text='Book ISBN:',fg='white',bg=theme_color, font=font_body)
        ei.place(x=10,y=70)
        eie = Entry(frame5,width=35,bd=2,fg='black',relief=FLAT,font=('Arial bold',10),textvariable=eisbn)
        eie.place(x=140,y=70)

        edn = Label(frame5,text='Edit Title:',fg='white',bg=theme_color, font=font_body)
        edn.place(x=10,y=115)
        edne = Entry(frame5,width=35,bd=2,fg='black',relief=FLAT,font=('Arial bold',10),textvariable=ename)
        edne.place(x=140,y=115)

        eba = Label(frame5,text='Edit Author:',fg='white', bg=theme_color, font=font_body)
        eba.place(x=10,y=160)
        eA= Entry(frame5,width=35,bd=2,fg='black',relief=FLAT,font=('Arial bold',10),textvariable=eAname)
        eA.place(x=140,y=160)

        epn = Label(frame5,text='Edit publisher:',fg='white',bg=theme_color, font=font_body)
        epn.place(x=10,y=205)
        epne = Entry(frame5,width=35,bd=2,fg='black',relief=FLAT,font=('Arial bold',10),textvariable=epname)
        epne.place(x=140,y=205)

        yl = Label(frame5,text='Edit Publish year:',fg='white',bg=theme_color, font=font_body)
        yl.place(x=10,y=250)
        y = Entry(frame5,width=35,bd=2,fg='black',relief=FLAT,font=('Arial bold',10),textvariable=eyop)
        y.place(x=140,y=250)

        checkBut = Button(frame5,text='Edit',width=5, bg='red',fg='white',font=font_btn,command=cedit)
        checkBut.place(x=4,y=460)
        pass
    def cedit():
        databaseData2 = []
        cn = sqlite3.connect('shelf.db')
        cur = cn.cursor()
        cur.execute("SELECT * FROM shelf")
        records = cur.fetchall()
        for row in records:
            for i in row:
                databaseData2.append(i)
        if eisbn.get() == '':
            showerror(title='info',message='please enter ISBN')
        elif intcheck(eisbn.get()) is False:
            showerror(title='info',message='ISBN must be numeric')
        elif eisbn.get() not in databaseData2:
            showerror(title='info', message="ISBN dosen't exist!")
        if  ename.get() == '':
            showerror(title='info',message='please enter bookname')
        elif eAname.get() == '':
            showerror(title='info',message='please enter authors name')
        elif strCheck(eAname.get()):
            showerror(title='info',message="author's name must be alphabetic")
        elif epname.get() == '':
            showerror(title='info',message="please enter publisher's name")
        elif strCheck(epname.get()):
            showerror(title='info',message="publisher's name must be aplhabetic")
        elif eyop == "":
            showerror(title='info',message='please enter publishing year')
        elif intcheck(eyop.get()) is False:
            showerror(title='info',message='year of publication must be numeric')
        else:
            edit()
            showinfo(title='info',message='Book info sucessfully updated')

        
    def edit():
        eName = ename.get()
        edName = eName.title()
        eauthor = eAname.get()
        edAuthor = eauthor.title()
        ePname = epname.get()
        edpName = ePname.title()
        eYOP = eyop.get()

        cn = sqlite3.connect('shelf.db')
        cur = cn.cursor()
        cur.execute("UPDATE shelf SET BookTitle='{}', BookAuthor='{}', PublisherName='{}', YOP='{}' WHERE ISBN={}".format(edName,edAuthor,edpName,eYOP,eisbn.get()))
        cn.commit()

    def save():
        cn = sqlite3.connect('shelf.db')
        cur = cn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS shelf(
        BookTitle text,
        BookAuthor text,
        ISBN varchar,
        PublisherName text,
        YOP integer,
        DateAdded  real)""")

        cur.execute("INSERT INTO shelf (BookTitle,BookAuthor,ISBN,PublisherName,YOP,DateAdded) VALUES(?,?,?,?,?,?)", (bookName,bookAuthor,ISBN,pName,YOP,Date))
        cn.commit()

        # clear field after
        clear()

    def display():
        INfo = info.get()
        inFO = INfo.title()

        try:
                global frame2, frame3


                cn = sqlite3.connect('shelf.db')
                cur = cn.cursor()

                cur.execute("SELECT * FROM shelf WHERE ISBN=? OR BookTitle=? OR BookAuthor=?", (inFO, inFO, inFO))
                records = cur.fetchall()
                print(records[0])
                # checking if search parameter is in the database scope
                if inFO in records[0]:

                        frame2 = LabelFrame(win, width=600, height=500, bg=theme_color)
                        frame2.place(x=0, y=0)

                        res = Label(frame2, text='Book Search Result', fg='grey', bg=theme_color, font=font_header)
                        res.place(x=0, y=8)

                        exitBtn = Button(frame2, image=newImg5, fg='white', bg=theme_color, bd=0, command=des2)
                        exitBtn.place(x=570, y=8)

                        # horizontal line
                        hLine = LabelFrame(win, width=600, height=1, bd=0, borderwidth=1, bg="grey").place(x=0, y=37)

                        nd = Label(frame2, text='Book Title :', bg=theme_color, fg='white', font=font_body)
                        nd.place(x=5, y=80)

                        ndl = Label(frame2, text=records[0][0], bg=theme_color, fg='white', font=font_body)
                        ndl.place(x=120, y=80)

                        ad = Label(frame2, text='Author :', bg=theme_color, fg='white', font=font_body)
                        ad.place(x=5, y=120)
                        adl = Label(frame2, text=records[0][1], bg=theme_color, fg='white', font=font_body)
                        adl.place(x=120, y=120)

                        isd = Label(frame2, text='ISBN :', bg=theme_color, fg='white', font=font_body)
                        isd.place(x=5, y=160)
                        isdl = Label(frame2, text=records[0][2], bg=theme_color, fg='white', font=font_body)
                        isdl.place(x=120, y=160)

                        pd = Label(frame2, text='Publisher :', bg=theme_color, fg='white', font=font_body)
                        pd.place(x=5, y=200)
                        pdl = Label(frame2, text=records[0][3], bg=theme_color, fg='white', font=font_body)
                        pdl.place(x=120, y=200)

                        ypd = Label(frame2, text='Publish Year :', bg=theme_color, fg='white', font=font_body)
                        ypd.place(x=5, y=240)
                        ypl = Label(frame2, text=records[0][4], bg=theme_color, fg='white', font=font_body )
                        ypl.place(x=120, y=240)

                        yd = Label(frame2, text='Date added :', bg=theme_color, fg='white', font=font_body)
                        yd.place(x=5, y=280)
                        ydl = Label(frame2, text=records[0][5], bg=theme_color, fg='white', font=font_body)
                        ydl.place(x=120, y=280)

                else:
                   pass


        except:
            frame3 = LabelFrame(win, width=600, height=500, bg=theme_color)
            frame3.place(x=0, y=0)
            noResult = Label(frame3, text='Sorry, No Search Result Found!', bg=theme_color, fg='grey', font=font_body)
            noResult.place(x=0, y=8)
            # horizontal line
            hLine = LabelFrame(win, width=600, height=1, bd=0, borderwidth=1, bg="grey").place(x=0, y=37)

            d3 = Button(frame3, image=newImg5, fg='white', bg=theme_color, bd=0, command=des3)
            d3.place(x=570, y=8)



    mainloop()
home()