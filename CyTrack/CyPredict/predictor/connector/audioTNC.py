'''
Created on Sep 26, 2016

@author: matth
'''


#plan
#   auto find com port (atelast ask for port number)
#   verify that port is good
#   background thread the serial read



'''


import serial
import threading
from threading import Thread
from queue import Queue
import AFSK.afsk as afsk

class AudioTNC():
    def __init__(self,portname,baud):
        self.qin=Queue()
        self.qout=Queue()
        self.AudioReader=AudioThread(self.qin,self.qout,portname,baud)
        self.threader = Thread(target=self.AudioReader.thread, args=())
        
    
       
    def _handle_signal(self,signal, frame):
        
        # mark the loop stopped
        # cleanup
        self.cleanup()
    
    def cleanup(self):
        print("cleaning up ...")
        self.threading.ser.close()
        
    def startAudioDat(self):    
        self.threader.start()
        
    def stopAudioDat(self):
        self.qin.put(False)
        
        
    def transmitAudioDat(self,line):
        self.qin.put(line.encode())
        
        
    def getAudioDat(self):
        if(self.qout.empty()==False):
            return self.qout.get()
        
        
        
'''
#This is the thread that is created to handle the continous loop for the serial data.
'''

class AudioThread(threading.Thread):
                
        #serialListen(ser,x)
        
    def __init__(self,qin,qout,portname,baud):
        self.qin=qin
        self.qout=qout
        self.portname=portname
        self.baud=baud
        self.running=True
        self.lines=""
        self.newLine=False
        
    def stopListening(self):
        self.running=False
            
            
            
    
    def thread(self):#this will need to be rewritten
        x=0
        print(self.portname)
        print(self.baud)
        audio = afsk.
        self.serrunning=True
        while self.running:
            if self.qin.empty()==False:
                self.line=self.qin.get()
                if self.line==False:
                    self.running=False
                    break
                ser.write(self.line)
            if ser.in_waiting!=0:
                x = ser.readline()
                self.qout.empty()
                self.qout.put(x)
                print(x)
                
        ser.close()

    
    

  
'''


