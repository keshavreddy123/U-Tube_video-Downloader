from pytube import YouTube
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as mb

td=Tk()
td.geometry('450x400')
td.title("Youtube Video Downloader")
pic = PhotoImage(file=r'F:\Mini Projects\Youtube Video Downloader\youtube-logo-png-2074.png')
td.iconphoto(FALSE,pic) # Icon

bg= PhotoImage(file=r"F:\Mini Projects\Youtube Video Downloader\25493-3-download-now-button-glossy-orange.png")
label= Label(td,image = bg)
label.place(x=0,y=0,relheight=1,relwidth=1)

def downloads():
    url =YouTube(str(e.get()))
    video = url.streams.first()
    #video = youtube.streams.get_highest_resolution() --For higher resolutions keep this. I'm gonna continue with the default because of my slower network


    video.download()
    Label(td, text = 'DOWNLOADED', font = 'arial 15').place(x= 160 , y = 0)  

e=Entry(td,  width=20,font=('Ubuntu', 15))
T = Text(td, height = 5, width = 52)
  
# Create label
l = Label(td, text = "Enter The Link Here",font =("Courier", 14))
l.place(x=120,y=80)
b=Button(td,text="Press Here",command=downloads)
e.place(x=120,y=50)
b.place(x=180,y=300)

mainloop()