# OptionData
NSE Option Data

Data will be uploading every day.
This pyc fiel will run on python version 3.10.4.
Anyone can update dateconsr.py, and fyers_token to save data

To Load data online from market, we need to run:
> python HistVixCompare.pyc

To Load data Offline for todays date:
> python HistVixCompare.pyc --offline --folder Jun-08-2022

To Load data Offline for a specific folder loaded at github:
> python HistVixCompare.pyc --offline --folder Jun-08-2022

To load data from a start date:
 > python HistVixCompare.pyc --startdate 165483270
 Where time input is in epoch. You can find epoch time 
 using python as below:
 > import datetime

 > epoch = datetime.datetime(2021, 7, 7, 0, 0, 0).timestamp()
 
 > print(epoch)