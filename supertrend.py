from stockdata import *
class supertrend:
    
    def prevATR(high,low,close):
      
       size=high.size()
       i=0
       print(size)
       trange=0
       while(i<size):
           trange += max(high[i] -low[i],high[i]-abs(close[i-1]),abs(low[i]-close[i-1]))
           i+=1 
        
       av = ( 1/size) *trange
       
       return av 
    def curATR(h,l,c,prevatr,size):
        atr += max(h -l,h-abs(c),abs(l-c))
        ans = prevatr(size-1)+atr
        return ans


high, low, close = bardata("SPY", "1D",'2024-05-21T00:00:00Z','2024-05-24T00:00:00Z')
atr=supertrend.prevATR(high,low,close,)






