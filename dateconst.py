# Fyers Script naming
WEEKLY = 1
MONTHEND = 0

#WEEKLY = 0
#MONTHEND = 1

# Important value to adjuect every Week       
YEAR = "22"
MONTH = "6"
DATE = "16"

#YEAR = "22"
#MONTH = "MAR"
#DATE = "17"

# https://myapi.fyers.in/docs/#section/Symbology-Possible-Values
#101122033158492,NIFTY 22 Mar 31 16550 PE,14,50,0.05,,0915-1530|1815-1915:17,2022-03-11,1648737000,NSE:NIFTY22MAR16550PE,10,11,58492,NIFTY,26000,16550.0,PE
#101122032445962,NIFTY 22 Mar 24 15350 PE,14,50,0.05,,0915-1530|1815-1915:17,2022-03-11,1648132200,NSE:NIFTY2232415350PE,10,11,45962,NIFTY,26000,15350.0,PE
#Equity Options (Monthly Expiry)	{Ex}:{Ex_UnderlyingSymbol}{YY}{MMM}{Strike}{Opt_Type}	
#NSE:NIFTY20OCT11000CE,
#NSE:BANKNIFTY20NOV25000PE
#Equity Options (Weekly Expiry)	{Ex}:{Ex_UnderlyingSymbol}{YY}{M}{dd}{Strike}{Opt_Type}	
#NSE:NIFTY20O0811000CE,
#NSE:BANKNIFTY20 N 05 25000PE,
#NSE:NIFTY20D1025000CE -->D for Dec