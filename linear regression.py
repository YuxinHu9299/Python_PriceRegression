
pip install pandas
pip install pandas_datareader
conda install statsmodels
conda install numpy

import numpy as np
import pandas_datareader.data as dtr
import statsmodels.formula.api as smf

tickers = ['fb','aapl','amzn','nflx','goog','^gspc']
D=dtr.DataReader(tickers,"yahoo")
type(D)

D.tail()

price = D['Adj Close']
price.tail()

price2 = price.shift(periods = 1)
# if use shift(1), shift base on 'periods'
price2.tail()

dailyreturn = price / price2 -1
dailyreturn.head()

dailyreturn.tail()

R = dailyreturn.tail(100)
R.columns

R = R.rename(columns = {'^gspc':'SnP'})
#R.rename(columns = {'^gspc':'SnP'},inplace = True)
#also could use R.rename(columns = {'^gspc':'SnP'},inplace = True) to redefine R
R.tail()

results = smf.ols(formula = 'fb ~ SnP',data = R).fit()
results.params

mystocks = dailyreturn.columns[:5]
type(mystocks)


betalist = []

for mystock in mystocks:
    myformula = mystock + "~ SnP"
    print(myformula)
    results = smf.ols(formula = myformula,data = R).fit()
    print(results.params['SnP'])
    betalist.append(results.params['SnP'])

betalist
beta = np.array(betalist)


notional = 100
notional * beta
sum(notional * beta)
