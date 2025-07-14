import pandas as pd
import yfinance as yf

msft = yf.Ticker("MSFT")    #create ticker object of microsoft stock (the parameter for microsoft is MSFT)
msft_data = msft.history(period="max")  #extracting stock history of microsoft, max means maximum data avalaible needs to be extracted.
#other period attribute can be used such as 5d, 3mo, 6y, ytd(for data since beginning of this year) and etc

print(msft_data.head())    #prints stock data as panda's dataframe