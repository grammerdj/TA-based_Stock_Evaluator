class technicalBuildout:

    """ Class Documentation: 
    
            This class takes in historical data and builds out the dataframe with common technical indicators. Right now, the list of indicators calculated will be daily MACD histogram, 13 day EMA, 26 day EMA, 200 day EMA, ADX, 13-Day force Index, and Stochastic. There will also be fields associated with each of these having boolean values associated with common signals.
            
     """


    """ User Comment:
    
        One of the large problems I think I am running into is that the software has a hard time telling when the technical indicator is about to turn. I think I need to add a filter in there that says - hey, if this is at super high levels, please do not respond to this signal.
    
    """

    

#Important: Here is the list comprehension for +/- slope of something: [(list[i] > list[i-1]) if ((i>0)&(not pd.isnull(list[i-1]))) else False for i in range(len(list))]

    def __init__(self, hdf):
        self.index = hdf.index
        self.length = len(hdf)
        self.adj_close = hdf["Adj Close"]
        self.volume = hdf["Volume"]
        self.open = hdf["Open"]
        self.close = hdf["Close"]
        self.high = hdf["High"]
        self.low = hdf["Low"]
        self.spread = (self.close-self.open)/self.open
        self.range = (self.high-self.low)

    def _reduce(list, averaging):

        import numpy as np
        
        avgs = []

        for level in list:
            ls = []
            for sup in list:
               if (sup <= level+averaging) & (sup >= level-averaging):
                    ls.append(sup)
            
            avgs.append(np.mean(ls).round(2))
        return(np.unique(avgs))
        
    
    def market_state(self, hdf):

        import pandas as pd
        import numpy as np
        from scipy.signal import argrelextrema
        
        
        trend = []
        
        min_idx = argrelextrema(np.array(self.adj_close), np.less_equal, order=4)[0]
        max_idx = argrelextrema(np.array(self.adj_close), np.greater_equal, order=4)[0]
        for idx in range(len(self.adj_close)):
            mins = [i for i in min_idx if i <idx]
            maxs = [i for i in max_idx if i <idx]
            if len(mins) >= 2:
                min_val = self.adj_close.iloc[mins[-2:]]
                if (min_val.iloc[1] >= min_val.iloc[0]*1.025):
                    trend.append("Uptrend")
                elif len(maxs) >= 2:
                    max_val = self.adj_close.iloc[maxs[-2:]]
                    if (max_val.iloc[0] >= max_val.iloc[1]*1.025):
                        trend.append("Downtrend")
                    else:
                        trend.append("TradingRange")
                else:
                     trend.append(None)
            elif len(maxs) >= 2:
                max_val = self.adj_close.iloc[maxs[-2:]]
                if (max_val.iloc[0] >= max_val.iloc[1]*1.05):
                    trend.append("Downtrend")
                else:
                    trend.append("TradingRange")
            else:
                trend.append(None)
        hdf["Market_State"] = trend
        return(hdf)
    
    def add_emas(self, hdf, fast=11, slow=26, trend=200):

        import pandas as pd
        import pandas_ta as ta

        self.emas = [fast, slow, trend]
        emafast = ta.ema(self.adj_close, length=fast)
        emafastslope = [emafast.iloc[i] - emafast.iloc[i-1] if ((i>0)&(not pd.isnull(emafast.iloc[i]))) else None for i in range(len(emafast))]
        emafastsecdx = [emafastslope[i] - emafastslope[i-1] if ((i>0)&(not pd.isnull(emafastslope[i]))) else None for i in range(len(emafastslope))]
        emaslow = ta.ema(self.adj_close, length=slow)
        emaslowslope = [emaslow.iloc[i] - emaslow.iloc[i-1] if ((i>0)&(not pd.isnull(emaslow.iloc[i]))) else None for i in range(len(emaslow))]
        emaslowsecdx = [emaslowslope[i] - emaslowslope[i-1] if ((i>0)&(not pd.isnull(emaslowslope[i]))) else None for i in range(len(emaslowslope))]
        hdf["emaFast"] = emafast
        hdf["emaFastSlope"] = emafastslope
        slopebinf = []
        for sl in emafastslope:
            if sl == None:
                slopebinf.append(None)
            elif sl > 0:
                slopebinf.append("Increasing")
            else:
                slopebinf.append("Decreasing")
        hdf["emaFastSlopeBin"] = slopebinf
        hdf["emaFastSecondDerivative"] = emafastsecdx
        hdf["emaSlow"] = emaslow
        hdf["emaSlowSlope"] = emaslowslope
        slopebins = []
        for sl in emaslowslope:
            if sl == None:
                slopebins.append(None)
            elif sl > 0:
                slopebins.append("Increasing")
            else:
                slopebins.append("Decreasing")
        hdf["emaSlowSlopeBin"] = slopebins
        hdf["emaSlowSecondDerivative"] = emaslowsecdx
        crossover = [emafast.iloc[i] > emaslow.iloc[i] if (not pd.isnull(emaslow.iloc[i])) else None for i in range(len(emaslow))]
        hdf["emaCrossover"] = [((crossover[i] == True) & (crossover[i-1] == False)) if (not pd.isnull(crossover[i])) else None for i in range(len(crossover))]
        ematrend = ta.ema(self.adj_close, length=trend)
        hdf["emaTrend"] = [(self.adj_close.iloc[i] > ematrend.iloc[i]) if ((i>0)&(not pd.isnull(ematrend.iloc[i]))) else None for i in range(len(ematrend))]
        emasignal = []
        for idx in range(len(self.close)):
            state = hdf["Market_State"].iloc[idx]
            if hdf["Market_State"].iloc[idx] != None:
                if (state == "Uptrend") & (self.close.iloc[idx] < hdf["emaFast"].iloc[idx]):
                    emasignal.append("Buy")
                elif (state == "Downtrend") & (self.close.iloc[idx] > hdf["emaFast"].iloc[idx]):
                    emasignal.append("Short")
                else:
                    emasignal.append("Hold")
            else:
                emasignal.append(None)
        hdf["emaSignal"] = emasignal
        
        return(hdf)
        

    
    def add_macd(self, hdf, fast=12, slow=26, signal=9):

        import talib
        import pandas as pd
        import numpy as np
        
        macd, signalma, histogram = talib.MACD(self.adj_close, fast, slow, signal)
        self.macd = [fast, slow, signal]
        hdf["rawMACD"] = macd
        hdf["signalMACD"] = signalma
        hdf["histogramMACD"] = histogram
        hi = np.array(histogram)
        state = []
        for st in hi:
            if st == None:
                state.append(None)
            elif st > 0:
                state.append("Positive")
            else:
                state.append("Negative")
        hdf["histMACDState"] = state
        slope = [(hi[i] > hi[i-1]) if ((i>0)&(not pd.isnull(hi[i-1]))) else None for i in range(len(hi))]
        hdf["slopeMACD"] = slope
        slopebin = []
        for sl in slope:
            if sl == None:
                slopebin.append(None)
            elif sl > 0:
                slopebin.append("Increasing")
            else:
                slopebin.append("Decreasing")
        hdf["slopeMACDBin"] = slopebin
        return(hdf)
        

    def add_adx(self, hdf, length=14, matype = "ema"):

        import pandas as pd
        import pandas_ta as ta
        
        self.adx = [length, matype]
        adx_df = ta.adx(self.high, self.low, self.close, timeperiod=length, mamode = matype)
        adx = adx_df[f"ADX_{length}"]
        hdf["ADX"] = adx
        hdf["slopeADX"] = [(adx.iloc[i] > adx.iloc[i-1]) if ((i>0)&(not pd.isnull(adx.iloc[i-1]))) else None for i in range(len(adx))]
        hdf["posDI"] = adx_df[f"DMP_{length}"]
        hdf["negDI"] = adx_df[f"DMN_{length}"]
        state = []
        for idx in range(len(adx)):
            if adx.iloc[idx] == None:
                state.append(None)
            elif adx_df[f"DMP_{length}"].iloc[idx] > adx_df[f"DMN_{length}"].iloc[idx]:
                state.append("Positive")
            else:
                state.append("Negative")

        hdf["stateDI"] = state
        return(hdf)

    
    def add_FI(self, hdf, length=13, matype = "ema"):

        """Indicator: Elder's Force Index (EFI)
             Source: https://tradingstrategy.ai/docs/_modules/pandas_ta/volume/efi.html
        """

        import numpy as np
        import pandas as pd
        import pandas_ta as ta
        
        
        self.FI = length
        pv_diff = self.adj_close.diff() * self.volume
        efi = ta.ma(matype, pv_diff, length=length)
        hdf[f"fi{length}"] = efi
        posneg = [True if (i>=0) else np.NaN if i == np.NaN else False for i in efi]
        hdf["fiPositiveCrossover"] = [((posneg[i] ==True) & (posneg[i-1]==False)) if ((i>0)&(not pd.isnull(posneg[i-1]))) else False for i in range(len(posneg))]
        slope = [(efi.iloc[i] > efi.iloc[i-1]) if ((i>0)&(not pd.isnull(efi.iloc[i-1]))) else None for i in range(len(efi))]
        hdf["fiSlope"] = slope
        slopebin = []
        for sl in slope:
            if sl == None:
                slopebin.append(None)
            elif sl > 0:
                slopebin.append("Increasing")
            else:
                slopebin.append("Decreasing")
        hdf["fiSlopeBin"] = slopebin
        return(hdf)

    
    def add_stochastic(self, hdf, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):

        import talib
        import pandas as pd
        
        slowk, slowd = talib.STOCH(self.high, self.low, self.close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
        hdf["stochK"] = slowk
        hdf["stochD"] = slowd
        slope = [((slowk.iloc[i] > slowk.iloc[i-1]) & (slowd.iloc[i] > slowd.iloc[i-1])) if ((i>0)&(not pd.isnull(slowd.iloc[i-1]))) else None for i in range(len(slowd))]
        hdf["slopeStoch"] = slope
        slopebin = []
        for sl in slope:
            if sl == None:
                slopebin.append(None)
            elif sl > 0:
                slopebin.append("Increasing")
            else:
                slopebin.append("Decreasing")
        hdf["slopeStochBin"] = slopebin
        hdf["Overbought"] = [(slowk.iloc[i] > 80) and (slowd.iloc[i] > 80) if not pd.isnull(slowd.iloc[i]) else None for i in range(len(slowd))]
        hdf["Oversold"] = [(slowk.iloc[i] < 20) and (slowd.iloc[i] < 20) if not pd.isnull(slowd.iloc[i]) else None for i in range(len(slowd))]
        return(hdf)
    


    """
    Defining characteristics of a kangeroo tail are a long spike (wide range) that protrudes in the direction of the trend out of a tight weave of prices.
    I am going to define the kangeroo tail mathematically as follows - range of tail is > 2X range of the 2 bars preceding it, tail is at least as long 
    in the direction of the trend as .75*preceding_bar. 
    """

    def finger_pattern(self, hdf):

        import numpy as np
        
        list = [None, None, None, None]
        for idx in range(4, len(self.range)):
            rop_and_now= np.max([self.range.iloc[idx + i] for i in [-3, -2, 0]])
            range_of_tail = self.range.iloc[idx - 1]
            if (range_of_tail >= 2 * rop_and_now):
                if hdf["emaSlowSlope"].iloc[idx-2] > 0:
                    if self.high.iloc[idx - 1] > (self.high.iloc[idx-2] + .75*(self.high.iloc[idx-2] - self.low.iloc[idx-2])):
                        list.append("Up")
                    else:
                        list.append("Not")
                else:
                    if self.low.iloc[idx-1] < (self.low.iloc[idx-2] - .75*(self.high.iloc[idx-2] - self.low.iloc[idx-2])):
                        list.append("Down")
                    else:
                        list.append("Not")
            else:
                list.append("Not")
        hdf["Finger"] = list
        return(hdf)

    def add_bollinger(self, hdf, malength=20, sdmultiplier=2, widthaverage = 5):

        import numpy as np
        import pandas as pd
        
        sma = []
        sd = []
        for idx in range(len(self.adj_close)):
            if idx < malength:
                sma.append(None)
                sd.append(None)
            else:
                mean = np.mean(self.adj_close.iloc[idx-malength:idx])
                dev = np.std(self.adj_close.iloc[idx-malength:idx])
                sma.append(mean)
                sd.append(dev)
        upper_band = []
        lower_band = []
        for idx in range(len(sd)):
            if sd[idx] == None:
                upper_band.append(None)
                lower_band.append(None)
            else:
                upper_band.append(sma[idx] + sd[idx]*sdmultiplier)
                lower_band.append(sma[idx] - sd[idx]*sdmultiplier)

        band_breach = []
        for idx in range(len(sd)):
            if sd[idx] == None:
                band_breach.append(None)

            elif self.adj_close.iloc[idx] > upper_band[idx]:
                
                band_breach.append("Upper Breach")
                
            elif self.adj_close.iloc[idx] < lower_band[idx]:
                
                band_breach.append("Lower Breach")

            else:
                
                band_breach.append("Stable")

        
        delta_band_width = []
        for idx in range(len(sd)):
            
            if idx < malength + widthaverage:

                delta_band_width.append(None)

            else:

                fivedayavg = np.mean([upper_band[i]-lower_band[i] for i in range(idx-widthaverage, idx)])
                percentchange = ((upper_band[idx] - lower_band[idx]) - fivedayavg)/fivedayavg
                delta_band_width.append(percentchange)

        hdf["upperBollinger"] = upper_band
        hdf["lowerBollinger"] = lower_band
        hdf["bollingerBreach"] = band_breach
        hdf["deltaBollinger"] = delta_band_width
        return hdf
                


    def add_atr(self, hdf, timeperiod = 14):

        import talib
        import pandas as pd

        atr_raw = talib.ATR(self.high, self.low, self.close, timeperiod=14)
        atr_onepointfive = atr_raw * 1.5
        atr_percent = round((atr_onepointfive / self.close)*100, 4)
        hdf["1.5 ATR Percent"] = atr_percent 
        return hdf

                        
                                     
        
    def technical_buildout(self, hdf, returnwindow = 5, emaFast=11, emaSlow=26, emaTrend=200, macdFast=12, macdSlow=26, macdSignal=9, adxLength=14, adxMAType = "ema", fiLength=13, fiMAType = "ema", stochFastKPeriod=5, stochSlowKPeriod=3, stochSlowKMAType=0, stochSlowDPeriod=3, stochSlowdMAType=0, bandMALength=20, sdMultiplier=2, timeperiodATR = 14):
        
        import pandas as pd


        #hdf = self.add_return(hdf, returnwindow)
        hdf = self.market_state(hdf)
        hdf = self.add_emas(hdf, emaFast, emaSlow, emaTrend)
        hdf = self.add_macd(hdf, macdFast, macdSlow, macdSignal)
        hdf = self.add_adx(hdf, adxLength, adxMAType)
        hdf = self.add_FI(hdf, fiLength, fiMAType)
        hdf = self.add_stochastic(hdf, stochFastKPeriod, stochSlowKPeriod, stochSlowKMAType, stochSlowDPeriod, stochSlowdMAType)
        hdf = self.finger_pattern(hdf)
        hdf = self.add_bollinger(hdf, bandMALength, sdMultiplier)
        hdf = self.add_atr(hdf, timeperiodATR)
        hdf = hdf.dropna()
        return(hdf)



        """
    CAVEAT: This is assuming you identify a stock, place an order that executes at market close on a day, and then sell X days later (inclusive) at market close.
    """
    def add_return(hdf, time = 5, threshold = 2):

        import pandas as pd
        import numpy as np

        returns = []
        for idx in range(len(hdf)-time):
            highs = list(hdf["High"].iloc[idx+1:idx+time+1])
            max = np.max(highs)
            index = highs.index(max) + 1
            percent_return = ((max - hdf["Open"].iloc[idx+1]) /  hdf["Open"].iloc[idx+1])*100
            returns.append(percent_return)
        for idx in range(len(hdf)-time, len(hdf)):
            returns.append(None)

        lowest_value = []
        for idx in range(len(hdf)-time):
            if index == 1:
                min = hdf["Low"].iloc[idx+1]
            else:
                min = np.min(hdf["Low"].iloc[idx+1:idx+index+1])
            percent_below = ((min - hdf["Open"].iloc[idx+1]) /  hdf["Open"].iloc[idx+1])*100
            lowest_value.append(percent_below)
        for idx in range(len(hdf)-time, len(hdf)):
            lowest_value.append(None)

        benchmark = []
        for ret in returns:
            if ret == None:
                benchmark.append(None)
            elif ret >= (threshold):
                benchmark.append("Good")
            else:
                benchmark.append("Bad")

        
                
        hdf["Return"] = returns
        hdf["Return_Status"] = benchmark
        hdf["Lowest_Value"] = lowest_value
        return hdf

    """
        I am not sure how to build this out yet where the computer could analyze whether or not a stock is approaching support or resistance. This problem
        encompasses a logarithmic problem - since their inception, stocks often increase a lot - tens of thousands of basis points. In order to accurately
        draw support and resistance levels at the granularity that I want - trading in weeks/days, not months - I would need to find a way to draw support 
        and resistance in a certain time period and price range. This takes a lot of computational power and would be a function of improving an already built 
        model (and doing a lot of math). Therefore, I include this function to help plot the last year of support and resistance, to manually assess.
    """
    def add_support_and_resistance(self, percent = .05, length = 20, time_days = 250):
    
        import pandas as pd
        import numpy as np
        from scipy.signal import argrelextrema
        import matplotlib.pyplot as plt

        max = argrelextrema(np.array(self.close.iloc[-time_days:-1]), np.greater_equal, order=20)[0].tolist()
        min = argrelextrema(np.array(self.close.iloc[-time_days:-1]), np.less_equal, order=20)[0].tolist()
        max.extend(min)
        ex = self.close[-time_days:-1].iloc[max] 
        trading_range = np.max(self.close.iloc[-time_days:-1]) - np.min(self.close.iloc[-time_days:-1])
        averaging = trading_range * percent
        rough = technicalBuildout._reduce(ex, averaging)
        smooth = technicalBuildout._reduce(rough, averaging)
        return(smooth)
        plt.plot(self.index[-time_days:], self.close.iloc[-time_days:])
        plt.hlines(smooth, xmin = self.index[-time_days], xmax = self.index[-1])



    def plot_line_chart(self, hdf, price, length=250, bollinger = True, fastEma = True, slowEMA=True, supportAndResistance = True):

        import matplotlib.pyplot as plt
        import pandas as pd

        colors = {"Uptrend": "g", "Downtrend": "r", "TradingRange": "b"}
        plt.scatter(self.index[-length:], hdf[price].iloc[-length:], )
        



                
                
            
        
        



                        
        

        

        
                
