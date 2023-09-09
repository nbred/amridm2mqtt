
from datetime import datetime, timedelta, date
import time

class DayFileOpener:
    mode = 'w'

    # nextDay False = today True = tomorrow , a_mode 'r' 'w' 'a' 'b' etc
    def __init__ (self, nextDay,a_mode):
        self.mode = a_mode
        newSeconds = self.calcNextStart( nextDay)
        self.createDayFile(newSeconds)
        
    def __enter__ (self):
        return self.f

    def __exit__ (self, exc_type, exc_value, traceback):
        self.f.close()
        # do more stuff
        print('Everything is over.')

    def calcNextStart(self, plusone): 
        if(plusone):
            EndDate = date.today() + timedelta(days=1) # next day
        else:
            EndDate = date.today()

        t = (EndDate.year, EndDate.month, EndDate.day, 0, 0, 0, 0, 0, 0) # 12:00 midnight 00:00 hour
        return time.mktime( t ) # in seconds

    def createDayFile(self, newSeconds):
        fileName = datetime.fromtimestamp(newSeconds).strftime("%Y-%m-%d.txt") # new text file from date
        self.f = open(fileName,self.mode)
        

# from DayFileOpener import *
#
# with DayFileOpener( False, 'a') as f:  
#       f.write("hello\n")

# or
# outfile = DayFileOpener(False, 'a')
# outfile.f.write("hello\n")
        