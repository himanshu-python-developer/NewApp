import io
import requests
import webbrowser
from  tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image

class NewsApp:
    
    def __init__(self):
        
        # Fach data 
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=7e18901feac448f7925ab740a2573bc4').json()
        # print(data) chake the condison 
        
        # initial GUI Load 
        self.load_gui()
        # load the First News Iteam
        self.load_news_item(0)
        
    def load_gui(self):
        self.root = Tk()
        self.root.geometry('365x490')
        self.root.title('News Applicition')
        self.root.resizable(0,0)
        self.root.config(background='black')
        
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
            
    def load_news_item(self,index):
        
        # clear the screen for new news item 
        self.clear()
        
        # image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            img = Image.open(io.BytesIO(raw_data)).resize((150,200))
            Photo = ImageTk.PhotoImage(img)
        except:
            img_url = 'https://thumbs.dreamstime.com/z/no-image-available-icon-flat-vector-no-image-available-icon-flat-vector-illustration-132482953.jpg'
            raw_data = urlopen(img_url).read()
            img = Image.open(io.BytesIO(raw_data)).resize((150,200))
            Photo = ImageTk.PhotoImage(img)            
        
        lable = Label(self.root,image=Photo) # bytes
        lable.pack()
        
        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white', wraplength=365,justify='center')
        heading.pack(pady=(16,18))
        heading.config(font=('verdana',14))
        
        
        details = Label(self.root,text=self.data['articles'][index]['description'],bg='black',fg='white', wraplength=365,justify='center')
        details.pack(pady=(2,18))
        details.config(font=('verdana',11))
        
        
        frame = Frame(self.root,bg='black')
        frame.pack(expand= True,fill=BOTH)
        if index !=0:
            prev = Button(frame,text='Prev', width= 16, height= 3,command= lambda : self.load_news_item(index-1))
            prev.pack(side=LEFT)
        
        
        read = Button(frame,text='Read More ', width= 16, height= 3,command= lambda : self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)
        if index != len(self.data['articles'])-1:
            
            next = Button(frame,text='next', width= 16, height= 3,command= lambda : self.load_news_item(index+1))
            next.pack(side=RIGHT) 
        
        
        
        self.root.mainloop()
        
    def open_link(self,url):
        webbrowser.open(url)   
    
obj = NewsApp()