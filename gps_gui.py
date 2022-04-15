import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pps_code import *
import pandas as pd

root=tkinter.Tk()
root.title('PPS system')


#read the data file by opening dailouge box
def Upload():
    try:
        root.filename= filedialog.askopenfilename(initialdir="/downloads",title="Select a File",filetypes=(("txt files","*.txt"),("CSV files","*.csv"),("all files","*.*")))
        df=pd.read_csv(root.filename)
        print(root.filename)
        print('data uploaded !')
    except Exception as e:
        print(e)


#window1

w1=Frame(root,height=300,width=250,highlightbackground='black',highlightthickness=3)
w1.grid(row=1,column=1,padx=20,pady=20,ipady=5,ipadx=5)

root.geometry('600x600+150+150')

from datetime import *

def show():
    a=e1.get()
    b=e2.get()
    c=e3.get()
    e4.insert(0,a+' '+b+' '+c+' ')


def Clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    c1.deselect()
    e1.focus()


def finish():
    root.destroy()


today = datetime.now()
d=today.strftime('%d %b %Y   %H:%M:%S %p')
l=Label(w1,text=d,font='Arial 8')
l.grid(row=1,column=2)

l1=Label(w1,text='PPS System - Car Data Analysis',font='Arial 16 underline bold italic',pady=10,padx=10)
l2=Label(w1,text='Enter Car No :',font='Arial 10 bold',pady=5,padx=5)
e1=Entry(w1,font='Arial 10')
l3=Label(w1,text='Enter Activity :',font='Arial 10 bold',pady=5,padx=5)
e2=Entry(w1,font='Arial 10')
l4=Label(w1,text='Date :',font='Arial 10 bold',pady=5,padx=5)
l5=Label(w1,text='Analyze Results for :',font='Arial 12 underline bold italic',pady=10,padx=10,bg='light pink')
e4=Entry(w1,font='Arial 12 bold',bg='light pink')
e3=Entry(w1,font='Arial 10')
c1=Checkbutton(w1,text='Select',font= 'Arial 8' ,command=show)
b1=Button(w1,text='Upload Ground data file',fg='green',font=' Arial 10 bold',pady=5,padx=5,command=Upload)
b5=Button(w1,text='Upload SSR data file',fg='green',font=' Arial 10 bold',pady=5,padx=5,command=Upload)
b6=Button(w1,text='Upload VDR data file',fg='green',font=' Arial 10 bold',pady=5,padx=5,command=Upload)
b7=Button(w1,text='Clear',pady=5,padx=5,command=Clear)
b8=Button(w1,text='QUIT',fg='red',pady=5,padx=5,command=finish)



b2=Button(w1,text='PPS Plots',fg='blue',font='Arial 10 bold',pady=5,padx=5,command=pps_plots)
b3=Button(w1,text='Heat Load plot',fg='blue',font='Arial 10 bold',pady=5,padx=5,command=pps_plots)
b4=Button(w1,text='Generate Report',fg='blue',font='Arial 10 bold',pady=5,padx=5,command=report)

l1.grid(row=0,columnspan=3)
l2.grid(row=2,column=0,sticky=tkinter.E)
e1.grid(row=2,column=1)
l3.grid(row=3,column=0,sticky=tkinter.E)
e2.grid(row=3,column=1)
l4.grid(row=4,column=0,sticky=tkinter.E)
e3.grid(row=4,column=1)
c1.grid(row=5,column=1)
l5.grid(row=9,columnspan=2,pady=10,sticky=E)
e4.grid(row=9,column=2,sticky=E)
b1.grid(row=6,column=1,pady=5)
b5.grid(row=7,column=1,pady=5)
b6.grid(row=8,column=1,pady=5)
b2.grid(row=10,column=0,pady=5)
b3.grid(row=10,column=1,pady=5)
b4.grid(row=10,column=2,pady=5)
b7.grid(row=5,column=2)
b8.grid(row=5,column=3)

root.mainloop()