#!/usr/bin/env python
# coding: utf-8

# # Expense Tracker v1.0

# ### Simple Expense tracker to track everyday spenditures.

# In[2]:


# Imported Libraries

import numpy as np
import pandas as pd
from datetime import date


# In[3]:


# Lists

Goods_or_Services = []
Price = []
Date = []
Expense_Types = []


# In[4]:


# Functions to add expenses to lists and organize data

def add_expense(good_or_service, price, date, expense_type):
    Goods_or_Services.append(good_or_service)
    Price.append(price)
    Date.append(date)
    Expense_Types.append(expense_type)


# In[ ]:


# Program
# Creating option menu

option = -1 # Users option/input
while(option != 0):
    # Create option menu
    print('Welcome to the Expense Tracker v1.0:')
    print('1. Add Food Expense')
    print('2. Add Household Expense')
    print('3. Add Debt Expense')
    print('4. Add Transportation Expense')
    print('5. Show and Save Expense Report')
    print('0. Exit Tracker')
    option = int(input('Choose Option:\n'))
    
    # Print new line - Format
    print()
    # Check user input
    if option == 0:
        print('Exiting now')
        break
    elif option == 1:
        print('Adding Food')
        expense_type = 'Food'
    elif option == 2:
        print('Adding Household')
        expense_type = 'Household'
    elif option == 3:
        print('Adding Debt')
        expense_type = 'Debt'
    elif option == 4:
        print('Adding Transportation')
        expense_type = 'Transportation'
    elif option == 5:
        # New Data Frame and Add expenses
        expense_report = pd.DataFrame()
        expense_report['Goods_or_Services'] = Goods_or_Services
        expense_report['Price'] = Price
        expense_report['Date'] = Date
        expense_report['Expense_Types'] = Expense_Types
        # Save Expense Report
        expense_report.to_csv('ExpenseTracker.csv')
        # Show Report
        print(expense_report)
    else:
        print('Incorrect Selection. Please Choose Between 0, 1, 2, 3, 4, or 5')
        
    # Allow user to enter price, good or service
    if option == 1 or option == 2 or option == 3 or option == 4:
        good_or_service = input('Enter Good or Service for Expense Type '+expense_type+':\n')
        price = float(input('Enter Price/Cost of Good or Service:\n'))
        today = date.today()
        add_expense(good_or_service, price, today, expense_type)
    
    print()


# In[ ]:




