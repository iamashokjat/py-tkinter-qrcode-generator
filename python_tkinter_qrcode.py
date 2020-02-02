import tkinter as tk 
#pip install pyqrcode 
import pyqrcode 

win=tk.Tk()  
win.title("QR Code Generator")  
win.geometry("100x70")

#qrgenerator function to generate a qr and save as svg 
def qrgenerator():
    url=entry.get() 
    qr=pyqrcode.create(url) 
    qr.svg("myqrcode.svg",scale=10) 
    print("QR code is saved as myqrcode")  
    
#This is 'Enter URL' label
enterUrlLabel=tk.Label(win,text="Enter URL") 
enterUrlLabel.grid(row=0,column=0) 

#creating Entry to get the URL from user
entry=tk.Entry(win) 
entry.grid(row=1,column=0) 

#creating button to generate QR Code 
#clicking on this button will call the qrgenerator function
button=tk.Button(win,text="Generate QR",command=qrgenerator) 
button.grid(row=3,column=0) 

win.mainloop()