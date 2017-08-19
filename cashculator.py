from tkinter import*
import tkinter.messagebox
import locale
import os
import time


window=Tk()
window.title("Cash Breakdown version 1.4")
window.resizable(0,0)

window.wm_iconbitmap('renlogo.ico')



def cquit():
    window.destroy()

def cabout():
    tkinter.messagebox.showinfo("About Cash Breakdown",'This Application is Licensed to Avon Angeles Branch \n\n \
    "To GOD be all the glory" \n\n \
    Created by : Renan Rivera :)')

def Print():
    ComputeTotal()
    os.startfile("cashbreakdown.html", "print")

def Openfile():
     os.startfile(r'.\cashbreakdown')

def reset():
    OneK_entry.delete(0,'end')
    OneK_entry.insert(0,'')
    FiveH_entry.delete(0,'end')
    FiveH_entry.insert(0,'')
    TwoH_entry.delete(0,'end')
    TwoH_entry.insert(0,'')
    OneH_entry.delete(0,'end')
    OneH_entry.insert(0,'')
    Fifty_entry.delete(0,'end')
    Fifty_entry.insert(0,'')
    Twenty_entry.delete(0,'end')
    Twenty_entry.insert(0,'')
    Ten_entry.delete(0,'end')
    Ten_entry.insert(0,'')
    Five_entry.delete(0,'end')
    Five_entry.insert(0,'')
    One_entry.delete(0,'end')
    One_entry.insert(0,'')

    ComputeTotal()
    OneK_entry.focus()


#Menu
menubar=Menu(window)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Open",command=Openfile)
filemenu.add_command(label="Reset",command=reset)
filemenu.add_command(label="Print",command=Print)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=cquit)
menubar.add_cascade(label="File",menu=filemenu)

Helpmenu=Menu(menubar,tearoff=0)
Helpmenu.add_command(label="About Cash Breakdown",command=cabout)
menubar.add_cascade(label="Help",menu=Helpmenu)


window.config(menu=menubar)

def htmlprint():
    times2=time.strftime('%b'+" "+'%d'+", "+'%Y'+" @ "+'%I'+":"+'%M')
    
    file=open("cashbreakdown.html","w")
   
    file.write('<table border="0">')

    file.write("<tr>")
    file.write('<td colspan="5"><font size="5">'+times2+'</font></td>')
    file.write("</tr>")
    
    file.write("<tr>")
    file.write('<td colspan="2"><font size="10">Name   :</font></td>')
    file.write('<td colspan="3"><font size="10">'+' '+NameEnt.get()+'</font></td>')
    file.write("</tr>")
    
    file.write("<tr>")        
    file.write('<th><font size="6"><p align="center">Bill</p></font></th>')
    file.write('<th><font size="6"><p align="center"> x </p></font></th>')	
    file.write('<th><font size="6"><p align="center">Count</p></font></th>')
    file.write("<th> </th>")
    file.write('<th><font size="6"><p align="center">Total</p></font></th>')
    file.write("</tr>")

    file.write("<tr>")
    file.write('<td><font size="6"><p align="center">1000</p></font></td>')
    file.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+OneK_entry.get()+"</p></font></td>")
    file.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+str(answer_OneK)+"</p></font></td>")
    file.write("</tr>")
    
    file.write("<tr>")
    file.write('<td><font size="6"><p align="center">500</p></font></td>')
    file.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+FiveH_entry.get()+"</p></font></td>")
    file.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+str(answer_FiveH)+"</p></font></td>")
    file.write("</tr>")
               
    file.write("<tr>")
    file.write('<td><font size="6"><p align="center">200</p></font></td>')
    file.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+TwoH_entry.get()+"</p></font></td>")
    file.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+str(answer_TwoH)+"</p></font></td>")
    file.write("</tr>")
    
    file.write("<tr>")
    file.write('<td><font size="6"><p align="center">100</p></font></td>')
    file.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+OneH_entry.get()+"</p></font></td>")
    file.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+str(answer_OneH)+"</p></font></td>")
    file.write("</tr>")
               
    file.write("<tr>")
    file.write('<td><font size="6"><p align="center">50</p></font></td>')
    file.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+Fifty_entry.get()+"</p></font></td>")
    file.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+str(answer_Fifty)+"</p></font></td>")
    file.write("</tr>")
               
    file.write("<tr>")
    file.write('<td><font size="6"><p align="center">20</p></font></td>')
    file.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+Twenty_entry.get()+"</p></font></td>")
    file.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+str(answer_Twenty)+"</p></font></td>")
    file.write("</tr>")
               
    file.write("<tr>")
    file.write('<td><font size="6"><p align="center">10</p></font></td>')
    file.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+Ten_entry.get()+"</p></font></td>")
    file.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+str(answer_Ten)+"</p></font></td>")
    file.write("</tr>")
               
    file.write("<tr>")
    file.write('<td><font size="6"><p align="center">5</p></font></td>')
    file.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+Five_entry.get()+"</p></font></td>")
    file.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+str(answer_Five)+"</p></font></td>")
    file.write("</tr>")
    file.write("<tr>")
               
    file.write('<td><font size="6"><p align="center">1</p></font></td>')
    file.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+One_entry.get()+"</p></font></td>")
    file.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file.write('<td><font size="6"><p align="center">'+str(answer_One)+"</p></font></td>")
    file.write("</tr>")

    file.write("<tr>")
    file.write('<td colspan="4"><font size="8"><p align="center">Total:</p></font></td>')
    file.write('<td><font size="8"><p align="center">'+str(total)+"</p></font></td>")
    file.write("</tr>")

    file.write("</table>")

    file.close()

