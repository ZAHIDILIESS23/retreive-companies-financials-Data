#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go
import requests
import pandas as pd


# In[90]:


import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=AMZN&interval=5min&apikey=UNWGJY8A55P2VSOR'
r = requests.get(url).json()
d=r['annualReports']
count=0
for item in d:
    if count==0:
        d=r['annualReports']
        d=d[0]
        incomeinitial=pd.DataFrame(list(d.items()),columns=['item','value'])
    count=count+1
    if count >3:
        continue
    d=r['annualReports']
    d=d[count]
    incomeinitial2=pd.DataFrame(list(d.items()),columns=['item','value'])
    incomeinitial=incomeinitial.merge(incomeinitial2,on="item",how='left')
    
incomeinitial   
incomeinitial.columns=incomeinitial.loc[0]
incomeinitial=incomeinitial[2:]
incomeinitial





    
  
       

    

    


# In[91]:


REV_1=incomeinitial[incomeinitial['fiscalDateEnding']=="totalRevenue"].iloc[0][1]
COV_1=incomeinitial[incomeinitial['fiscalDateEnding']=="costOfRevenue"].iloc[0][1]
GROSSPROFIT_1=incomeinitial[incomeinitial['fiscalDateEnding']=="grossProfit"].iloc[0][1]
RD_1=incomeinitial[incomeinitial['fiscalDateEnding']=="researchAndDevelopment"].iloc[0][1]
GNA_1=incomeinitial[incomeinitial['fiscalDateEnding']=="sellingGeneralAndAdministrative"].iloc[0][1]
OE_1=incomeinitial[incomeinitial['fiscalDateEnding']=="operatingExpenses"].iloc[0][1]
IE_1=incomeinitial[incomeinitial['fiscalDateEnding']=="interestExpense"].iloc[0][1]
EBT_1=incomeinitial[incomeinitial['fiscalDateEnding']=="incomeBeforeTax"].iloc[0][1]
ITX_1=incomeinitial[incomeinitial['fiscalDateEnding']=="incomeTaxExpense"].iloc[0][1]
NE_1=incomeinitial[incomeinitial['fiscalDateEnding']=="netIncome"].iloc[0][1]


# In[92]:


COV_1


# In[93]:


REV=int(REV_1)/100000
COV=int(COV_1)/100000*-1
GROSSPROFIT=int(GROSSPROFIT_1)/100000
RD=int(RD_1)/100000
GNA=int(GNA_1)/100000
OE=int(OE_1)/100000
IE=int(IE_1)/100000*-1
EBT=int(EBT_1)/100000
ITX=int(ITX_1)/100000*-1
NE=int(NE_1)/100000


# In[94]:


COV


# In[98]:


import plotly.graph_objects as go

fig = go.Figure(go.Waterfall(
    name = "20", orientation = "v",
    measure = ["relative", "relative", "total", "relative", "relative", "total","relative","total","relative","total"],
    x = ["Total Revenue", "Cost Of Revenue", "Gross Profit", "Research And Development", "Selling General And Administrative", "Operating Expenses","Interest Expense","incomeBeforeTax","incomeTaxExpense","Net Income"],
    textposition = "outside",
    text = [REV, COV, GROSSPROFIT, RD, GNA, OE,IE,EBT,ITX,NE],
    y = [REV, COV,GROSSPROFIT,RD,GNA, OE, IE,EBT,ITX,NE],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
    increasing={"marker":{"color":"blue"}},
    decreasing={"marker":{"color":"yellow"}}
))

fig.update_layout(
        title = "Profit and loss statement available",
        showlegend = True
)

fig.show()


# In[ ]:





# In[ ]:





# In[ ]:




