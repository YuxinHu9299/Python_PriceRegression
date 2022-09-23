#!/usr/bin/env python
# coding: utf-8

# In[120]:


pip install pandas


# In[121]:


pip install pandas_datareader


# In[122]:


conda install statsmodels


# In[123]:


conda install numpy


# In[124]:


import numpy as np


# In[125]:


import pandas_datareader.data as dtr


# In[126]:


import statsmodels.formula.api as smf


# In[127]:


tickers = ['fb','aapl','amzn','nflx','goog','^gspc']
D=dtr.DataReader(tickers,"yahoo")
type(D)


# In[128]:


D.tail()


# In[129]:


price = D['Adj Close']
price.tail()


# In[130]:


price2 = price.shift(periods = 1)
# if use shift(1), it default shift base on 'periods'
price2.tail()


# In[131]:


dailyreturn = price / price2 -1
dailyreturn.head()


# In[132]:


#dailyreturn2 = price.pct_change()
#dailyreturn2.head()


# In[133]:


dailyreturn.tail()


# In[134]:


R = dailyreturn.tail(100)


# In[135]:


R.columns


# In[136]:


#R.rename(columns = {'^gspc':'SnP'},inplace = True)
#R.tail()
R = R.rename(columns = {'^gspc':'SnP'})
#also could use R.rename(columns = {'^gspc':'SnP'},inplace = True) to redefine R
R.tail()


# In[137]:


results = smf.ols(formula = 'fb ~ SnP',data = R).fit()


# In[138]:


results.params


# In[139]:


mystocks = dailyreturn.columns[:5]


# In[140]:


mystocks


# In[141]:


type(mystocks)


# In[142]:


betalist = []

for mystock in mystocks:
    myformula = mystock + "~ SnP"
    print(myformula)
    results = smf.ols(formula = myformula,data = R).fit()
    print(results.params['SnP'])
    betalist.append(results.params['SnP'])


# In[146]:


betalist
beta = np.array(betalist)


# In[147]:


notional = 100
notional * beta
sum(notional * beta)


# In[ ]:





# In[ ]:




