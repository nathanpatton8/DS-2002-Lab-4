#!/usr/bin/env python
# coding: utf-8

# # LAB 4

# ## DIRECTIONS

# Due: Sunday at 11:59 P.M. via Collab and GitHub
# 
# Learning Objective
# 1.	Put into practice using Python to interact and call a public API successfully
# 2.	Look at the data within JSON and DataFrames
# 3.	Write your data to a local file (JSON)
# 4.	Use basic visualization to display information
# 5.	Interact with users
# 
# Challenge:
# You have seen some examples of how to interact with JSON, CSV and make API Calls. Take some time to explore the YAHOO Finance Guide https://syncwith.com/yahoo-finance/yahoo-finance-api which shows you endpoints for calling information. Your job is to code a Python Program that does the following things:
# 
# 1.	Takes user input for a stock (using the Ticker Symbol): IE with the input() command
# 2.	You will display back the user: Name Ticker, Full Name of the Stock, Current Price, Target Mean Price, Cash on Hand, Profit Margins
# 3.	Store the Results Locally in JSON Format with just those items and include a date of when that data was pulled
# 4.	Handle Errors (IE, the stock doesn’t exist and/or the API is not returning information)
# 
# You will have to read the documentation and figure out which modules to call to get the data that you need. You will need to make more than one call to this API. Use the examples in our Zoom Session to guide you, but the documentation will be enough. Post your code to GitHub.
# 
# Bonus –
# 1.	Use MatPlotLib to chart the historical price of a stock price’s highest value over the past 5 days. 

# ## CODE

# In[240]:


#Import Statements
import json
import requests 
import pandas
import datetime
from datetime import date
from matplotlib import pyplot as plt


# In[221]:


#Taking user input for a stock
stock = input()


# In[253]:


#Extracting data from API
header_var = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url1 = 'https://query1.finance.yahoo.com/v7/finance/quote'
query_str1 = {"symbols": stock}
response1 = requests.request("GET", url1, headers = header_var, params=query_str1)
stock_json1 = response1.json()

url2 = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/"
query_str2 = {"symbol": stock, "modules":"financialData"}
response2 = requests.request("GET", url2, headers = header_var, params=query_str2)
stock_json2 = response.json()


# In[248]:


#Declaring Variables and Handling Errors
try:
    long_name = stock_json1['quoteResponse']['result'][0]['longName']
    current_price = stock_json2["quoteSummary"]["result"][0]["financialData"]["currentPrice"]
    target_mean_price = stock_json2["quoteSummary"]["result"][0]["financialData"]["targetMeanPrice"]
    profit_margin = stock_json2["quoteSummary"]["result"][0]["financialData"]["profitMargins"]
    cash_on_hand = stock_json2["quoteSummary"]["result"][0]["financialData"]["freeCashflow"]
except IndexError:
    raise IndexError("Stock is not properly defined or server is down. Please input a valid ticker or try again later.")


# In[251]:


#Name Ticker
stock


# In[231]:


#long_name
long_name


# In[232]:


#current_price
current_price


# In[233]:


#target_mean_price
target_mean_price


# In[234]:


#profit_margin
profit_margin


# In[236]:


#cash_on_hand
cash_on_hand


# In[241]:


#Store the Results Locally in JSON Format with just those items and include a date of when that data was pulled
date = str(date.today())
dictionary = {"Name Ticker": stock,
              "Full Name of Stock": long_name,
              "Profit Margins": profit_margins,
              "Target Mean Price": target_mean_price,
              "Cash on Hand": cash_on_hand,
              "Current Price": current_price,
              "Date": date}
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)

dictionary


# In[250]:


#Use MatPlotLib to chart the historical price of a stock price’s highest value over the past 5 days.
url3 = "https://query1.finance.yahoo.com/v8/finance/chart/"
query_str3 = {"symbol": stock, "range": '5d', 'interval': '1d', 'metrics': 'high'}
response3 = requests.request("GET", url3, headers = header_var, params=query_str4)
stock_json3 = response.json()

