from stockdata import bardata
from datetime import datetime, timedelta
from workalendar.usa import UnitedStates

def setsupertrend(m1,l1,t1,m2,l2,t2):
    return(m1,l1,t1,m2,l2,t2)

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
    def ATR(self, high, low, close, length):
       trange = 0
       for i in range(length):
        if i == len(high) - 1:  # For the last value, no previous close to compare with
            tr = high[i] - low[i]
        else:
            tr = max(high[i] - low[i], abs(high[i] - close[i+1]), abs(low[i] - close[i+1]))
        trange += tr
        av = trange / length
        print("ATR: ",av)
        return av
    def runsupertrend(self, multiplier, atrperiod, high, low, close, ph=None, pl=None, pst=None):
        if len(high) < atrperiod:
           print("You have", len(close), "bars, and you need", atrperiod, "to run.")
           return 0, 0, 0
        high, low, close = Reverse(high), Reverse(low), Reverse(close)
        atrr = self.ATR(high, low, close, atrperiod)

        middle_value = (high[0] + low[0]) / 2
        basicUpperBand = middle_value + (multiplier * atrr)
        basicLowerBand = middle_value - (multiplier * atrr)
        upperBand = basicUpperBand
        lowerBand = basicLowerBand

        if len(ph) > 0 and len(pl) > 0:
          ph = Reverse(ph)
          pl = Reverse(pl)

        if len(close) > 1 and len(ph) > 0 and len(pl) > 0:
            upperBand = basicUpperBand if basicUpperBand < ph[0] or close[1] > ph[0] else ph[0]
            lowerBand = basicLowerBand if basicLowerBand > pl[0] or close[1] < pl[0] else pl[0]
        else:
            print("Not enough data to evaluate previous close for bands.")
            return lowerBand, upperBand,0

    
        isUpTrend = 1
        isDownTrend = -1
        trendDirection = isDownTrend  # Default to isDownTrend if no previous values

        if len(pst) != 0:
          pst = Reverse(pst)
          prev_superTrend = pst[0]

        if prev_superTrend == ph[0]:
            trendDirection = isUpTrend if close[0] > upperBand else isDownTrend
        else:
            trendDirection = isDownTrend if close[0] < lowerBand else isUpTrend

        superTrend = lowerBand if trendDirection == isUpTrend else upperBand
       

        return lowerBand, upperBand, superTrend
        
    
class DEMA:
    def SMA(length,close):
        avg=0 
        i=0
        if(len(close)<length):
            print("you have ",len(close)," bar, and you need ", length," to run" )
            return 0
        close = Reverse(close)
        while(i<length):
            
            avg+=close[i]
            i+=1
        return avg/length
   