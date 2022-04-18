# python libary it create application.
# Gui:-graphical user interface ,it is a destop app. which helps  you to interact with computer
#  functions and methods that can be used to create an application.
# package:=package:-A package contains all the files you need for a module.
# *>>>it will contain all the module files for this,so we can not need to import again again
from tkinter import*
# It helps to display the root window and manages all the other components of the tkinter application
# TK:- manages all the other components of the tkinter application.
define_tk=Tk()
define_tk.configure(background="yellow")
define_tk.title(" NAVGURUKUL CHATBOAT")

def send():
    # get() : Returns the entry's current text as a string
    send = "you->"+e.get()
    # \n is using next line
    txt.insert(END,"\n"+send)
    if (e.get()=="hi"):
# get>to get the output or to write text
        txt.insert(END,"\n"+"                       Bot-> Hello!, How can we help you? ")
    elif (e.get()=="i want to know about NAVGURUKUL?"):
        # Insert:-it insert text form whatever we enter data
# End:-const and literal,not be change
# Insert:-it insert text form whatever we enter data
        txt.insert(END,"\n"+"Bot->                  Sure! Navgurukul is free SOFTWARE DEVELOPMENT COURSE  ")
    elif (e.get()=="what are the languages you are teaching "):
        txt.insert(END,"\n"+"Bot->                  We  teahes Programming Languages ")
    elif (e.get()=="Like?"):
        txt.insert(END,"\n"+"Bot->                  Python,Javascript ,Advance javascript ,Node js and react.js ")
    elif (e.get()=="oky thankyou!"):
        txt.insert(END,"\n"+"Bot->                  for any other query please visit again.")
    else:
        txt.insert(END,"\n"+"Bot-> Plese enter again ")
    e.delete(0,END)
    # grid :-it gives us to  geomatrically stucture. it is a method for use row and coloumn.
# widgets:-it is gui ,which allows us to take user input
# gui:-graphical user interface ,it is a destop app. which helps  you to interact with computer
txt = Text(define_tk)
txt.grid(row=0,column=0)
# use to display a single line program.
# Entry widgets are used to display a single line text that is generally taken in the form of user Input.
e=Entry(define_tk,width=100,bg="pink",fg="purple")
send=Button(define_tk,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
define_tk.mainloop()