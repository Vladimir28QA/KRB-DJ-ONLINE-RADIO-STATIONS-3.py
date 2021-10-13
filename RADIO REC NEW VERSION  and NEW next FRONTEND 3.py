import sys, time, threading
# pip install python-vlc

import vlc
from guiradio import * 
from time import strftime
from tkinter import filedialog
import pygame

import tkinter.font as TkFont
#import mp3play
from pygame import mixer

import imageio
from PIL import Image, ImageTk


from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import win32com.client as mouth
import wx
 


 



voice = mouth.Dispatch("SAPI.SpVoice") 
word_to_say = " welcome Vladimir your online DJ radio  and ,your real time,and date is",strftime('%H:%M:%S - %d.%m.%Y') 
voice.Speak(word_to_say)   

canals=[]

songflag=0

def thread(my_func):
    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        my_thread.start()
    return wrapper

@thread
def playradio(canal):
    
    #import win32com.client as mouth
    #voice = mouth.Dispatch("SAPI.SpVoice") 
    #word_to_say = " play station"# time is,strftime('%H:%M:%S') 
    #voice.Speak(word_to_say)    
    
    global songflag
    songflag=1
    ppp = vlc.MediaPlayer(canal)
    ppp.play()

    while songflag==1:
        time.sleep(0.7)
    ppp.stop()

  
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        global canals
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        f=open('My radio online.txt','r',encoding='UTF-8')
     
            
        for x in f:
            mas=x.split('|')
            name=mas[0]
        
        
        
            self.ui.listView.addItem(name)
            canal=mas[0]
           
            canals.append(x)
        self.ui.pushButton_5.clicked.connect(self.openPlayList)     
        self.ui.pushButton_3.clicked.connect(self.help)                
        self.ui.pushButton.clicked.connect(self.PlayMusic)
        self.ui.pushButton_2.clicked.connect(self.StopMusic)
        self.ui.listView.currentTextChanged.connect(self.PlayMusic)



    
 
                     
   
    
  
    def openPlayList(self):
        import subprocess as sp
        programName = "notepad.exe"
        # This is name for txt file"
        fileName = "My radio online.txt"
        #My radio online.txt"
        sp.Popen([programName, fileName])                             
                         
    def help(self):                 
        webbrowser.open("https://forum.lugasat.org.ua/viewtopic.php?t=965") 
        webbrowser.open (" https://www.aimp.ru/forum/index.php?topic=22023.6675")  
    
        
         
  
    
    
    
    def PlayMusic(self):
        global songflag
        songflag=0
        time.sleep(1)
       
        name=self.ui.listView.currentItem().text()
        for x in canals:
            
            if name in x:
                mas=x.split('|')
              
                canal=mas[1].strip()
                print(name)
               
                playradio(canal)
            
                                           



    def StopMusic(self):
        global songflag

        songflag=0
        time.sleep(1)
        
     
        
    def set_volume(v):
        global vol
        global player
        #either get the new volume from given argument v (type: str):
        value = int(v)
        #or get it directly from Scale widget (type: int)
        value = vol.get()
        player.audio_set_volume(value)        
        
        vol = Scale(..., command=set_volume)          
    def show_value(self):
        global player
        i = vol.get()
        player.audio_set_volume(i)        
   
   
   
        vol = Scale(root,from_ = 0,to = 100,orient = HORIZONTAL ,resolution = 1) 
        vol.place(x=75, y = 300)
        vol.set(50)        
     
           #song = ""
                             
 

    def closeEvent(self,event):
        
        
        
        import win32com.client as mouth
        voice = mouth.Dispatch("SAPI.SpVoice") 
        word_to_say = '''Goodbye, thank you for listening to online 
        radio stations well If you want to add a new radio station or 
        replace the old one you need to add to the folder of the text 
        document python the 
        link address of the online radio stream I hope our information helped'''
        voice.Speak(word_to_say)          
        StopMusic()
        event.accept()  
        
        
        
     
        instance = vlc.Instance()   
        from PyQt5 import QtCore, QtGui, QtWidgets

        
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Main Radio")
        MainWindow.resize(298, 411)
                        

             
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(158, 338, 121, 53))
        self.pushButton_5.setObjectName("pushButton")          
       
        self.pushButton_5.setStyleSheet("QPushButton"
                             "{"
                             "background-color :yellow;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : lightgreen;"
                             "}"
                             )                
          
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(18, 338, 121,53))
        
        self.pushButton_3.setObjectName("pushButton")        
        
        self.pushButton_3.setStyleSheet("QPushButton"
                             "{"
                             "background-color : dodgerblue ;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : lightgreen;"
                             "}"
                             )                        
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(18, 20, 122, 53))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton"
                             "{"
                             "background-color :  seagreen;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : lightgreen;"
                             "}"
                             )                
        
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(157, 20, 122, 53))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton"
                             "{"
                             "background-color :indianred ;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}"
                             )        
        
        
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(18, 80, 261, 250))
        self.listView.setObjectName("listView")
        
        self.listView.setStyleSheet("background-color: lightseagreen;  border: 1px solid roylblue;   border: 1px solid springgreen;  foreground-color: text lightgreen;") 
       
        MainWindow.setCentralWidget(self.centralwidget)
        
        
        
  
       
        # creating a label widget
          # 
    
          
          # setting up background color
        #self.pushButton_5.setStyleSheet("background-color: royalblue; border: 1px solid gray;")
    
          # creating a label widget
       
    
          # setting up background color and border
        #self.pushButton_3.setStyleSheet("background-color: yellow;   border: 1px solid roylblue;")
                                    
    
          # show all the widgets
        
                
        
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
       
        MainWindow.setWindowTitle(_translate("MainWindow","MainWindow"))
        self.pushButton.setText(_translate("MainWindow","PLAY\n►\nRadio"))
        self.pushButton_2.setText(_translate("MainWindow","STOP\n⬛\nRadio"))  
        self.pushButton_3.setText(_translate("MainWindow","🔎 RADIO\n Stream")) 
        self.pushButton_5.setText(_translate("MainWindow","OPEN TXT\nList  📂")) 

     
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
   
    myapp = MyWin()

    myapp.setWindowTitle('KRB<))DJ((>ONLINE RADIO STATIONS')
  
    myapp.setStyleSheet("background-color: royalblue; border: 3px solid blue; border: 2px solid springgreen;")
    myapp.setFixedSize(298, 411)
    myapp.show()
    sys.exit(app.exec_())  
    openPlayList()
    
    
    help() 
 
    
    
    

    
    
