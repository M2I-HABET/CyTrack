'''
Created on Sep 25, 2016

@author: matth
'''
#plan
#   auto find com port (atelast ask for port number)
#   verify that port is good
#   background thread the serial read






import serial
import threading
from threading import Thread
from queue import Queue


class Serial():
    def __init__(self,portname,baud):
        self.qin=Queue()
        self.qout=Queue()
        self.serialReader=SerialThread(self.qin,self.qout,portname,baud)
        self.threader = Thread(target=self.serialReader.thread, args=() )
        
    '''            
    def serial_ports(self):
            # from http://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
        """ Lists serial port names
        :raises EnvironmentError:
        On unsupported or unknown platforms
        :returns:
        A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        
        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result
        
    '''    
       
    def _handle_signal(self,signal, frame):
        
        # mark the loop stopped
        # cleanup
        self.cleanup()
    
    def cleanup(self):
        print("cleaning up ...")
        self.threading.ser.close()
        
    def startSerialDat(self):    
        self.threader.start()
        
    def stopSerialDat(self):
        self.qin.put(False)
        
        
    def writeToPort(self,line):
        self.qin.put(line.encode())
        
        
    def getFromPort(self):
        if(self.qout.empty()==False):
            return self.qout.get()
        
        
        
'''
This is the thread that is created to handle the continous loop for the serial data.
'''

class SerialThread(threading.Thread):
                
        #serialListen(ser,x)
        
    def __init__(self,qin,qout,portname,baud):
        self.qin=qin
        self.qout=qout
        self.portname=portname
        self.baud=baud
        self.serrunning=True
        self.lines=""
        self.newLine=False
        
    def stopListening(self):
        self.serrunning=False
            
            
            
    
    def thread(self):#this will need to be rewritten
        x=0
        print(self.portname)
        print(self.baud)
        ser = serial.Serial(
        port=self.portname,   
        timeout=.2,
        baudrate=self.baud,
        write_timeout=.2
        )
        self.serrunning=True
        while self.serrunning:
            if self.qin.empty()==False:
                self.line=self.qin.get()
                if self.line==False:
                    self.serrunning=False
                    break
                ser.write(self.line)
            if ser.in_waiting!=0:
                x = ser.readline()
                self.qout.empty()
                self.qout.put(x)
                print(x)
                
        ser.close()

    
    

  




'''
import time
import threading
import serial
run = True
global num
global x
global a
num=0
x=0
a=x

def base91(string):
    print string
    

def foo():
        global num
        global x
        global a
        ser = serial.Serial(
        port='COM8',
        baudrate=9600,
        parity=serial.PARITY_ODD,
        stopbits=serial.STOPBITS_TWO,
        bytesize=serial.SEVENBITS
        )
        
        while run:
            time.sleep(0)
            x = ser.readline()
            num=num+1   

        ser.close()
    

t1 = threading.Thread(target=foo)
t1.start()
while num<10:
    if x!=a:
        base91(x)

        a=x
run=False


#use https://github.com/ampledata/aprs/blob/master/aprs/decimaldegrees.py to decode

'''