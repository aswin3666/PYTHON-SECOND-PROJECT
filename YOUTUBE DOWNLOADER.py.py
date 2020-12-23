from tkinter import*
from tkinter import font as tFont
from pytube import YouTube 
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from time import sleep
from threading import*
file_size=0
def download_video():
    global file_size
    try:
         url=url_field.get()
         print(url)
         searchbtn.config(text="please wait....")
         ob=YouTube(url)
         path=askdirectory()
         print(path)
         videos=ob.streams.first()
         print(videos)
         file_size=videos.filesize
         print(file_size)
         print(videos.title)
         videos.download(path)
         print("done")
         messagebox.showinfo("info","Downloaded")
         url_field.delete(0,END)
         searchbtn.configure(text="Download Video")
    except Exception as e:
        print(e)
        print("eroorrrr")

window=Tk()
window.configure(bg="skyblue")
window.title("You Tube Downloader")
file=PhotoImage(file='download.png')
headingIcon=Label(window,image=file)
headingIcon.pack(side=TOP)
url_field=Entry(window,bg="#C0C0C0",font="Helvetica 15")
url_field.pack(side=TOP,fill=X,padx=10)
searchbtn=Button(window,text="Download Video..",font=("verdana,18"),width="30",height="3",bg="red",fg="white",relief='ridge',command=lambda:download_video())
searchbtn.pack(side=TOP)

window.mainloop()