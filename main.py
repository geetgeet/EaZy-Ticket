
# Import libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title("EaZy Ticket")
window.geometry("500x500")
window.configure(background="teal")

# Creates variables prices
socceram = 40
movieam = 75
theateram  = 100

# Creates Tkinter widgets
ttypevar = StringVar()

lblcell = Label(window, text="Cellphone number:", pady=5,)
lblcell.grid(row=0, column=0, sticky=W, )
lblcell.configure(background="teal")
cellno = Entry(window, width=20, )
cellno.grid(row = 0, column=1, )

lbltickettype = Label(window, text="Ticket Category:", pady=5)
lbltickettype.grid(row=1, column=0, sticky=W)
lbltickettype.configure(background="teal")
tickettype = ttk.Combobox(window, textvariable=ttypevar, width=20, value=["Soccer", "Movie", "Theater"],state="")
tickettype.grid(row=1, column=1)

lbltktnum = Label(window, text="Number of tickets:", pady=5)
lbltktnum.grid(row=2, column=0, sticky=W)
lbltktnum.configure(background="teal")

num_ticket = ttk.Spinbox(window, from_=0, to=20, state="readonly")
num_ticket.grid(row=2, column=1)

anslbl = Label(window,text="*************************************")
anslbl.configure(background="teal")
anslbl.grid(row=4, column=0)





#Create class
class clsTiketSales:
    def __init__(self, cellno, nrtkts, price):
        self.celno = cellno
        self.nrtkts = nrtkts
        self.price = price
        return

 # Main calc def
def calc():
    # Passes through class
    tksale = clsTiketSales(cellno.get(), float(num_ticket.get()), tickettype.get())

    # Ticket type and Calculation #Added Vat
    if tickettype.get() == "Soccer":
        scprice = socceram * int(num_ticket.get()) + (socceram * int(num_ticket.get())*(14/100))
        anslbl.config(text="Price:"+ str(scprice) + "\n"+ ("(VAT included)") + "\n" + "Amount of Tickets:"+"\n" +str(num_ticket.get()) + "\n" +"Reservation done by:"+ str(cellno.get()))
    if tickettype.get() == "Movie":
        mvprice = movieam * int(num_ticket.get()) + (movieam * int(num_ticket.get()) *(14/100))
        anslbl.config(text="Price:"+ str(mvprice) + "\n" +("(VAT included)") + "\n" "Amount of Tickets:"+"\n" +str(num_ticket.get()) + "\n" +"Reservation done by:"+ str(cellno.get()))
    if tickettype.get() == "Theater":
        thprice = theateram * int(num_ticket.get()) + (theateram * int(num_ticket.get())*(14/100))
        anslbl.config(text="Price:"+ str(thprice) + "\n" +("(VAT included)") + "\n" "Amount of Tickets:"+"\n" +str(num_ticket.get()) + "\n" +"Reservation done by:"+ str(cellno.get()))


def clear():
    anslbl.configure(text="")
    cellno.delete(0,END)
    tickettype.delete(0,END)
    num_ticket.set(value=0)

clearb=Button(window,text="Clear Entries" , command=clear)
clearb.grid(row=5,column=1)




#Creates button
tkbtn = Button(window, text="Calculate", command=calc, width=20, height=1)
tkbtn.grid(row=5, column=0)
# Adds widgets






window.mainloop()
