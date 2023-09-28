from tkinter import *



# Create the main window
window = Tk()
window.title("Add and Subtract")
window.geometry("600x400")

# add widgets to main window
lb1=Label(window, text="First Number")

lb2=Label(window,text="Second window")

lb3=Label(window,text="result")

# add entry widgete(display a single line text field to accept values from users)

t1=Entry()
t2=Entry()
t3=Entry()

#arranging the widets (placing  each and eveyr thing)
lb1.place(x=100,y=50)
t1.place(x=200,y=50)

lb2.place(x=100,y=100)
t2.place(x=200,y=100)

lb3.place(x=100,y=150)
t3.place(x=200,y=150)



# functions to perform  addition

def add():
  num1=int(t1.get())
  num2=int(t2.get())
  result=num1+num2
  t3.insert(END,str(result))
# end means that the text which is being inserted is the last thing that is going to be inserted in the entry widgets


def subtract():
  num1=int(t1.get())
  num2=int(t2.get())
  result=num1-num2
  t3.insert(END,str(result))

# Add buttons
b1= Button(window,text='Add',command=add)
b2=Button(window,text='Sub',command=subtract)

b1.place(x=100,y=150)
b2.place(x=200,y=150)

lb3.place(x=100,y=200)
t3.place(x=200,y=200)


#enter the main event loop everytime an event is trigggered. 
window.mainloop() # this is very important to run the main loop else if this was not there nothing will be seen 