def htmlfile():

    times=time.strftime('%b%d%I%M')
    times2=time.strftime('%b'+" "+'%d'+", "+'%Y'+" @ "+'%I'+":"+'%M')

    newpath = r'.\Cashbreakdown' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    file1=open(r'.\Cashbreakdown\''+times+".html","w")
   
    file1.write('<table border="0">')
    file1.write("<tr>")
    file1.write('<td colspan="5"><font size="5">'+times2+'</font></td>')
    file1.write("</tr>")
    
    file1.write("<tr>")
    file1.write('<td colspan="2"><font size="8">Name   :</font></td>')
    file1.write('<td colspan="3"><font size="8">'+NameEnt.get()+'</font></td>')
    file1.write("</tr>")
    
    file1.write("<tr>")        
    file1.write('<th><font size="6"><p align="center">Bill</p></font></th>')
    file1.write('<th><font size="6"><p align="center"> x </p></font></th>')	
    file1.write('<th><font size="6"><p align="center">Count</p></font></th>')
    file1.write("<th> </th>")
    file1.write('<th><font size="6"><p align="center">Total</p></font></th>')
    file1.write("</tr>")

    file1.write("<tr>")
    file1.write('<td><font size="6"><p align="center">1000</p></font></td>')
    file1.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+OneK_entry.get()+"</p></font></td>")
    file1.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+str(answer_OneK)+"</p></font></td>")
    file1.write("</tr>")
    
    file1.write("<tr>")
    file1.write('<td><font size="6"><p align="center">500</p></font></td>')
    file1.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+FiveH_entry.get()+"</p></font></td>")
    file1.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+str(answer_FiveH)+"</p></font></td>")
    file1.write("</tr>")
               
    file1.write("<tr>")
    file1.write('<td><font size="6"><p align="center">200</p></font></td>')
    file1.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+TwoH_entry.get()+"</p></font></td>")
    file1.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+str(answer_TwoH)+"</p></font></td>")
    file1.write("</tr>")
    
    file1.write("<tr>")
    file1.write('<td><font size="6"><p align="center">100</p></font></td>')
    file1.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+OneH_entry.get()+"</p></font></td>")
    file1.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+str(answer_OneH)+"</p></font></td>")
    file1.write("</tr>")
               
    file1.write("<tr>")
    file1.write('<td><font size="6"><p align="center">50</p></font></td>')
    file1.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+Fifty_entry.get()+"</p></font></td>")
    file1.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+str(answer_Fifty)+"</p></font></td>")
    file1.write("</tr>")
               
    file1.write("<tr>")
    file1.write('<td><font size="6"><p align="center">20</p></font></td>')
    file1.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+Twenty_entry.get()+"</p></font></td>")
    file1.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+str(answer_Twenty)+"</p></font></td>")
    file1.write("</tr>")
               
    file1.write("<tr>")
    file1.write('<td><font size="6"><p align="center">10</p></font></td>')
    file1.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+Ten_entry.get()+"</p></font></td>")
    file1.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+str(answer_Ten)+"</p></font></td>")
    file1.write("</tr>")
               
    file1.write("<tr>")
    file1.write('<td><font size="6"><p align="center">5</p></font></td>')
    file1.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+Five_entry.get()+"</p></font></td>")
    file1.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+str(answer_Five)+"</p></font></td>")
    file1.write("</tr>")
    file1.write("<tr>")
               
    file1.write('<td><font size="6"><p align="center">1</p></font></td>')
    file1.write('<td><font size="6"><p align="center"> x </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+One_entry.get()+"</p></font></td>")
    file1.write('<td><font size="6"><p align="center"> = </p></font></td>')
    file1.write('<td><font size="6"><p align="center">'+str(answer_One)+"</p></font></td>")
    file1.write("</tr>")

    file1.write("<tr>")
    file1.write('<td colspan="4"><font size="8"><p align="center">Total:</p></font></td>')
    file1.write('<td><font size="8"><p align="center">'+str(total)+"</p></font></td>")
    file1.write("</tr>")

    file1.write("</table>")

    file1.close()        

def MessageError():
    tkinter.messagebox.showinfo("Wrong Input","Please input Numeric only! ")

def MessageError2():
    tkinter.messagebox.showinfo("Null Values Detected","Please input zero if value is none! ")
    
def computeOneKClick():
    computeOneKCall()


def computeOneK(enter):
    computeOneKCall()
    OneK_entry.tk_focusNext().focus()

def computeOneKCall():
    global answer_OneK
    if len(OneK_entry.get())!=0:
        try:            
            answer_OneK=0
            answer_OneK= int(OneK_entry.get()) * 1000

        except:
            MessageError()
    else:
        answer_OneK=0
            
    labelAns_OneK=Label(window,text="    "+str(answer_OneK)+"    ",font=("Arial",20))
    labelAns_OneK.grid(row=2,column=4)
    

def computeFiveHClick():
    computeFiveHCall()

def computeFiveH(enter):
    computeFiveHCall() 
    FiveH_entry.tk_focusNext().focus()
    
def computeFiveHCall():
    global answer_FiveH
    if len(FiveH_entry.get())!=0:
        try:
            global answer_FiveH
            answer_FiveH=0
            answer_FiveH= int(FiveH_entry.get()) * 500      
        except:
            MessageError()
    else:
        answer_FiveH=0
        
    labelAns_FiveH=Label(window,text="    "+str(answer_FiveH)+"    ",font=("Arial",20))
    labelAns_FiveH.grid(row=3,column=4)  

def computeTwoHClick():
    computeTwoHCall()
    
def computeTwoH(enter):
    computeTwoHCall()
    TwoH_entry.tk_focusNext().focus()

def computeTwoHCall():
    global answer_TwoH
    if len(TwoH_entry.get())!=0:
        try:            
            answer_TwoH=0
            answer_TwoH= int(TwoH_entry.get()) * 200           
        except:
            MessageError()
    else:
        answer_TwoH=0
        
    labelAns_TwoH=Label(window,text="    "+str(answer_TwoH)+"    ",font=("Arial",20))
    labelAns_TwoH.grid(row=4,column=4)

def computeOneHClick():
    computeOneHCall()

def computeOneH(enter):
    computeOneHCall()
    OneH_entry.tk_focusNext().focus()

def computeOneHCall():
    global answer_OneH
    if len(OneH_entry.get())!=0:
        try:         
            answer_OneH=0
            answer_OneH= int(OneH_entry.get()) * 100
    
        except:
            MessageError()
    else:
        answer_OneH=0
    labelAns_OneH=Label(window,text="    "+str(answer_OneH)+"    ",font=("Arial",20))
    labelAns_OneH.grid(row=5,column=4)
    

def computeFiftyClick():
    computeFiftyCall()

def computeFifty(enter):  
    computeFiftyCall()
    Fifty_entry.tk_focusNext().focus()

def computeFiftyCall():
    global answer_Fifty
    if len(Fifty_entry.get())!=0:
        try:
            answer_Fifty=0
            answer_Fifty= int(Fifty_entry.get()) * 50

        except:
            MessageError()
    else:
        answer_Fifty=0
    labelAns_Fifty=Label(window,text="    "+str(answer_Fifty)+"    ",font=("Arial",20))
    labelAns_Fifty.grid(row=6,column=4)

def computeTwentyClick():
    computeTwentyCall()

def computeTwenty(enter):
    computeTwentyCall()
    Twenty_entry.tk_focusNext().focus()

def computeTwentyCall():
    global answer_Twenty
    if len(Twenty_entry.get())!=0:    
        try:
            answer_Twenty=0
            answer_Twenty= int(Twenty_entry.get()) * 20  

            
        except:
            MessageError()
    else:
        answer_Twenty=0
    labelAns_Twenty=Label(window,text="    "+str(answer_Twenty)+"    ",font=("Arial",20))
    labelAns_Twenty.grid(row=7,column=4)

def computeTenClick():
    computeTenCall()

def computeTen(enter):
    computeTenCall()
    Ten_entry.tk_focusNext().focus()

def computeTenCall():
    global answer_Ten
    if len(Ten_entry.get())!=0:
        try:
            
            answer_Ten=0
            answer_Ten= int(Ten_entry.get()) * 10
            
        except:
            MessageError()
    else:
        answer_Ten=0
    labelAns_Ten=Label(window,text="    "+str(answer_Ten)+"    ",font=("Arial",20))
    labelAns_Ten.grid(row=8,column=4)
    
def computeFiveClick():
    computeFiveCall()
    
def computeFive(enter):
    computeFiveCall()
    Five_entry.tk_focusNext().focus()

def computeFiveCall():
    global answer_Five
    if len(Five_entry.get())!=0:
        try:
            
            answer_Five=0
            answer_Five= int(Five_entry.get()) * 5

            
        except:
            MessageError()
    else:
        answer_Five=0
    labelAns_Five=Label(window,text="    "+str(answer_Five)+"    ",font=("Arial",20))
    labelAns_Five.grid(row=9,column=4)

def computeOneClick():
    computeOneCall()
    
def computeOne(enter):
    computeOneCall()
    One_entry.tk_focusNext().focus()

def computeOneCall():
    global answer_One
    if len(One_entry.get())!=0:
        try:
            
            answer_One=0
            answer_One= int(One_entry.get()) * 1
           
        except:
            MessageError()
    else:
        answer_One=0
    labelAns_One=Label(window,text="    "+str(answer_One)+"    ",font=("Arial",20))
    labelAns_One.grid(row=10,column=4)
    
def TotalCash(event):
    ComputeTotal()

def TotalCashClick():
    ComputeTotal()

def ComputeTotal():
        
    if len(NameEnt.get())!=0: 

        global total
        computeOneKClick()
        computeFiveHClick()
        computeTwoHClick()
        computeOneHClick()
        computeFiftyClick()
        computeTwentyClick()
        computeTenClick()
        computeFiveClick()
        computeOneClick()
       
        total =answer_OneK+answer_FiveH+answer_TwoH+answer_OneH+answer_Fifty+answer_Twenty+answer_Ten+answer_Five+answer_One
               
        TotalLabel=Label(window,text="    "+str(total)+"    ",font=("Arial",25),fg="red")
        TotalLabel.grid(row=12,column=4)

        #HTML printout       
        htmlprint()
        htmlfile()
    else:
        tkinter.messagebox.showinfo("Name value is NULL","Please input your Name! ")


def entername(event):
    NameEnt.bind("<Return>",NameEnt.tk_focusNext().focus())

def ComputewhenClick(click):
    computeOneK(click)
    computeFiveH(click)
    computeTwoH(click)
    computeOneH(click)
    computeFifty(click)
    computeTwenty(click)
    computeTen(click)
    computeFive(click)
    computeOne(click)
    ComputeTotal()


#Name of POS
NameLab=Label(window,text="Name of Cashier :",font=("arial",20))
NameLab.grid(row=0,columnspan=3)

NameEnt=Entry(window,width=10,font=("Arial",20))
NameEnt.grid(row=0,column=4)
NameEnt.bind("<Return>",entername)
NameEnt.focus()

#Lining1
photo=PhotoImage(file="lining.gif")
w=Label(window,image=photo)
w.grid(row=1,columnspan=5)

#Cash breakdown
oneK_label=Label(window,text="1000",font=("arial",20))
oneK_label.grid(row=2,column=0)
fiveH_label=Label(window,text="500",font=("arial",20))
fiveH_label.grid(row=3,column=0)
twoH_label=Label(window,text="200",font=("arial",20))
twoH_label.grid(row=4,column=0)
oneH_label=Label(window,text="100",font=("arial",20))
oneH_label.grid(row=5,column=0)
fifty_label=Label(window,text="50",font=("arial",20))
fifty_label.grid(row=6,column=0)
twenty_label=Label(window,text="20",font=("arial",20))
twenty_label.grid(row=7,column=0)
ten_label=Label(window,text="10",font=("arial",20))
ten_label.grid(row=8,column=0)
five_label=Label(window,text="5",font=("arial",20))
five_label.grid(row=9,column=0)
one_label=Label(window,text="1",font=("arial",20))
one_label.grid(row=10,column=0)

#multiply sign
for i in range(2,11):
    xlabel=Label(window,text=" x ",font=("arial",20))
    xlabel.grid(row=i,column=1)

#equal sign
for i in range(2,11):
    xlabel=Label(window,text=" = ",font=("arial",20))
    xlabel.grid(row=i,column=3)

#entry

OneK_entry=Entry(window,width=5,font=("Arial",20))
OneK_entry.bind("<Return>",computeOneK)
OneK_entry.bind("<Button-1>",ComputewhenClick)
OneK_entry.grid(row=2,column=2)

FiveH_entry=Entry(window,width=5,font=("Arial",20))
FiveH_entry.grid(row=3,column=2)
FiveH_entry.bind("<Return>",computeFiveH)
FiveH_entry.bind("<Button-1>",ComputewhenClick)

TwoH_entry=Entry(window,width=5,font=("Arial",20))
TwoH_entry.grid(row=4,column=2)
TwoH_entry.bind("<Return>",computeTwoH)
TwoH_entry.bind("<Button-1>",ComputewhenClick)

OneH_entry=Entry(window,width=5,font=("Arial",20))
OneH_entry.grid(row=5,column=2)
OneH_entry.bind("<Return>",computeOneH)
OneH_entry.bind("<Button-1>",ComputewhenClick)

Fifty_entry=Entry(window,width=5,font=("Arial",20))
Fifty_entry.grid(row=6,column=2)
Fifty_entry.bind("<Return>",computeFifty)
Fifty_entry.bind("<Button-1>",ComputewhenClick)

Twenty_entry=Entry(window,width=5,font=("Arial",20))
Twenty_entry.grid(row=7,column=2)
Twenty_entry.bind("<Return>",computeTwenty)
Twenty_entry.bind("<Button-1>",ComputewhenClick)

Ten_entry=Entry(window,width=5,font=("Arial",20))
Ten_entry.grid(row=8,column=2)
Ten_entry.bind("<Return>",computeTen)
Ten_entry.bind("<Button-1>",ComputewhenClick)

Five_entry=Entry(window,width=5,font=("Arial",20))
Five_entry.grid(row=9,column=2)
Five_entry.bind("<Return>",computeFive)
Five_entry.bind("<Button-1>",ComputewhenClick)

One_entry=Entry(window,width=5,font=("Arial",20))
One_entry.grid(row=10,column=2)
One_entry.bind("<Return>",computeOne)
One_entry.bind("<Button-1>",ComputewhenClick)

#Lining2
photo2=PhotoImage(file="lining.gif")
w2=Label(window,image=photo2)
w2.grid(row=11,columnspan=5)

#Button compute
compute=Button(window,text="Total",font=("Arial",20),width=15,command=TotalCashClick)
compute.grid(row=12,columnspan=3)
compute.bind("<Return>",TotalCash)
  
window.mainloop()
