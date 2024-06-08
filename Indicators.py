from stockdata import *
def restmonth(month):
        if(month==1):
          return 31
        elif(month==2):
            return 28
        elif(month==3):
            return 31
        elif(month==4):
            return 30
        elif(month==5):
             return 31
        elif(month==6):
             return 30
        elif(month==7):
             return 31
        elif(month==8):
             return 31
        elif(month==9):
             return 30
        elif(month==10):
             return 31
        elif(month==11):
             return 30
        elif(month==12):
             return 31
        elif(month=="01"):
          return 31
        elif(month=="02"):
            return 28
        elif(month=="03"):
            return 31
        elif(month=="04"):
            return 30
        elif(month=="05"):
             return 31
        elif(month=="06"):
             return 30
        elif(month=="07"):
             return 31
        elif(month=="08"):
             return 31
        elif(month=="09"):
             return 30
        elif(month=="10"):
             return "31"
        elif(month=="11"):
             return 30
        elif(month=="12"):
             return 31
def numtostr(num):
        if(num<10):
            num='0'+str(num)
        else:
             num=str(num)
            
        return num
def getday(stock,day,year,length,month,timeframe):
       
        high, low, close = bardata(stock, timeframe, year+'-'+numtostr(month)+'-'+numtostr(day)+'T08:00:00Z','2024-06-06T16:00:00Z')
        while(length!= len(high)):
             if(len(high)<length):
                 day=day-1
                 if(day<=0):
                      month=month-1
                      if(month==0):
                           month=12
                      d=restmonth(month)
                      day=d
             high, low, close = bardata(stock, timeframe,year+'-'+numtostr(month)+'-'+numtostr(day)+'T08:00:00Z','2024-06-07T16:00:00Z')
        return high, low, close,day
class Supertrend:
    def prevATR(self, high, low, close, length):
      
        trange = 0
        
        for i in range(1, length):
           
            tr = max(high[i] - low[i], abs(high[i] - close[i-1]), abs(low[i] - close[i-1]))
            trange += tr
                    
        av = trange / length-1
        return av

    def curATR(self, h, l, c, prevatr, length):
        tr = max(h - l, abs(h - c), abs(l - c))
        print(tr)
        curatr = ((prevatr * (length - 1)) + tr) / length
        return curatr

    def supert(self, high, low, multiplier, catr):
        return (((high + low) / 2) + (multiplier * catr))

class DEMA:
     def SMA(stock,length):
          high,low,close,day = getday(stock,5,"2024",length,6,"1D")
          high,low,close,day = getday(stock,day,"2024",length,6,"5min")
          avg =0
          for i in range(length):
               avg+=close[i]
          
          sma = avg/length
          print(sma)
          
             
       
      


DEMA.SMA("SPY",50)

'''
high, low, close = bardata("SPY", "1D", '2024-01-01T00:00:00Z', '2024-01-21T00:00:00Z')
print(high)
supertrend_instance = Supertrend()

atr_length = len(low)
print(atr_length)

atr = supertrend_instance.prevATR(high, low, close, atr_length)

h, l, c = bardata("SPY", "1D", '2024-04-19T00:00:00Z', '2024-04-23T00:00:00Z')


catr = supertrend_instance.curATR(h[1], l[1], c[0], atr, atr_length-1)
ans=supertrend_instance.supert(h[1],l[1],3,catr)
print(ans)
'''