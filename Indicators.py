from stockdata import bardata
from datetime import datetime, timedelta
from workalendar.usa import UnitedStates



def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst

def numtostr(num):
    if num < 10:
        num = '0' + str(num)
    else:
        num = str(num)
    return num
def getday(length):
    now = datetime.now()
    a = str(now.year) + '-' + numtostr(now.month) + '-' + numtostr(now.day)
    daycount = 0
    i = 1
    cal = UnitedStates()
    arr = []

   
    year_holidays = cal.holidays(now.year)
    for holiday_date, _ in year_holidays:
        arr.append(holiday_date.strftime('%Y-%m-%d'))

    while daycount < length:
        yesterday = now - timedelta(days=i)
        year = yesterday.year
        if year_holidays and year != year_holidays[0][0].year:
            year_holidays = cal.holidays(year)
            for holiday_date, _ in year_holidays:
                arr.append(holiday_date.strftime('%Y-%m-%d'))

        dow = yesterday.weekday()
        b = str(yesterday.year) + '-' + numtostr(yesterday.month) + '-' + numtostr(yesterday.day)
        
        if dow != 5 and dow != 6 and b not in arr:
            daycount += 1

        i += 1

    return b, a

class Supertrend:
    def prevATR(self, high, low, close, length):
      
        trange = 0
        
        for i in range(1, length):
           
            tr = max(high[i] - low[i], abs(high[i] - close[i-1]), abs(low[i] - close[i-1]))
            trange += tr
                    
        av = trange / (length-1)
        
        return av

    def curATR(self, h, l, c, prevatr, length):
        tr = max(h - l, abs(h - c), abs(l - c))
        
        curatr = ((prevatr * (length - 2)) + tr) / (length - 1)
        print("ATR: ",curatr)
        return curatr       
    def runsupertrend(self,multiplier,atr,high,low,close):
        '''
        b, a = getday(atr+1)
        a=a+ 'T00:00:00Z'
        b=b+'T00:00:00Z'
        high, low, close = bardata(ticker, timeframe,b, a)
        '''
        if(len(high)<atr):
            print("you have ",len(high),"and you need ", atr," to run" )
            return 0
        high, low, close = Reverse(high), Reverse(low), Reverse(close)
        prev=self.prevATR(high, low, close, atr)
        curatr = self.curATR(high[0], low[0], close[1], prev, atr)
        middle_value = (high[0] + low[0]) / 2
        low = middle_value - (multiplier * curatr)
        high = middle_value + (multiplier * curatr)
        return high,low
        
       
class DEMA:
    def SMA(ticker,timeframe, length):
        b, a = getday(20)
        a=a+ 'T00:00:00Z'
        b=b+'T00:00:00Z'
        high, low, close = bardata(ticker, timeframe,b, a)
        avg=0        
        i=0
        
        
        close = Reverse(close)
        while(i<length):
            
            avg+=close[i]
            i+=1
        return avg/length