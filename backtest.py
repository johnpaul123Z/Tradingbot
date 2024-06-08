from stockdata import *
from supertrend import *
class Backtest:
    def setdata(self,length,day,month):
        si = Supertrend()
        backday=day-length
        if(day-length <= 0):
            dif= day-length
            backday=30+dif
            month =month-1
        
        print(backday,month)
        high, low, close = bardata("SPY", "1H", '2024-02-02T08:00:00Z', '2024-02-02T16:00:00Z')
        

            
      
        
        print(high)
        #while(len(high!=length)):
           


b=Backtest()
b.setdata(7,4,2)